from _typeshed import Self
from django.test import SimpleTestCase


class SimpleTests(SimpleTestCase):
    def test_home_page_status_code(self):
        response = self.client.get("/")
        self.assertEqual(response.stauts_code, 200)

    def test_about_page_status_code(self):
        response = self.client.get("/about/")
        self.assertEqual(response.status_code, 200)
    
    def test_home_page_uses_correct_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "home.html")

    def test_home_page_uses_correct_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "about.html")

    def test_home_page_extends_base_template(self):
        response = self.client.get("/")
        self.assertTemplateUsed(response, "base.html")

    def test_home_page_uses_extends_base_template(self):
        response = self.client.get("/about/")
        self.assertTemplateUsed(response, "base.html")




