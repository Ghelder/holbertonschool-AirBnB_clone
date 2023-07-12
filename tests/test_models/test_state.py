#!/usr/bin/python3
"""Module for testing the State class"""
import unittest
from models.state import State


class TestState(unittest.TestCase):
    """Test class for the State class."""

    def test_name_initialization(self):
        """Test case to check if the state name is initialized as an empty
        string."""
        state = State()
        self.assertEqual(state.name, "")

    def test_name_assignment(self):
        """Test case to check if the state name can be assigned correctly."""
        state = State()
        state.name = "New York"
        self.assertEqual(state.name, "New York")
