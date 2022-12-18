from django.test import TestCase
from django.urls import resolve, reverse

from blog import views
from unittest import skip


class TestHomeView(TestCase):
    def test_calls_correct_function(self):
        view = resolve(reverse('blog:home'))
        self.assertIs(view.func.view_class, views.PostList)

    @skip('Test is not ready')
    def test_loads_only_published_posts(self):
        ...
    
    @skip('Test is not ready')
    def test_posts_are_ordered_by_created_on(self):
        ...
    
    @skip('Test is not ready')
    def test_loads_correct_template(self):
        ...
