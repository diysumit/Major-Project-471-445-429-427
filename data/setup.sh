#!/bin/bash
#!/usr/bin/env bash

spacer="==============================================================================================="

#* installing puppet
sudo bash ./puppet_install.sh

#* running manifest
puppet apply -v manifest.pp

#* creating virtual environment and activating
if [ -d "./venv" ]; then
    source venv/bin/activate
else
    virtualenv venv
    source venv/bin/activate
fi

#* installing python dependencies
pip install pandas
pip install matplotlib
pip install requests
pip install apache_beam
pip freeze > requirements.txt
pip install -r requirements.txt

#* creating folders unprocessed_data and processed_data if not present
$(mkdir -p unprocessed_data)
$(mkdir -p processed_data)

#* downloading raw data
#* running pipeline.py
echo $spacer
$(./pipeline.py --input_path=./unprocessed_data/ --output_path=./processed_data/)
echo $spacer

#* running predict_data.py
$(./predict_data.py)

#* keep this at second last position
deactivate