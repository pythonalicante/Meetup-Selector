#!/bin/bash
set -e
pipenv lock -r > requirements.txt
