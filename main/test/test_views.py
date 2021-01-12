from django.test import TestCase, Client
from django.urls import reverse
from main.models import Comment,Product,Person,Seller,Customer,mail_verification
import json


class TestMainViews (TestCase):
    def setUp(self):
        self.client=Client()
        self.url_home=reverse('home')#
        self.url_verify_code=reverse('verify_code',args=['tonytonytony'])#
        self.url_category=reverse('category',args=['hiiiii'])
        self.url_redirect_to_main=reverse('redirect_to_main')
        self.url_favourite=reverse('favourite')
        self.url_filter=reverse('filter')

    def test_home_get(self):
        response=self.client.get(self.url_home)
        self.assertEquals(response.status_code,200)
        self.assertTemplateUsed(response,'shop-category-left.html')

    def test_verify_code(self):
        response=self.client.get(self.url_verify_code)
        self.assertEquals(response.status_code, 302)





