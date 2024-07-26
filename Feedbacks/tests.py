# feedbacks/tests/test_views.py

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient
from django.contrib.auth.models import User
from .models import Question, Answer
from Forms.models import Form

class FeedbacksAPITestCase(APITestCase):

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='password')
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

        self.form = Form.objects.create(
            author=self.user,
            form_type='survey',
            description='A test form'
        )

        self.question = Question.objects.create(
            user=self.user,
            form=self.form,
            question_type='survey',
            title='Test Question',
            body='This is a test question.'
        )

        self.answer = Answer.objects.create(
            user=self.user,
            question=self.question,
            text='This is a test answer.'
        )

    def test_question_list_view(self):
        url = reverse('Feedbacks:question')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question_create_view(self):
        url = reverse('Feedbacks:question_create')
        data = {
            'user': self.user.id,
            'form': self.form.id,
            'question_type': 'quiz',
            'title': 'New Test Question',
            'body': 'This is another test question.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_question_update_view(self):
        url = reverse('Feedbacks:question_update', kwargs={'pk': self.question.pk})
        data = {
            'title': 'Updated Test Question',
            'body': 'This is an updated test question.'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.question.refresh_from_db()
        self.assertEqual(self.question.title, 'Updated Test Question')

    def test_question_delete_view(self):
        url = reverse('Feedbacks:question_delete', kwargs={'pk': self.question.pk})
        response = self.client.delete(url)
        self.assertFalse(Question.objects.filter(pk=self.question.pk).exists())

    def test_answer_list_view(self):
        url = reverse('Feedbacks:answer_list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_answer_create_view(self):
        url = reverse('Feedbacks:answer_create')
        data = {
            'user': self.user.id,
            'question': self.question.id,
            'text': 'This is a new test answer.'
        }
        response = self.client.post(url, data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_answer_update_view(self):
        url = reverse('Feedbacks:answer_update', kwargs={'pk': self.answer.pk})
        data = {
            'text': 'This is an updated test answer.'
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.answer.refresh_from_db()
        self.assertEqual(self.answer.text, 'This is an updated test answer.')

    def test_answer_delete_view(self):
        url = reverse('Feedbacks:answer_delete', kwargs={'pk': self.answer.pk})
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertFalse(Answer.objects.filter(pk=self.answer.pk).exists())
