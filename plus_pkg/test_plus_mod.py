# the tests for plus_mod.py

import unittest
import plus_mod

class TestPlus(unittest.TestCase):
	def setUp(self):
		pass

	def test_4_plus_5(self):
		self.assertEqual( plus_mod.Plus(4,5), 9)

	def test_4_plus_5_plus_6(self):
		self.assertEqual( plus_mod.PlusPlus(4,5,6), 15)

if __name__ == "__main__":
	unittest.main()
