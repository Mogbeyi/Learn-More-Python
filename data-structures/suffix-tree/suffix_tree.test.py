import unittest
from suffix_tree import SuffixTree

class TestSuffixTree(unittest.TestCase):

    suffix_tree = SuffixTree('abracadabra')

    def test_get_suffix_array(self):
        self.assertIn('abra', self.suffix_tree.get_suffix_array())

if __name__ == '__main__':
    unittest.main()
    
