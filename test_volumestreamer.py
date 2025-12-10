# test_volumestreamer.py
"""
Tests for VolumeStreamer module.
"""

import unittest
from volumestreamer import VolumeStreamer

class TestVolumeStreamer(unittest.TestCase):
    """Test cases for VolumeStreamer class."""
    
    def test_initialization(self):
        """Test class initialization."""
        instance = VolumeStreamer()
        self.assertIsInstance(instance, VolumeStreamer)
        
    def test_run_method(self):
        """Test the run method."""
        instance = VolumeStreamer()
        self.assertTrue(instance.run())

if __name__ == "__main__":
    unittest.main()
