#!/bin/bash

# Install any needed packages specified in requirements.txt
pip install --no-cache-dir -r requirements.txt

# Below command must be always last in this file.
# This keeps containers running.
tail -f /dev/null
