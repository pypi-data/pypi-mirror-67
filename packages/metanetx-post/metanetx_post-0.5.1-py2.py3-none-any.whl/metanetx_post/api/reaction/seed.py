# Copyright (c) 2020, Moritz E. Beber.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


"""Provide a high-level SEED reaction API."""


import logging
from typing import Collection, Dict, Set

import httpx
import pandas as pd
from cobra_component_models.orm import (
    Namespace,
    Reaction,
    ReactionAnnotation,
    ReactionName,
)
from sqlalchemy.orm import sessionmaker
from tqdm import tqdm

from ...model import SEEDReactionsModel


__all__ = ()


logger = logging.getLogger(__name__)


Session = sessionmaker()


def extract(
    url: str = "https://raw.githubusercontent.com/ModelSEED/ModelSEEDDatabase/dev"
    "/Biochemistry/reactions.json",
) -> str:
    """
    Fetch all SEED reactions as JSON.

    Parameters
    ----------
    url : str, optional
        The URL to query for the SEED reaction file.

    Raises
    ------
    httpx.HTTPError
        In case the HTTP response status code was in the 400 or 500 range.

    """
    response = httpx.get(url)
    response.raise_for_status()
    # We return the response's `text` attribute (rather than the `raw` attribute) so
    # that the HTTP response body is already correctly encoded.
    return response.text


def transform(response: str) -> Dict[str, Set[str]]:
    """
    Generate a mapping of SEED reaction identifiers to names.

    Parameters
    ----------
    response : str
        The JSON response containing BiGG universal reactions.

    Returns
    -------
    dict
        A map of BiGG reaction identifiers to names.

    Raises
    ------
    pydantic.ValidationError
        In case the JSON response data has an unexpected format.

    """
    reactions = SEEDReactionsModel.parse_raw(response)
    mapping = {}
    for reaction in reactions.__root__:
        names = {reaction.name}
        if reaction.aliases is not None:
            for line in reaction.aliases:
                if line.startswith("Name:"):
                    names.update(n.strip() for n in line[5:].split(";"))
                    break
        mapping[reaction.id] = names
    return mapping


def load(
    session: Session, id2names: Dict[str, Collection[str]], batch_size: int = 1000,
) -> None:
    """
    Load SEED reaction names into a database.

    Parameters
    ----------
    session : sqlalchemy.orm.session.Session
        An active session in order to communicate with a SQL database.
    id2names : dict
        A map of SEED reaction identifiers to names.
    batch_size : int, optional
        The size of batches to process the data in.

    """
    # Fetch all reactions from the database that have SEED identifiers.
    seed_ns: Namespace = session.query(Namespace).filter(
        Namespace.prefix == "seed.reaction"
    ).one()
    query = (
        session.query(Reaction.id, ReactionAnnotation.identifier)
        .select_from(Reaction)
        .join(ReactionAnnotation)
        .join(Namespace)
        .filter(Namespace.id == seed_ns.id)
    )
    df = pd.read_sql_query(query.statement, session.bind)
    # Only unique names per reaction and namespace are allowed. Thus we group the
    # data by reaction index so that we can later make the names unique.
    grouped = df.groupby("id", as_index=False, sort=False)
    reaction_ids = df["id"].unique()
    with tqdm(total=len(reaction_ids), desc="Reaction") as pbar:
        for index in range(0, len(reaction_ids), batch_size):
            mappings = []
            batch = reaction_ids[index : index + batch_size]
            for rxn_id in batch:
                sub = grouped.get_group(rxn_id)
                # Create unique names per reaction.
                names = set()
                for seed_id in sub["identifier"]:
                    if labels := id2names.get(seed_id, None):
                        names.update(labels)
                # Apparently, `numpy.int` ends up as a BLOB in the database. We
                # convert to native `int` here.
                mappings.extend(
                    {"reaction_id": int(rxn_id), "namespace_id": seed_ns.id, "name": n,}
                    for n in names
                )
            session.bulk_insert_mappings(ReactionName, mappings)
            session.commit()
            pbar.update(len(batch))
