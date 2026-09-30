import io
import os
import runpy
import sys
import unittest
from contextlib import redirect_stdout
from unittest.mock import patch

HERE = os.path.dirname(os.path.abspath(__file__))
MAIN_PATH = os.path.join(HERE, "main.py")
sys.path.insert(0, HERE)

from main import hello_world  # noqa: E402


def run_main(input_mock):
    out = io.StringIO()
    with patch("builtins.input", input_mock), redirect_stdout(out):
        runpy.run_path(MAIN_PATH, run_name="__main__")
    return out.getvalue()


class TestHelloWorld(unittest.TestCase):
    def test_greets_given_name(self):
        out = io.StringIO()
        with redirect_stdout(out):
            hello_world("Mike")
        self.assertEqual(out.getvalue(), "Hello, Mike!\n")

    def test_defaults_to_world(self):
        out = io.StringIO()
        with redirect_stdout(out):
            hello_world()
        self.assertEqual(out.getvalue(), "Hello, world!\n")


class TestMain(unittest.TestCase):
    def test_prompts_for_name_and_greets(self):
        mock_input = unittest.mock.Mock(return_value="Ada")
        self.assertEqual(run_main(mock_input), "Hello, Ada!\n")
        mock_input.assert_called_once_with("Enter your name: ")

    def test_strips_whitespace(self):
        self.assertEqual(run_main(unittest.mock.Mock(return_value="  Ada  ")), "Hello, Ada!\n")

    def test_empty_name_falls_back_to_world(self):
        self.assertEqual(run_main(unittest.mock.Mock(return_value="   ")), "Hello, world!\n")

    def test_eof_falls_back_to_world(self):
        self.assertEqual(run_main(unittest.mock.Mock(side_effect=EOFError)), "\nHello, world!\n")


if __name__ == "__main__":
    unittest.main()
