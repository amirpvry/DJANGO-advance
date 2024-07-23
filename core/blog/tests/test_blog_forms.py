from django.test import TestCase , SimpleTestCase
from django.urls import reverse, resolve
from blog.views import PostDetailView
from ..models import Categories
from ..forms import PostForm
from accounts.models import User


# Create your tests here.
class PostFormTest(TestCase):
        def setUp(self):
        # ایجاد یک کاربر تستی
            self.user = User.objects.create_user(username='testuser', password='12345')
        # ایجاد یک دسته‌بندی تستی
            self.category = Categories.objects.create(name='test')

        def test_form_post_with_valid_data(self):
            form = PostForm(data={
                'title': 'Test Post',
                'content': 'This is a test post.',
                'author': self.user.id,
                'categories': [self.category.id]
            })
            self.assertTrue(form.is_valid())