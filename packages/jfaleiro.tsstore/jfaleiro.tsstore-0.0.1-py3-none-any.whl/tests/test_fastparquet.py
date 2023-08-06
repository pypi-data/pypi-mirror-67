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

import numpy as np
import pandas as pd
import pytest
from hamcrest import assert_that, equal_to
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
    return tsstore_root(tmp_path, type_='fastparquet')


class TestFastParquet(AbstractFileSystemTests):

    def test_prepend(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')

        dfs = np.array_split(ohlc_daily_adjusted, 2)
        assert_that(len(dfs), equal_to(2))

        s.put('AAPL', dfs[1])
        assert_frame_equal(dfs[1], s.get('AAPL'))
        s.prepend('AAPL', dfs[0])
        assert_frame_equal(ohlc_daily_adjusted, s.get('AAPL'))
