from django.test import TestCase
import app.controllers.collection as col
from django.http import Http404


class TestCollectionController(TestCase):
    fixtures = ['poet']

    def test_get_collection_or_404(self):
        result = col.get_collection_or_404(412)
        self.assertEqual(result['id'], 412)

        with self.assertRaises(Http404):
            col.get_collection_or_404(1)

    def test_clean_collection(self):
        reference = {
            'album_art_design': None,
            'collection_name': 'Eslam de poesía 33 Rojo Córdova CCD',
            'commentary': '',
            'id': 315,
            'image': 'images/13/Eslam_CCD_Radio.jpg',
            'origin': 'Slam de poesía',
            'release_state': 'PUBLICADO'
        }
        result = col.clean_collection(reference)
        self.assertDictEqual(result, {
            'album_art_design': None,
            'collection_name': 'Eslam de poesía 33 Rojo Córdova CCD',
            'commentary': None,
            'id': 315,
            'collection_id': 315,
            'image': '/media/images/13/Eslam_CCD_Radio.jpg',
            'origin': 'Slam de poesía',
            'release_state': 'PUBLICADO'
        })

    def test_get_recordings(self):
        pass




