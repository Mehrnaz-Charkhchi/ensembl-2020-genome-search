import app
import unittest
import json
from urllib.parse import urlparse

class MyTestCase(unittest.TestCase):

    def setUp(self):
        app.app.testing = True
        self.app = app.app.test_client()
        self.base_url = '/api/popular_genomes/'


    def test_if_popular_genomes_works(self):

        print("\n\t*** Testing if popular genomes endpoint works ***")

        response = self.app.get(self.base_url)

        print('\t*** Request: {} ***'.format(self.base_url))

        self.assertEqual(response.status_code, 200)

        print("\t*** Response code: {} ***".format(response.status_code))


    def test_if_there_is_atleast_one_popular_genome(self):

        print("\n\t*** Testing if there is at least one popular genome ***")

        response = self.app.get(self.base_url)

        print('\t*** Request: {} ***'.format(self.base_url))

        self.assertEqual(response.status_code, 200)

        response_data =json.loads(response.data)

        self.assertGreater(len(response_data['popular_species']), 1)

        print("\t*** Response code: {} ***".format(response.status_code))





if __name__ == '__main__':
    unittest.main()