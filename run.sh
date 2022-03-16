#!/bin/sh

# start the container stack
# (assumes the caller has permission to do this)
docker-compose up -d

# open the browser window
open http://localhost:8000