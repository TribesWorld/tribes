# tribes [![Build Status](https://travis-ci.org/TribesWorld/tribes.svg?branch=develop)](https://travis-ci.org/TribesWorld/tribes)

# Quick Start Guide

## Start through Flask

`pip install -r requirements`

`./run.sh` or `run.bat`

## Start through Docker

`docker build -t 'tribes' .`

`docker run -itd --restart always --name tribes -p 5000:5000 -e DEV_DATABASE_URL ${DEV_DATABASE_URL} tribes`

## Start through Docker-Compose

`docker-compose up`


2017年6月12日