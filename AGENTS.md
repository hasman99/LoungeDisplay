## Running the project

When asked to run the project first ensure the huxley docker container is up and running by checking `docker ps`.

If it is not navigate to `huxley2/Huxley2` and run `docker compose up -d`.

Finally run `uv run main.py` from the project root.

## Code conventions

- Python files are expected to pass pyrefly type check with strict preset, so all function parameters must be typed.
- We use `ruff` to lint and format python files. See below for instructions on how to do this.

## Python Change Validation

After making any changes to python files, run the following commands/checks:

1) Format python files with `uv run ruff format`.

2) Sort python imports with `uv run ruff check --select I --fix`

3) Lint python files with `uv run ruff check`. Fix any returned errors.

4) Typecheck python files with `uv run pyrefly check`. Fix any returned errors.

## Project Structure

- The root of this repo is a python project whose entrypoint is [main.py](./main.py). Project configuration is found in [pyproject.toml](./pyproject.toml).
- The python package that allows scripts to control the LED Matrix is found in the [rgbmatrix](./rgbmatrix/) directory. This is a C++ library wrapped in a python wrapper found in `rgbmatrix/bindings/python/rgbmatrix`.
- The rgbmatrix package also includes multiple examples of scripts utilising the rgbmatrix package to control an LED matrix in `rgbmatrix/bindings/python/samples`. Inspect these to see how to control the LED matrix.
- The code for the huxley 2 national rail departure board SOAP API Proxy is found in the [huxley2](./huxley2/) directory.
