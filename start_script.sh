#!/usr/bin/env bash

source activate pandas_postgres;
export FLASK_APP=src/app.py;
flask run;
