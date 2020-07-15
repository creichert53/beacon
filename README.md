Clone the project to the `/srv` directory in the raspberry pi

# Set Up Pyenv and Poetry

## Install Python

```bash
# Install Dependencies

cd ~
sudo apt install -y build-essential tk-dev libncurses5-dev \
  libncursesw5-dev libreadline6-dev libdb5.3-dev libgdbm-dev \
  libsqlite3-dev libssl-dev libbz2-dev libexpat1-dev liblzma-dev \
  zlib1g-dev libffi-dev tar wget vim
```

```bash
# Install Pyenv

curl -L https://github.com/pyenv/pyenv-installer/raw/master/bin/pyenv-installer | bash
echo 'export PATH="/home/$(whoami)/.pyenv/bin:$PATH"' >> ~/.bashrc
echo "$(pyenv init -)" >> ~/.bashrc
echo "$(pyenv virtualenv-init -)" >> ~/.bashrc
source ~/.bashrc
```

```bash
# Install Python 3.8 with Pyenv

pyenv install 3.8.3
pyenv global 3.8.3
pyenv version
```

## Install Poetry

```bash
# Simple Installation

curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python3
source $HOME/.poetry/env
poetry --version
```

```bash
# Install Python Dependencies

cd ~/srv/beacon
poetry install
```

```bash
# Run Poetry environment

poetry shell
```