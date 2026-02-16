"""Tests for hostname_script module."""

import unittest
from unittest.mock import patch
import socket
import sys
import os

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'src'))

from hostname_script import get_hostname, main


class TestHostnameScript(unittest.TestCase):
    """Test cases for hostname_script."""

    def test_get_hostname_returns_string(self):
        """Test that get_hostname returns a string."""
        hostname = get_hostname()
        self.assertIsInstance(hostname, str)

    def test_get_hostname_not_empty(self):
        """Test that get_hostname returns a non-empty string."""
        hostname = get_hostname()
        self.assertGreater(len(hostname), 0)

    def test_get_hostname_matches_socket(self):
        """Test that get_hostname matches socket.gethostname()."""
        expected = socket.gethostname()
        actual = get_hostname()
        self.assertEqual(actual, expected)

    @patch('builtins.print')
    @patch('hostname_script.get_hostname')
    def test_main_prints_hostname(self, mock_get_hostname, mock_print):
        """Test that main prints the hostname correctly."""
        mock_get_hostname.return_value = "test-machine"
        main()
        mock_print.assert_called_once_with("Computer name: test-machine")

    @patch('builtins.print')
    def test_main_prints_actual_hostname(self, mock_print):
        """Test that main prints the actual hostname."""
        main()
        mock_print.assert_called_once()
        call_args = str(mock_print.call_args)
        self.assertIn("Computer name:", call_args)


if __name__ == '__main__':
    unittest.main()
