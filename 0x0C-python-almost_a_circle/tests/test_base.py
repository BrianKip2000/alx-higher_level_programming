#!/usr/bin/python3
import unittest
from models.base import Base


class TestClass(unittest.TestCase):
    def test_init_id(self):
        obj_0 = Base(id=10)
        self.assertEqual(obj_0.id, 10)

