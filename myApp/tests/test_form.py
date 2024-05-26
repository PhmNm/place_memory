from django.test import TestCase, Client

from ..models import *

from ..forms import *

class FormsTestCase(TestCase):
    
    def test_memory_form(self):
        form = MemoryForm(data={
            'longitude': 1000.0,
            'latitude': 1999.0,
            'place_name': 'test_place',
            'comments': 'test_comment'
        })

        self.assertTrue(form.is_valid())
        self.assertEqual(form.cleaned_data['longitude'], 1000.0)
        self.assertEqual(form.cleaned_data['latitude'], 1999.0)
        self.assertEqual(form.cleaned_data['place_name'], 'test_place')
        self.assertEqual(form.cleaned_data['comments'], 'test_comment')