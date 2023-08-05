# bbbmon

A small python based CLI utility to monitor BigBlueButton-Usage. 

## Installation

The easiest way to install bbbmon is to install it from the Python Package Index (PyPi). This project uses [python poetry](https://python-poetry.org/) for dependency management, so you could also run it without installing the package system wide, see instructions below.

## Install with pip3

```bash
sudo pip3 install bbbmon --upgrade
```

Then run with:

```bash
bbbmon
```

## Run with poetry (without pip)

Clone the repo:

```bash
git clone https://code.hfbk.net/bbb/bbbmon.git
```

Make sure you have poetry installed. Install instruction for poetry can be [found here](https://python-poetry.org/docs/#installation).
From inside the project directory run:

```bash
poetry install
```

Run bbbmon with:

```bash
poetry run bbbmon
```

For bbbmon to run you need to have a `bbbmon.properties` file at the path specified. In this file there should be your servers secret and the server URL. You can find this secret on your server in the file `/usr/share/bbb-web/WEB-INF/classes/bigbluebutton.properties` (look for a line starting with `securitySalt=` and copy it to). If in doubt just follow the instructions the CLI gives you.

