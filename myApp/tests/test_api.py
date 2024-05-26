from django.test import TestCase, Client

from ..models import *

class ViewsTestCase(TestCase):

    client = Client()

    def init_user(self):
        if User.objects.filter(username='test_usn').exists():
            return User.objects.get(username='test_usn')
        return User.objects.create_user(username='test_usn', password='test_pw')

    def setUp(self):
        Memory.objects.create(
            user=self.init_user(),
            longitude=1000.0,
            latitude=1999.0,
            place_name='test_place',
            comments='test_comment'
        )

    def test_load_memory(self):
        self.client.login(username='test_usn', password='test_pw')
        response = self.client.get('/api/load-memory/')

        self.assertEqual(response.status_code, 200)
        self.assertJSONEqual(
            response.content,
            [
                {
                    'longitude': 1000.0,
                    'latitude': 1999.0,
                    'place_name': 'test_place',
                    'comments': 'test_comment'
                }
            ]
        )
        self.assertEqual(len(response.json()), 1)