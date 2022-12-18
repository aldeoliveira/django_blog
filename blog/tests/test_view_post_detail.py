from django.test import TestCase
from django.urls import resolve, reverse

from blog import views
from unittest import skip


class TestPostDetailView(TestCase):
    def test_post_detail_calls_correct_view_function(self):
        view = resolve(reverse('blog:post_detail', kwargs={'slug': 'a-slug'}))
        self.assertIs(view.func.view_class, views.PostDetail)
    
    @skip('Test is not ready')
    def test_loads_correct_template(self):
        ...
