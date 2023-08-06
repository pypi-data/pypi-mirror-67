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

import dask.dataframe as dd
import pandas as pd

from .filesystem import (METADATA, AbstractFilesystemRoot,
                         AbstractFilesystemStore)


class DaskRoot(AbstractFilesystemRoot):
    def __init__(self, root: str):
        self.root = root

    def get_store(self, **kwargs):
        return DaskStore(self.root, **kwargs)


class DaskStore(AbstractFilesystemStore):

    SYMBOL_EXTENSION = '.__dask__'

    def __init__(self, root: str, **kwargs: dict):
        self.root = root
        self.attributes = kwargs
        os.makedirs(self.path, exist_ok=True)
        with open(os.path.join(self.path, METADATA), 'w') as f:
            f.write(json.dumps(self.attributes))

    def put(self, ticker: str, df: pd.DataFrame) -> None:
        os.makedirs(self.filename(ticker), exist_ok=True)
        dd.to_parquet(df=dd.from_pandas(data=df, npartitions=1),
                      path=self.filename(ticker))

    def append(self, ticker: str, df: pd.DataFrame) -> None:
        fn = self.filename(ticker)
        _ = (dd.read_parquet(fn)
             .append(dd.from_pandas(data=df, npartitions=1))
             .to_parquet(fn))

    def prepend(self, ticker: str, df: pd.DataFrame) -> None:
        fn = self.filename(ticker)
        _ = (dd.from_pandas(data=df, npartitions=1)
             .append(dd.read_parquet(fn))
             .to_parquet(fn))

    def _get(self, ticker: str) -> pd.DataFrame:
        return dd.read_parquet(path=self.filename(ticker)).compute()
