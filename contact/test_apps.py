from django.apps import apps
from django.test import TestCase
from contact.apps import ContactConfig

class ContactConfigTest(TestCase):
    
    def test_contact_config(self):
        self.assertEqual(ContactConfig.name, 'contact')
        self.assertEqual(apps.get_app_config('contact').name, 'contact')