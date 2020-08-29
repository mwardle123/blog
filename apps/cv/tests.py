from django.test import TestCase, Client
from .models import Item, CV
from django.contrib.auth.models import User

class HomePageTest(TestCase):

    def test_uses_home_template(self):
        response = self.client.get('/cv/')
        self.assertTemplateUsed(response, 'cv/home.html')

    def test_displays_all_cv_items(self):
        CV.objects.create(title='CV',name='test_name',address='test_address',mobile_number='test_mobile_number',email='test_email',personal_profile='test_personal_profile')
        
        response = self.client.get('/cv/')

        self.assertIn('test_name', response.content.decode())
        self.assertIn('test_address', response.content.decode())
        self.assertIn('test_mobile', response.content.decode())
        self.assertIn('test_email', response.content.decode())
        self.assertIn('test_personal_profile', response.content.decode())

class EditPageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_uses_edit_template(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/cv/edit/')
        self.assertTemplateUsed(response, 'cv/edit.html')

    def test_can_save_a_POST_request(self):
        self.client.login(username='testuser', password='12345')
        self.client.post('/cv/edit/', data={'name': 'test_name', 'address': 'test_address', 'mobile_number': 'test_mobile', 'email': 'test_email', 'personal_profile': 'test_personal_profile'})
        self.assertEqual(CV.objects.count(), 1)
        cv = CV.objects.first()
        self.assertEqual(cv.name, 'test_name')
        self.assertEqual(cv.address, 'test_address')
        self.assertEqual(cv.mobile_number, 'test_mobile')
        self.assertEqual(cv.email, 'test_email')
        self.assertEqual(cv.personal_profile, 'test_personal_profile')

    def test_redirects_after_POST(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/cv/edit/', data={'name': 'Matthew Wardle', 'address': 'test_address', 'mobile_number': 'test_mobile', 'email': 'test_email', 'personal_profile': 'test_personal_profile'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/')
        
    def test_only_saves_items_when_necessary(self):
        self.client.login(username='testuser', password='12345')
        self.client.get('/cv/edit')
        self.assertEqual(CV.objects.count(), 0)

class CVModelTest(TestCase):

    def test_saving_and_retrieving_items(self):
        cv = CV()
        cv.name = 'test_name'
        cv.address = 'test_address'
        cv.mobile_number = 'test_mobile'
        cv.email = 'test_email'
        cv.personal_profile = 'test_personal_profile'
        cv.save()

        saved_items = CV.objects.all()
        self.assertEqual(saved_items.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.name, 'test_name')
        self.assertEqual(first_saved_item.address, 'test_address')
        self.assertEqual(first_saved_item.mobile_number, 'test_mobile')
        self.assertEqual(first_saved_item.email, 'test_email')
        self.assertEqual(first_saved_item.personal_profile, 'test_personal_profile')

    
