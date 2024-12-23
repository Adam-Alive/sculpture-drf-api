from django.contrib.auth.models import User
from .models import Post
from rest_framework import status
from rest_framework.test import APITestCase


class PostListViewTests(APITestCase):
    def setUp(self):
        User.objects.create_user(username='jack', password='pass')

    def test_can_list_posts(self):
        jack = User.objects.get(username='jack')
        Post.objects.create(owner=jack, title='a title')
        response = self.client.get('/posts/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        print(response.data)
        print(len(response.data))

    def test_user_not_logged_in_cant_create_post(self):
        response = self.client.post('/posts/', {'title': 'a title'})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)


class PostDetailViewTests(APITestCase):
    def setUp(self):
        jack = User.objects.create_user(username='jack', password='pass')
        jane = User.objects.create_user(username='jane', password='pass')
        Post.objects.create(
            owner=jack, title='a title', artist='artist one',
            street='street one', postcode='postcode one', borough='borough one'
        )
        Post.objects.create(
            owner=jane, title='another title', artist='artist two',
            street='street two', postcode='postcode two', borough='borough two'
        )

    def test_can_retrieve_post_using_valid_id(self):
        response = self.client.get('/posts/1/')
        self.assertEqual(response.data['title'], 'a title')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_cant_retrieve_post_using_invalid_id(self):
        response = self.client.get('/posts/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
