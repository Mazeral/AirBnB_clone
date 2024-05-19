import unittest
from ..models.base_model import BaseModel
import datetime
import uuid


class TestBaseClass(unittest.TestCase):
    def test_instance(self):
        """Tests if the instance is corrent"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)
        self.assertTrue(uuid.UUID(model.id))  # Validate UUID format
        self.assertEqual(model.created_at, model.updated_at)

    def test_str(self):
        """tests if the str is equal"""
        model = BaseModel()
        expected = f"[BaseModel] ({model.id}) ({model.__dict__})"
        self.assertEqual(str(model), expected)

    def test_save(self):
        model = BaseModel()
        model.save()
        self.assertNotEqual(model.created_at, model.updated_at)
        self.assertGreater(model.updated_at, model.created_at)

    def test_to_dictmethod(self):
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())
        self.assertIn('__class__', model_dict)
        self.assertEqual(model_dict['id'], model.id)
        self.assertEqual(model_dict['created_at'],
                         model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'],
                         model.updated_at.isoformat())
        self.assertIn('__class__', model_dict)


if __name__ == '__main__':
    unittest.main()
