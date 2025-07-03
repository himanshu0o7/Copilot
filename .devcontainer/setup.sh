#!/bin/bash
set -e

# System packages
if [ -f "packages.txt" ]; then
    sudo apt-get update && sudo apt-get upgrade -y
    sudo xargs apt-get install -y < packages.txt
fi

# Python packages
if [ -f "requirements.txt" ]; then
    pip3 install --user -r requirements.txt
fi

echo "✅ Packages installed and Requirements met"
