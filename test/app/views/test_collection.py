from django.test import TestCase


class TestCollection(TestCase):
    fixtures = ['poet']

    def setUp(self):
        self.response = self.client.get('/coleccion/315')
        self.response_404 = self.client.get('/coleccion/1')

    def test_200_collection(self):
        self.assertEqual(self.response.status_code, 200)

    def test_csrf(self):
        self.assertContains(self.response, 'csrf-token')

    def test_entity_contains_search(self):
        self.assertContains(self.response, 'search-form')

    def test_entity_contains_audio(self):
        self.assertContains(self.response, 'wavesurfer-container')

    def test_404_page(self):
        self.assertEqual(self.response_404.status_code, 404)
