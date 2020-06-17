from django.test import TestCase

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'home.html')

    def test_can_save_a_POST_request(self):
        response = self.client.post('/cv/', data={'item_text': 'A new CV item'})
        self.assertIn('A new CV item', response.content.decode())
        self.assertTemplateUsed(response, 'home.html')
    
