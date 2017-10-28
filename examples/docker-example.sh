#!/usr/bin/env bash

set -ex

# PREREQUISITE:
# 1. must Build the Dockerfile at the root of this project
# $ docker build -t basicauth-brute /path/to/BasicAuth-Brute/Dockerfile

# docker run instruction:
# "--rm" instructs docker to clean-up container after it stops
# "-v $PWD:/basicauth" mounts the current host directory in the container as "/basicauth" directory
# "basicauth-brute" is the name of the container
# "/basicauth/wordlist.txt" supplies the wordlist.txt file mounted inside the container under "/basicauth" path
# "http://google.com" is the URL required by BasicAuth-Brute.py
docker run --rm -v "${PWD}:/basicauth" basicauth-brute /basicauth/wordlist.txt http://google.com

