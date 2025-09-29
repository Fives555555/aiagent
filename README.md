# AI Agent

An AI Agent to assist with coding and debugging.

AI Agent was a guided project from [Boot.dev](https://www.boot.dev).

## Environment

Requires Python 3.10+. 

Virtual environment created with [uv](https://github.com/astral-sh/uv).

## Usage

Inside the AI Agent directory, activate the virtual environment:

```console
source .venv/bin/activate
```

Then run the main Python file along with your prompt:

```console
uv run main.py "fix the bug in the calculator app"
```

## Restrictions

The agent is restricted to the calculator directory to prevent any unwanted actions being performed.

If the agent needs access to other directories, change the [functions/config.py](functions/config.py) working directory variable.
