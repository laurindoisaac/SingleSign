# test_singlesignon.py
"""
Tests for SingleSignOn module.
"""

import unittest
from singlesignon import SingleSignOn

class TestSingleSignOn(unittest.TestCase):
    """Test cases for SingleSignOn class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = SingleSignOn()
        self.assertIsInstance(instance, SingleSignOn)
        
    def test_run_method(self):
        """Test the run method."""
        instance = SingleSignOn()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
