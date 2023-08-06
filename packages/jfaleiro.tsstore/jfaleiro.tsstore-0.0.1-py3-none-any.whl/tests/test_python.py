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
from abc import ABC, abstractmethod


def test_kwargs():
    class A:
        def m(self, **kw):
            return kw['a'] + kw['b']
    a = A()
    assert a.m(a=1, b=2) == 3


def test_kwargs_abstract():
    class B(ABC):
        @abstractmethod
        def m(self, **kw):
            pass

    class A(B):
        def m(self, **kw):
            return kw['a'] + kw['b']
    a = A()
    assert a.m(a=1, b=2) == 3
