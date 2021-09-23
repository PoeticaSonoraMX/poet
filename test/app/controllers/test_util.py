from django.test import TestCase
from unittest.mock import ANY
import app.controllers.util as u
from django.http import Http404


class TestUtils(TestCase):
    fixtures = ['poet']

    def test_query(self):
        res = u.query('SELECT * FROM poet_work WHERE id = %s', [1])[0]['full_name']
        self.assertEqual('La guerra es una locura extrema', res)

    def test_get_extension(self):
        self.assertEqual(u.get_extension('song.wav'), 'wav')

    def test_return_or_404(self):
        def raises():
            return [][0]

        with self.assertRaises(Http404):
            u.return_or_404(raises)

        def doesnt_raise():
            return ['woop'][0]

        self.assertEqual(u.return_or_404(doesnt_raise), 'woop')

    def test_normalize(self):
        result = u.normalize([1, -2, 4])
        self.assertListEqual(result, [0.25, -0.5, 1])

    def test_to_none(self):
        self.assertIsNone(u.to_none(None))
        self.assertIsNone(u.to_none({}))
        self.assertListEqual(u.to_none([]), [])
        self.assertIsNone(u.to_none('   '))
        self.assertEqual(u.to_none('string'), 'string')

    # def test_sort_entries(self):
    #     input_data = u.query("""
    #     SELECT *
    #     FROM poet_entity e
    #     JOIN poet_entity_to_work_rel r
    #     ON e.id = r.from_entity
    #     LIMIT 5
    #     """, [])
    #     result = u.sort_entities(input_data)
    #     self.assertEqual(len(result['composers']), 5)
    #     self.assertEqual(len(result['interpreters']), 0)
    #     self.assertEqual(len(result['others']), 0)

    def test_dashed_list(self):
        result = u.get_dashed_list(['a', 'b'], {'a': 'hi', 'b': 'hello', 'c': 'oh no'})
        self.assertEqual(result, 'hi - hello')
