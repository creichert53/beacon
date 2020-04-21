#!/bin/bash 

# Update Linux Distro and install dependencies
apt-get update
apt-get -y upgrade
apt-get -y install -y make build-essential libssl-dev zlib1g-dev \
  libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev \
  libncursesw5-dev xz-utils tk-dev libffi-dev liblzma-dev python-openssl \
  net-tools