#!/bin/bash 

# Install pyenv
if [ -d "/home/$(whoami)/.pyenv" ]
then
  echo "It looks like .penv is already installed in the /home/{user}/.pyenv directory. If you'd like reinstall, simply delete this directory."
else
  git clone https://github.com/pyenv/pyenv.git ~/.pyenv
  echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
  echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc
  echo -e 'if command -v pyenv 1>/dev/null 2>&1; then\n  eval "$(pyenv init -)"\nfi' >> ~/.bashrc
  exec $SHELL
fi

pyenv install 3.7.5
pyenv global 3.7.5
pip install pipenv

cd "/home/$(whoami)/beacon"
pipenv install