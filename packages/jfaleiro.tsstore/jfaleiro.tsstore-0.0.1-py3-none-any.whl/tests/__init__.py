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
from hamcrest import assert_that, equal_to
from pandas.testing import assert_frame_equal


class AbstractFileSystemTests:

    def test_root_creates_dir(self, root):
        assert os.path.exists(root.root)

    def test_put(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')
        s.put('AAPL', ohlc_daily_adjusted)

    def test_double_put(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')
        s.put('AAPL', ohlc_daily_adjusted)
        s.put('AAPL', ohlc_daily_adjusted)
        assert_frame_equal(ohlc_daily_adjusted, s.get('AAPL'))

    def test_append(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')

        dfs = np.array_split(ohlc_daily_adjusted, 2)
        assert_that(len(dfs), equal_to(2))

        s.put('AAPL', dfs[0])
        assert_frame_equal(dfs[0], s.get('AAPL'))
        s.append('AAPL', dfs[1])
        assert_frame_equal(ohlc_daily_adjusted, s.get('AAPL'))

    def test_get(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')
        s.put('AAPL', ohlc_daily_adjusted)
        assert_frame_equal(ohlc_daily_adjusted, s.get('AAPL'))

    def test_all_stores(self, root, ohlc_daily_adjusted):
        dfs = np.array_split(ohlc_daily_adjusted, 10)
        for i, df in enumerate(dfs):
            ticker = f'T{i}'
            s = root.get_store(type='ohlcvds',
                               provider='alphavantage',
                               range='full')
            s.put(ticker, df)
        ss = list(root.all_stores)
        assert_that(len(ss), equal_to(1))

    def test_all_symbols(self, root, ohlc_daily_adjusted):
        s = root.get_store(type='ohlcvds',
                           provider='alphavantage',
                           range='full')
        symbols = [f'S{i}' for i in range(5)]
        for i in symbols:
            s.put(i, ohlc_daily_adjusted)

        stored = s.all_symbols
        assert_that(len(symbols), equal_to(len(stored)))
        assert_that(set(symbols), equal_to(set(stored)))
