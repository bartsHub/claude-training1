# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Overview

A minimal Python script: `main.py` prompts for a name and prints a greeting via `hello_world(name="world")`. Standard library only — no dependencies, no build or lint tooling. Local git repo with no remote.

## Commands

```sh
python3 main.py                      # interactive; pipe input to run non-interactively: echo "Mike" | python3 main.py
python3 -m unittest -v               # all tests (from repo root)
python3 -m unittest test_main.TestMain.test_eof_falls_back_to_world   # single test
python3 -m unittest discover -s <path-to-repo>                         # from another directory
```

## Behavior to preserve

- `hello_world()` with no argument must keep printing `Hello, world!` (the default exists for backward compatibility).
- In the `__main__` block, input is `.strip()`ed; blank input or `EOFError` (Ctrl-D, `< /dev/null`) falls back to `"world"`. On EOF an extra newline is printed so the greeting doesn't share the prompt's line.

## Testing notes

- `test_main.py` exercises the `__main__` block by running `main.py` via `runpy.run_path` with `builtins.input` patched. It resolves `main.py` and adds the repo dir to `sys.path` relative to `__file__`, so tests work from any working directory — keep it that way if files move.
- Tests assert exact stdout, including trailing newlines.
