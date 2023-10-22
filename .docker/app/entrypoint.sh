#!/bin/bash

# Install any needed packages specified in requirements.txt
pip install --no-cache-dir -r requirements.txt

# Below command must be always run last
python app.py
