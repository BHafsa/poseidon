#!/usr/bin/env python
#
#   Copyright (c) 2016 In-Q-Tel, Inc, All Rights Reserved.
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
"""
Test module for periodically

Created on 28 June 2016
@author: dgrossman, lanhamt
"""

from poseidon.periodically.periodically import doSleep
from poseidon.periodically.periodically import periodically


def test_sleepbad():
    assert not doSleep(-1)


def test_sleepgood():
    assert doSleep(1)


def test_periodically():
    a = periodically(1, 3, None)
    assert a == 3
