#!/usr/bin/python3
""" """
import os
import models
from console import HBNBCommand
import unittest
from io import StringIO
from unittest.mock import patch

class test_console(unittest.TestCase):
    """ """
    def test_emptyline(self):
     """Test empty line input."""
     with patch("sys.stdout", new=StringIO()) as f:
        self.HBNB.onecmd("\n")
        self.assertEqual("", f.getvalue())

    def test_quit(self):
       """Test quit command"""
       with patch("sys.stdout", new=StringIO()) as f:
          self.HBNB.onecmd("quit")
          self.assertEqual("", f.getvalue())
    
if __name__ == "__main__":
    unittest.main()