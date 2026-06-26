# app.py
def add(a, b):
    return a + b
    # test_app.py
from app import add

def test_add():
    assert add(2, 3) == 5
    git init
git add .
git commit -m "Initial commit with app and test"
git branch -M main
git remote add origin <your-repo-url>
git push -u origin main
name: CI Pipeline
on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  build-and-test:
    runs-on: ubuntu-latest

    steps:
    - name: Checkout code
      uses: actions/checkout@v3

    - name: Set up Python
      uses: actions/setup-python@v4
      with:
        python-version: '3.10'

    - name: Install dependencies
      run: |
        pip install pytest

    - name: Run tests
      run: |
        pytest
        git add .
git commit -m "Add CI pipeline"
git push
