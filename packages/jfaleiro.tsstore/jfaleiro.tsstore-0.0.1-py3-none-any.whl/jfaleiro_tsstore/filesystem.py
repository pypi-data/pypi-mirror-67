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
import json
import os
import shutil
from abc import abstractmethod, abstractproperty
from pathlib import Path

import pandas as pd

from .tsstore import AbstractRoot, AbstractStore

METADATA = 'jfaleiro_tsstore.metadata'


class AbstractFilesystemRoot(AbstractRoot):
    @property
    def all_stores(self):
        for f in Path(os.path.join(self.root)).rglob(METADATA):
            with open(f) as file_:
                attributes = json.load(file_)
            yield self.get_store(**attributes)


class AbstractFilesystemStore(AbstractStore):
    def __init__(self, root: str, **kwargs: dict):
        self.root = root
        self.attributes = kwargs

    @abstractproperty
    @classmethod
    def SYMBOL_EXTENSION(cls):
        raise NotImplementedError()

    @property
    def path(self):
        return os.path.join(self.root, *[f'{k}_{self.attributes[k]}'
                                         for k in sorted(self.attributes)])

    @property
    def all_symbols(self):
        return [f.stem
                for f in Path(os.path.join(
                    self.root)).rglob(f'*{type(self).SYMBOL_EXTENSION}')]

    def filename(self, ticker: str) -> None:
        return os.path.join(self.path, f'{ticker}{type(self).SYMBOL_EXTENSION}')

    def delete(self) -> None:
        shutil.rmtree(self.path)

    def get(self, ticker: str) -> pd.DataFrame:
        return None if not os.path.exists(self.filename(ticker)) else self._get(ticker)

    @abstractmethod
    def _get(self, ticker: str) -> pd.DataFrame:
        raise NotImplementedError()
