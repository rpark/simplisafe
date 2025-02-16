#!/bin/bash

state="$1"

date
/usr/local/bin/python /home/simplisafe/scripts/simplisafe.py --state $state
