from django.test import TestCase, SimpleTestCase
from django.urls import reverse

class AboutPageTest(SimpleTestCase):
  def test_about_status_code(self):
    url = reverse('about')
    actual = self.client.get(url)
    expected = 200
    self.assertEqual(actual.status_code, expected)

  def test_about_template(self):
    url = reverse('about')
    actual = self.client.get(url)
    expected = 'about.html'
    self.assertTemplateUsed(actual, expected)

class SnackTest(TestCase):
  def test_snack_status_code(self):
    url = reverse('snack_list')
    actual = self.client.get(url)
    expected = 200
    self.assertEqual(actual.status_code,expected)

  def test_snack_template(self):
    url = reverse('snack_list')
    actual = self.client.get(url)
    expected = 'snack_list.html'
    self.assertTemplateUsed(actual, expected)


# Create your tests here.
