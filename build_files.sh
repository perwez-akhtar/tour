#!/bin/bash

# Ensure Python 3.12.0 is installed
if ! command -v python3.12.0 &> /dev/null
then
    echo "Python 3.12.0 is not installed. Please install it."
    exit 1
fi

# Activate virtual environment if needed
# source /path/to/your/virtual/environment/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run any additional build steps
# python3.12.0 setup.py build

# Run Django migrations
python3.12.0 manage.py migrate

# Collect static files
python3.12.0 manage.py collectstatic --noinput

# Run tests (if applicable)
# python3.12.0 manage.py test

# Any other build steps...

echo "Build completed successfully."
