from django.test import TestCase
from .form import ItemForm

class TestItemForm(TestCase):
    
    def trst_item_name_is_required(self):
        form = ItemForm({'name':''})
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())

