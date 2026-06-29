This repo contains code for a program that will show my local Bus and Train arrivals/departures on a LED Matrix driven by a raspberry pi 5.

# Hardware

This code is designed to run on a raspberry pi 5, attached via it's GPIO pins to the Hub75 connector on a waveshare 96*48 LED Matrix Display.

Documentation for the LED matrix can be found here: https://docs.waveshare.com/RGB-Matrix-Px-96x48/Raspberry-Pi

# How to run

To run the code first install [uv by astral](https://docs.astral.sh/uv/). This is used for python installation, dependancy management and virtual environment creation.

Next, if this is your first time running this program, acquire a Darwin SOAP Api key and create a .env file in `huxley2/Huxley2` with the contents:

```bash
ACCESS_TOKEN=<darwin-access-token>
```

Then start the huxley 2 docker container by running:

```bash
cd huxley2/Huxley2
docker compose up -d
```

Finally run the following from the project root:

```bash
uv run main.py
```

This will install the python version specified in [.python-version](.python-version), create a virtual environment in `.venv` using this version, and run `main.py` from this venv.

> for better LED matrix performance run the script as root:
>
> ```bash
> # Required if you haven't setup the project venv before
> uv sync
>
> # Run main.py as root by referencing uv's venv manually
> sudo .venv/bin/python main.py
> ```

# Project Structure

- The root of this repo is a python project whose entrypoint is [main.py](./main.py).
- The python package that allows scripts to control the LED Matrix is found in the [rgbmatrix](./rgbmatrix/) directory.
- The code for the huxley 2 national rail departure board SOAP API Proxy is found in the [huxley2](./huxley2/) directory.
