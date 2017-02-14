from django.test import TestCase
from django.contrib.auth.models import User
from payment.models import UserContent, Content


# Create your tests here.
class SimpleTest(TestCase):
    def setUp(self):
        self.user1 = User.objects.create_user('test_user1', password='0000')
        self.user2 = User.objects.create_user('test_user2', password='1111')
        self.content1 = Content.objects.create(subject="test_content1", price=1000)
        self.content2 = Content.objects.create(subject="test_content2", price=3000)
        self.content3 = Content.objects.create(subject="test_content3", price=5000)

        UserContent.objects.create_usercontent(self.user1.id, self.content1.id)
        UserContent.objects.create_usercontent(self.user2.id, self.content1.id)
        UserContent.objects.create_usercontent(self.user2.id, self.content2.id)
        UserContent.objects.create_usercontent(self.user2.id, self.content3.id)

    def test_payment_sum(self):
        payment_sum_1 = self.user1.get_payment_sum()
        payment_sum_2 = self.user2.get_payment_sum()

        self.assertEqual(payment_sum_1, 1000)
        self.assertEqual(payment_sum_2, 9000)

    def test_content_buy_count(self):
        content_buy_count_1 = self.content1.get_content_buy_count()
        content_buy_count_2 = self.content2.get_content_buy_count()
        content_buy_count_3 = self.content3.get_content_buy_count()

        self.assertEqual(content_buy_count_1, 2)
        self.assertEqual(content_buy_count_2, 1)
        self.assertEqual(content_buy_count_3, 1)
