#!/usr/bin/python3
"""Contains definition of TestBaseModel class.
"""


from models.base_model import BaseModel
from datetime import datetime
from unittest import TestCase


class TestBaseModel(TestCase):
    """Contains the individual tests for BaseModel class."""

    def test_uuid(self):
        """Tests whether different instances have unique uuid's."""
        base_m1 = BaseModel()
        self.assertIsInstance(base_m1, BaseModel)
        self.assertTrue(hasattr(base_m1, "id"))
        base_m2 = BaseModel()
        self.assertNotEqual(base_m1.id, base_m2.id)
        self.assertIsInstance(base_m1.id, str)

    def test_times(self):
        """Tests whether the object is assigned datetime attributes."""
        base_m1 = BaseModel()
        self.assertTrue(hasattr(base_m1, "created_at"))
        self.assertTrue(hasattr(base_m1, "updated_at"))
        self.assertIsInstance(base_m1.created_at, datetime)

    def test_save(self):
        """Tests if save function updates updated_at attribute."""
        base_m1 = BaseModel()
        first_update = base_m1.updated_at
        base_m1.save()
        new_update = base_m1.updated_at
        self.assertNotEqual(first_update, new_update)

    def test_to_dict(self):
        """Tests to_dict function of BaseModel class."""
        base_m1 = BaseModel()
        self.assertIsInstance(base_m1.__dict__, dict)
        self.assertEqual(len(base_m1.__dict__), 3)
        self.assertTrue("id" in base_m1.__dict__)
        self.assertTrue("created_at" in base_m1.__dict__)
        self.assertTrue("updated_at" in base_m1.__dict__)
        self.assertIsInstance(base_m1.to_dict(), dict)
        self.assertEqual(len(base_m1.to_dict()), 4)
        self.assertTrue("id" in base_m1.to_dict())
        self.assertTrue("created_at" in base_m1.to_dict())
        self.assertTrue("updated_at" in base_m1.to_dict())
        self.assertTrue("__class__" in base_m1.to_dict())

    def test_str(self):
        """Tests __str__ method of BaseModel."""
        base_m1 = BaseModel()
        class_name = base_m1.__class__.__name__
        comp_s = f"[{class_name}] ({base_m1.id}) {base_m1.__dict__}"
        self.assertEqual(comp_s, str(base_m1))
