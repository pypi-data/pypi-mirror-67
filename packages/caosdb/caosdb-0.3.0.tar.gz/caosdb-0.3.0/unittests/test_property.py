# -*- encoding: utf-8 -*-
#
# ** header v3.0
# This file is a part of the CaosDB Project.
#
# Copyright (C) 2018 Research Group Biomedical Physics,
# Max-Planck-Institute for Dynamics and Self-Organization Göttingen
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program. If not, see <https://www.gnu.org/licenses/>.
#
# ** end header
#
"""Tests for the Property class."""
# pylint: disable=missing-docstring
from nose.tools import (assert_is_not_none as there, assert_true as tru,
                        assert_equal as eq)
from caosdb import Entity, Property, configure_connection
from caosdb.connection.mockup import MockUpServerConnection


def setup_module():
    there(Property)
    configure_connection(url="unittests", username="testuser",
                         password="testpassword", timeout=200,
                         implementation=MockUpServerConnection)


def hat(obj, attr):
    tru(hasattr(obj, attr))


def test_is_entity():
    prop = Property()
    tru(isinstance(prop, Entity))


def test_instance_variables():
    prop = Property()
    hat(prop, "datatype")
    hat(prop, "unit")
    hat(prop, "value")


def test_role():
    prop = Property()
    eq(prop.role, "Property")
