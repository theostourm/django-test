import unittest

from django.test import TestCase
from django.test.client import RequestFactory
from blog.views import PostList


class PostListTest(unittest.TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get(self):
        # create a GET request.
        request = self.factory.get('/posts/')

        # test the view
        response = PostList.get(self, request)
        self.assertEqual(response.status_code, 200)

    def test_post(self):
        # create a POST request.
        request = self.factory.post('/posts/')

        # test the view
        response = PostList.post(self, request)
        self.assertEqual(response.status_code, 200)
