#!/bin/sh

curl -s $1 | grep href | cut -d= -f2 | cut -d'"' -f2;
