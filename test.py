#hw2 Helena Rong
from hw2 import MediaCloud
import unittest

class TestMediaCloud(unittest.TestCase):

	def setUp(self):
		self.results = get_data()

	def test_MediaCLoudAPI(self):
		self.results.load()
		assert self.results is not None
		self.assertTrue len(self.results.all_lines) > 0



if __name__ == '__main__':
    unittest.main()
