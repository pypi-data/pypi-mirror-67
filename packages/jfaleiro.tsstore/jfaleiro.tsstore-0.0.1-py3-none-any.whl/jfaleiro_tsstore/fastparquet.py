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

import fastparquet as fp
import pandas as pd

from .filesystem import (METADATA, AbstractFilesystemRoot,
                         AbstractFilesystemStore)


class FastParquetRoot(AbstractFilesystemRoot):
    def __init__(self, root: str):
        self.root = root

    def get_store(self, **kwargs):
        return FastParquetStore(self.root, **kwargs)


class FastParquetStore(AbstractFilesystemStore):

    SYMBOL_EXTENSION = '.__parquet__'

    def __init__(self, root: str, **kwargs: dict):
        self.root = root
        self.attributes = kwargs

    def _write(self, ticker, df: pd.DataFrame, append) -> None:
        fp.write(self.filename(ticker), df, file_scheme='hive', compression='GZIP',
                 append=append)
        with open(os.path.join(self.path, METADATA), 'w') as f:
            f.write(json.dumps(self.attributes))

    def put(self, ticker: str, df: pd.DataFrame) -> None:
        os.makedirs(self.path, exist_ok=True)
        self._write(ticker, df, append=False)

    def append(self, ticker: str, df: pd.DataFrame) -> None:
        self._write(ticker, df, append=True)

    def prepend(self, ticker: str, df: pd.DataFrame) -> None:
        current = self.get(ticker)
        self.put(ticker, df)
        self.append(ticker, current)

    def _get(self, ticker: str) -> pd.DataFrame:
        return fp.ParquetFile(self.filename(ticker)).to_pandas()
