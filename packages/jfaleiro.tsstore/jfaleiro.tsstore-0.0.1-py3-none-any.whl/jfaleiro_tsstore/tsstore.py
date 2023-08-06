#
#     tsstore - Fast and simple timeseries storage
#
#     Copyright (C) 2018 Jorge M. Faleiro Jr.
#
#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU Affero General Public License as published
#     by the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.
#
#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU Affero General Public License for more details.
#
#     You should have received a copy of the GNU Affero General Public License
#     along with this program.  If not, see <http://www.gnu.org/licenses/>.
#     '
#     '
import os
from abc import ABC, abstractmethod, abstractproperty

import pandas as pd


class AbstractRoot(ABC):

    def __init__(self, root: str):
        self.root = root

    @abstractproperty
    def all_stores(self):
        raise NotImplementedError()

    @abstractmethod
    def get_store(self, **kwargs):
        raise NotImplementedError()

    def purge_all(self):
        for s in self.all_stores:
            s.delete()


class AbstractStore(ABC):

    @abstractmethod
    def put(self, ticker: str, df: pd.DataFrame):
        raise NotImplementedError()

    @abstractmethod
    def get(self, ticker: str) -> pd.DataFrame:
        raise NotImplementedError()

    @abstractmethod
    def append(self, ticker: str, df: pd.DataFrame) -> None:
        raise NotImplementedError()

    @abstractmethod
    def delete(self) -> None:
        raise NotImplementedError()

    @abstractproperty
    def all_symbols(self):
        raise NotImplementedError()


def root(path: str, type_: str = 'fastparquet') -> AbstractRoot:
    def fastparquet(p):
        from .fastparquet import FastParquetRoot
        return FastParquetRoot(p)

    def dask(p):
        from .dask import DaskRoot
        return DaskRoot(p)

    roots = dict(
        fastparquet=fastparquet,
        dask=dask,
    )

    if type_ in roots:
        return roots[type_](os.path.expanduser(path))
    else:
        raise ValueError(f'invalid {type_}, valid: {roots.keys()}')
