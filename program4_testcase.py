import unittest


class TestSortArray(unittest.TestCase):
    def test_empty_array(self):
        self.assertEqual(sort_array([]), [])
    
    def test_sorted_array(self):
        self.assertEqual(sort_array([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])
    
    def test_reverse_sorted_array(self):
        self.assertEqual(sort_array([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])
    
    def test_duplicate_elements(self):
        self.assertEqual(sort_array([3, 2, 1, 2, 3]), [1, 2, 2, 3, 3])
    
    def test_large_array(self):
        arr = list(range(500))
        self.assertEqual(sort_array(arr), arr)
    
if __name__ == '__main__':
    unittest.main()
