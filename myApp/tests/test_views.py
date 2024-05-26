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

        Memory.objects.create(
            user=self.init_user(),
            longitude=2000.0,
            latitude=2999.0,
            place_name='test_place_2',
            comments='test_comment_2'
        )

    def test_dashboard(self):
        self.client.login(username='test_usn', password='test_pw')
        response = self.client.get('/dashboard/')

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'myApp/dashboard.html')

        self.assertEqual(len(response.context['memories']), 2)
