from django.test import TestCase
from django.urls import reverse


class TestBlogUrls(TestCase):
    def test_blog_home_url_is_correct(self):
        url = reverse('blog:home')
        self.assertEqual(url, '/')
    
    def test_blog_post_url_is_correct(self):
        url = reverse('blog:post_detail', kwargs={'slug': 'a-post'})
        self.assertEqual(url, '/a-post/')
