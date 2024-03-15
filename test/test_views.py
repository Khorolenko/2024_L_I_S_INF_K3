import unittest
from hello_world import app
from hello_world.formater import SUPPORTED


class FlaskrTestCase(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        self.app = app.test_client()

    def test_outputs(self):
        rv = self.app.get('/outputs')
        s = str(rv.data)
        ','.join(SUPPORTED) in s

    def test_msg_with_output(self):
        rv = self.app.get('/?output=json')
<<<<<<< HEAD
        self.assertEqual(b'{ "imie":"Oleksandra", "mgs":"Hello World!"}', rv.data)
=======
        self.assertEqual(b'{ "imie":"Oleksandra", "msg":"Hello World!"}', rv.data)
>>>>>>> 2fc5dbf31eb4843083333a0ca0ee75606964f70f
