from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from django.template.loader import render_to_string

from lists.views import home_page

class HomePageTest(TestCase):
    
    def test_home_page_returnsss_correct_html(self):
        response = self.client.get('/')
        self.assertTemplateUsed(response, 'home.html')

