#!/bin/bash

python server/manage.py runserver & cd client && yarn start && fg
