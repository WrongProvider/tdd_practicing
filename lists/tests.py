from django.test import TestCase
from django.template.loader import render_to_string
from django.http import HttpRequest
from django.urls import resolve
from lists.views import home_page

# Create your tests here.
class HomePageTest(TestCase):
    def test_home_page_returns_correct_html(self):
        response = self.client.get('/')  

        html = response.text  
        self.assertTrue(html.startswith('<html>'))
        self.assertIn('<title>To-Do lists</title>', html)
        self.assertTrue(html.strip().endswith('</html>'))

        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/', data={'item_text': 'A new list item'})
        self.assertIn('A new list item', response.text)
        self.assertTemplateUsed(response, 'home.html')
