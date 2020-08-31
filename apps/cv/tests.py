from django.test import TestCase, Client
from .models import CV, Category, Item
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

class CategoryandItemPageTest(TestCase):

    def setUp(self):
        user = User.objects.create(username='testuser')
        user.set_password('12345')
        user.save()

    def test_uses_edit_category_template(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.get('/cv/category/new/')
        self.assertTemplateUsed(response, 'cv/edit_category.html')

    def test_uses_edit_item_template(self):
        self.client.login(username='testuser', password='12345')
        category = Category()
        category.title = 'test_category'
        category.save()
        response = self.client.get('/cv/category/1/new/')
        self.assertTemplateUsed(response, 'cv/edit_item.html')

    def test_can_save_a_category_POST_request(self):
        self.client.login(username='testuser', password='12345')
        self.client.post('/cv/category/new/', data={'title': 'test_title'})
        self.assertEqual(Category.objects.count(), 1)
        category = Category.objects.first()
        self.assertEqual(category.title, 'test_title')
    
    def test_redirects_after_category_POST(self):
        self.client.login(username='testuser', password='12345')
        response = self.client.post('/cv/category/new/', data={'title': 'test_title'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/edit')
        
    def test_only_saves_category_when_necessary(self):
        self.client.login(username='testuser', password='12345')
        self.client.get('/cv/category/new/')
        self.assertEqual(Category.objects.count(), 0)

    def test_can_save_a_item_POST_request(self):
        self.client.login(username='testuser', password='12345')
        category = Category()
        category.title = 'test_category'
        category.save()
        self.client.post('/cv/category/1/new/', data={'title': 'test_title', 'text': 'test_text'})
        self.assertEqual(Category.objects.count(), 1)
        item = Item.objects.first()
        self.assertEqual(item.title, 'test_title')
        self.assertEqual(item.text, 'test_text')
    
    def test_redirects_after_item_POST(self):
        self.client.login(username='testuser', password='12345')
        category = Category()
        category.title = 'test_category'
        category.save()
        response = self.client.post('/cv/category/1/new/', data={'title': 'test_category', 'text': 'test_text'})
        self.assertEqual(response.status_code, 302)
        self.assertEqual(response['location'], '/cv/category/1/list/')
        
    def test_only_saves_item_when_necessary(self):
        self.client.login(username='testuser', password='12345')
        category = Category()
        category.title = 'test_category'
        category.save()
        self.client.get('/cv/category/1/new/')
        self.assertEqual(Item.objects.count(), 0)

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

class CategoryAndItemModelTest(TestCase):

    def test_saving_and_retrieving_categories_and_items(self):
        category = Category()
        category.title = 'test_category'
        category.save()
        saved_categories = Category.objects.all()
        self.assertEqual(saved_categories.count(), 1)
        
        first_saved_category= saved_categories[0]
        self.assertEqual(first_saved_category.title, 'test_category')
        
        saved_items = category.items.all()
        self.assertEqual(saved_items.count(), 0)
        item1 = Item()
        item1.category = category
        item1.title = 'test_title_1'
        item1.text = 'test_text_1'
        item1.save()
        item2 = Item()
        item2.category = category
        item2.title = 'test_title_2'
        item2.text = 'test_text_2'
        item2.save()
        differentCategory = Category()
        differentCategory.title = 'test_category_2'
        differentCategory.save()
        itemForDifferentCategory = Item()
        itemForDifferentCategory.category = differentCategory
        itemForDifferentCategory.title = 'test_title_3'
        itemForDifferentCategory.text = 'test_text_3'
        itemForDifferentCategory.save()
        saved_items = category.items.all()
        self.assertEqual(saved_items.count(), 2)
        saved_items_different = differentCategory.items.all()
        self.assertEqual(saved_items_different.count(), 1)

        first_saved_item = saved_items[0]
        self.assertEqual(first_saved_item.title, 'test_title_1')
        self.assertEqual(first_saved_item.text, 'test_text_1')

        second_saved_item = saved_items[1]
        self.assertEqual(second_saved_item.title, 'test_title_2')
        self.assertEqual(second_saved_item.text, 'test_text_2')

        different_saved_item = saved_items_different[0]
        self.assertEqual(different_saved_item.title, 'test_title_3')
        self.assertEqual(different_saved_item.text, 'test_text_3')
    
    def test_editing_categories_and_items(self):
        category = Category()
        category.title = 'test_category'
        category.save()
    
        item = Item()
        item.category = category
        item.title = 'test_title'
        item.text = 'test_text'
        item.save()

        saved_items = category.items.all()
        self.assertEqual(saved_items.count(), 1)

        category.title = 'test_category_change'
        category.save()

        saved_items = category.items.all()
        self.assertEqual(saved_items.count(), 1)

        self.assertEqual(category.title, 'test_category_change')
        saved_item = saved_items[0]
        self.assertEqual(saved_item.title, 'test_title')
        self.assertEqual(saved_item.text, 'test_text')

        item.title = 'test_title_change'
        item.save()

        saved_items = category.items.all()
        self.assertEqual(saved_items.count(), 1)

        self.assertEqual(category.title, 'test_category_change')
        saved_item = saved_items[0]
        self.assertEqual(saved_item.title, 'test_title_change')
        self.assertEqual(saved_item.text, 'test_text')