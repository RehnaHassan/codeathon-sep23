import unittest
from copilot_test import is_valid_ip_address

class TestIsValidIPAddress(unittest.TestCase):
    def test_valid_ip_address(self):
        self.assertTrue(is_valid_ip_address("192.168.0.1"))
    
    def test_invalid_ip_address(self):
        self.assertFalse(is_valid_ip_address("555.555.555.555"))
    
    def test_missing_component(self):
        self.assertFalse(is_valid_ip_address("192.168.0"))
    
    def test_extra_component(self):
        self.assertFalse(is_valid_ip_address("192.168.0.1.1"))
    
    def test_non_numeric_component(self):
        self.assertFalse(is_valid_ip_address("192.168.0.a"))
    
if __name__ == '__main__':
    unittest.main()
