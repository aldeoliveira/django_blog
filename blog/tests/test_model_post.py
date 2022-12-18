from django.test import TestCase
from django.core.exceptions import ValidationError
from django.db.utils import IntegrityError
from django.contrib.auth.models import User

from parameterized import parameterized
from unittest import skip

from blog.models import Post


class TestBlogModelPost(TestCase):
    def setUp(self) -> None:
        self.user = User.objects.create(username='test_user')

    def create_post_no_defaults(
        self,
        title='Default Title',
        slug='default-title',
        content='Default text.',
    ):
        return Post.objects.create(title=title, slug=slug, content=content, author=self.user)

    @parameterized.expand([
        ('title', 200),
        ('slug', 200)
    ])
    def test_post_fields_max_length(self, field, length):
        """Fields 'title' and 'slug' must have max lengths of 200 characters."""
        post = self.create_post_no_defaults()
        setattr(post, field, ('A' * (length + 1)))
        with self.assertRaises(ValidationError):
            post.full_clean()

    @parameterized.expand([
        ({'title': 'Title 1', 'slug': 'slug-1'}, {'title': 'Title 1', 'slug': 'slug-2'}),
        ({'title': 'Title 1', 'slug': 'slug-1'}, {'title': 'Title 2', 'slug': 'slug-1'}),
    ])
    def test_post_fields_that_must_be_unique(self, post1, post2):
        """Fields 'title' and 'slug' must be unique."""
        self.create_post_no_defaults(**post1)
        with self.assertRaises(IntegrityError):
            self.create_post_no_defaults(**post2)

    @skip('Test is not ready')
    def test_post_created_on_is_set_as_now_by_default(self):
        ...

    @skip('Test is not ready')
    def test_post_updated_on_is_set_as_now_by_default(self):
        ...

    @skip('Test is not ready')
    def test_post_created_on_doesnt_change_when_the_post_is_saved(self):
        ...

    @skip('Test is not ready')
    def test_post_updated_on_changes_when_the_post_is_saved(self):
        ...

    @skip('Test is not ready')
    def test_posts_are_ordered_by_created_on(self):
        ...

    def test_status_is_0_by_defaul(self):
        """A Post has status 0 by default."""
        post = self.create_post_no_defaults()
        self.assertEqual(post.status, 0)

    def test_string_representation_is_title(self):
        """The string representation of a Post is it's title."""
        title = 'Test Title'
        post = self.create_post_no_defaults(title=title)
        self.assertEqual(str(post), title)
