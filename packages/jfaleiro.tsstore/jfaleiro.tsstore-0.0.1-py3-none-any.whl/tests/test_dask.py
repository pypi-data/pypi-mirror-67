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

import dask.dataframe as dd
import numpy as np
import pandas as pd
import pytest
from pandas.testing import assert_frame_equal

from jfaleiro_tsstore import root as tsstore_root

from . import AbstractFileSystemTests


@pytest.fixture
def ohlc_daily_adjusted():
    result = pd.read_csv(
        os.path.join('tests', 'data',
                     'alpaca_alphavantage_raw_df_ohlcvds_AAPL_daily_full.csv'),
        index_col='date')
    mapping = {v: v[3:].replace(' ', '_') for v in result.columns}
    return result.rename(columns=mapping).sort_index()


@pytest.fixture
def root(tmp_path):
    return tsstore_root(tmp_path, type_='dask')


class TestDask(AbstractFileSystemTests):
    def test_dask_append(self, tmp_path, ohlc_daily_adjusted):
        dfs = np.array_split(ohlc_daily_adjusted, 2)
        dd1 = dd.from_pandas(dfs[0], npartitions=1)
        dd2 = dd.from_pandas(dfs[1], npartitions=1)

        dd1.to_parquet(tmp_path)

        _ = (dd.read_parquet(tmp_path)
             .append(dd2)
             .to_parquet(tmp_path))

        assert_frame_equal(ohlc_daily_adjusted,
                           dd.read_parquet(tmp_path).compute())

    def test_dask_append_flag(self, tmp_path, ohlc_daily_adjusted):
        dfs = np.array_split(ohlc_daily_adjusted, 2)
        dd1 = dd.from_pandas(dfs[0], npartitions=1)
        dd2 = dd.from_pandas(dfs[1], npartitions=1)

        dd1.to_parquet(tmp_path)
        dd.to_parquet(df=dd2, path=tmp_path, append=True)

        assert_frame_equal(ohlc_daily_adjusted,
                           dd.read_parquet(tmp_path).compute())

    def test_dask_prepend_error(self, tmp_path, ohlc_daily_adjusted):
        dfs = np.array_split(ohlc_daily_adjusted, 2)
        dd1 = dd.from_pandas(dfs[0], npartitions=1)
        dd2 = dd.from_pandas(dfs[1], npartitions=1)

        dd2.to_parquet(tmp_path)

        with pytest.raises(BaseException):
            _ = (dd1
                 .append(dd.read_parquet(tmp_path))
                 .to_parquet(tmp_path))

            assert_frame_equal(ohlc_daily_adjusted,
                               dd.read_parquet(tmp_path).compute())


def test_dask_intermittent_error(tmp_path):
    df = pd.DataFrame(np.random.randn(100, 1), columns=['A'],
                      index=pd.date_range('20130101', periods=100, freq='T'))
    dfs = np.array_split(df, 2)

    dd1 = dd.from_pandas(dfs[0], npartitions=1)
    dd2 = dd.from_pandas(dfs[1], npartitions=1)

    dd2.to_parquet(tmp_path)

    with pytest.raises(BaseException):
        _ = (dd1
             .append(dd.read_parquet(tmp_path))
             .to_parquet(tmp_path))

        assert_frame_equal(df,
                           dd.read_parquet(tmp_path).compute())


def test_dask_prepend_as_append(tmp_path):
    df = pd.DataFrame(np.random.randn(100, 1), columns=['A'],
                      index=pd.date_range('20130101', periods=100, freq='T'))
    dfs = np.array_split(df, 2)

    dd1 = dd.from_pandas(dfs[0], npartitions=1)
    dd2 = dd.from_pandas(dfs[1], npartitions=1)

    dd2.to_parquet(tmp_path)
    with pytest.raises(ValueError):
        dd1.to_parquet(tmp_path, append=True)

        assert_frame_equal(df,
                           dd.read_parquet(tmp_path).compute())
