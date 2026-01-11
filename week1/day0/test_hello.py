"""Tests for Day 0"""

from hello import greet


def test_greet():
    """Test that greet returns the right message."""
    result = greet("World")
    assert result == "Hello, World!"


def test_greet_with_name():
    """Test with a different name."""
    result = greet("Python")
    assert result == "Hello, Python!"