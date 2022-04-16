from app import app
from unittest import TestCase

class TestApp(TestCase):
  '''This contains all the tests for the main app.py file.'''
  def test_make_baord(self):
    with app.test_client() as client:
      res = client.get('/')
      html = res.get_data(as_text=True)
      self.assertEqual(res.status_code, 200)