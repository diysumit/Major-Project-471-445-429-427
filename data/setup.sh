#!/bin/bash
#!/usr/bin/env bash

spacer="==============================================================================================="

# installing puppet
sudo bash ./puppet_install.sh

# running manifest
puppet apply -v manifest.pp

# installing python dependencies
pip freeze > requirements.txt
pip install -r requirements.txt

# setting up kaggle-api
$(wget -O kaggle.json "https://drive.google.com/uc?export=download&id=14kD-I5mmHLYG_DNXfzbn_851o8j8nD8W")
$(mkdir -p .kaggle)
$(mv kaggle.json ./.kaggle/)
$(sudo chmod 600 ./.kaggle/kaggle.json)
$(rsync -a ./.kaggle/ ~/ )

# checks if dataset is present, if not download it and unzip it in all_currencies folder
if [ -f "./392-crypto-currency-pairs-at-minute-resolution.zip" ]; then
    echo $spacer
    echo "Skipping file download"
    echo "Using cached file: ./392-crypto-currency-pairs-at-minute-resolution.zip"
    #checks if all_currencies folder is present, if not create it
    $(mkdir -p all_currencies)
    echo $spacer
    $(unzip 392-crypto-currency-pairs-at-minute-resolution.zip -d ./all_currencies)
else
    echo $spacer
    #downloading datasets from kaggle
    $(kaggle datasets download tencars/392-crypto-currency-pairs-at-minute-resolution)
    #checks if all_currencies folder is present, if not create it
    $(mkdir -p all_currencies)
    echo $spacer
    $(unzip 392-crypto-currency-pairs-at-minute-resolution.zip -d ./all_currencies)
fi

# copying necessary datasets(btc-usd and eth-usd) in unprocessed_data folder
# creating folder unprocessed_data if not present
$(mkdir -p unprocessed_data)
$(cp ./all_currencies/btcusd.csv ./unprocessed_data/)
$(cp ./all_currencies/ethusd.csv ./unprocessed_data/)

# making folder for processed_data
$(mkdir -p processed_data)

echo $spacer

# process_data.py
./process_data.py update