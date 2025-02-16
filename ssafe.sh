#!/bin/bash

state="$1"

date
/usr/local/bin/python /home/simplisafe/simplisafe-python-dev/simplisafe.py --state $state
