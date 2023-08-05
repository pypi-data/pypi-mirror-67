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


"""Provide compound extraction, transformation, and loading (ETL) functions."""


import logging
from typing import Any, Coroutine

import httpx
from sqlalchemy.orm import sessionmaker


__all__ = ("kegg_mol_fetcher",)


logger = logging.getLogger(__name__)


Session = sessionmaker()


def kegg_mol_fetcher(
    identifier: str, client: httpx.AsyncClient
) -> Coroutine[Any, Any, httpx.Response]:
    """
    Prepare an asynchronous HTTP call to retrieve a KEGG MDL MOL block.

    Parameters
    ----------
    identifier : str
        The KEGG compound identifier.
    client : httpx.AsyncClient
        An httpx asynchronous client with a `base_url` set.

    Returns
    -------
    coroutine
        A `client.get` call that can be awaited by the caller of this function.

    """
    return client.get(f"{identifier}/mol")
