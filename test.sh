#!/bin/sh

module load python/3.7.0
python -m venv venv
. venv/bin/activate
pip install --upgrade pip setuptools
pip install locust

locust -f test.py --no-web -c 10 -r 1 --run-time 60m --host=http://osg-kansas-city-stashcache.nrp.internet2.edu:8000 --csv=example


