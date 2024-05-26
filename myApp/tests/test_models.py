from django.test import TestCase

from ..models import *

class MemoryTestCase(TestCase):
    def init_user(self):
        if User.objects.filter(username='test_usn').exists():
            return User.objects.get(username='test_usn')
        return User.objects.create_user(username='test_usn', password='test_pw')

    def create_memory(self, lg=1000.0, lt=1999.0):
        return Memory.objects.create(
            user=self.init_user(),
            longitude=lg,
            latitude=lt,
            place_name='test_place',
            comments='test_comment'
        )

    def test_memory_create(self):
        memory = self.create_memory()
        self.assertTrue(isinstance(memory, Memory))

    def test_memory_fetch_all(self):
        self.create_memory()
        self.assertEqual(Memory.objects.count(), 1)

        self.create_memory(2000.0, 2999.0)
        self.assertEqual(Memory.objects.count(), 2)

    def test_memory_update(self):
        memory = self.create_memory()
        memory.place_name = 'new_place'
        memory.save()
        self.assertEqual(memory.place_name, 'new_place')

    def test_memory_delete(self):
        memory = self.create_memory()
        memory.delete()
        self.assertEqual(Memory.objects.count(), 0)
