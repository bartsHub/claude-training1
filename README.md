# Hello World

A small Python script that asks for your name and greets you.

## Requirements

- Python 3.6 or newer (no third-party packages)

## Usage

```sh
python3 main.py
```

Type your name at the prompt and press Enter:

```
Enter your name: Mike
Hello, Mike!
```

If you leave the name blank (or press Ctrl-D), it prints `Hello, world!`.

You can also use the function from other Python code:

```python
from main import hello_world

hello_world("Mike")  # prints "Hello, Mike!"
hello_world()        # prints "Hello, world!"
```

## Running the tests

The tests use Python's built-in `unittest` module:

```sh
python3 -m unittest -v
```

To run them from another directory, use `python3 -m unittest discover -s <path-to-repo>`.

## Project layout

| File           | Purpose                                         |
| -------------- | ----------------------------------------------- |
| `main.py`      | `hello_world(name)` and the interactive prompt  |
| `test_main.py` | Unit tests for `hello_world` and the prompt     |
