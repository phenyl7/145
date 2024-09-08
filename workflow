name: Run script every hour

on:
  schedule:
    - cron: '0 * * * *'  # Runs every hour

jobs:
  build:
    runs-on: ubuntu-latest
    
    steps:
    - name: Checkout code
      uses: actions/checkout@v3
    
    - name: Set up Python
      uses: actions/setup-python@v3
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install yfinance matplotlib pandas
    
    - name: Run script
      run: python your_script.py
