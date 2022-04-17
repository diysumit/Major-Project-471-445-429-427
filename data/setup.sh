#!/bin/bash
#!/usr/bin/env bash

spacer="==============================================================================================="

# installing puppet
sudo bash ./puppet_install.sh

# running manifest
puppet apply -v manifest.pp

# creating virtual environment and activating
if [ -d "./venv" ]; then
    source venv/bin/activate
else
    virtualenv venv
    source venv/bin/activate
fi

# installing python dependencies
pip install pandas
pip install matplotlib
pip install requests
pip freeze > requirements.txt
pip install -r requirements.txt


##################################################################################################################
#                                               OLD DATA FROM KAGGLE 
##################################################################################################################
# setting up kaggle-api
# $(wget -O kaggle.json "https://drive.google.com/uc?export=download&id=14kD-I5mmHLYG_DNXfzbn_851o8j8nD8W")
# $(mkdir -p .kaggle)
# $(mv kaggle.json ./.kaggle/)
# $(sudo chmod 600 ./.kaggle/kaggle.json)
# $(rsync -a ./.kaggle/ ~/ )

# checks if dataset is present, if not download it and unzip it in all_currencies folder
# if [ -f "./392-crypto-currency-pairs-at-minute-resolution.zip" ]; then
#     echo $spacer
#     echo "Skipping file download"
#     echo "Using cached file: ./392-crypto-currency-pairs-at-minute-resolution.zip"
#     #checks if all_currencies folder is present, if not create it
#     $(mkdir -p all_currencies)
#     echo $spacer
#     $(unzip 392-crypto-currency-pairs-at-minute-resolution.zip -d ./all_currencies)
# else
#     echo $spacer
#     #downloading datasets from kaggle
#     $(kaggle datasets download tencars/392-crypto-currency-pairs-at-minute-resolution)
#     #checks if all_currencies folder is present, if not create it
#     $(mkdir -p all_currencies)
#     echo $spacer
#     $(unzip 392-crypto-currency-pairs-at-minute-resolution.zip -d ./all_currencies)
# fi

# copying necessary datasets(btc-usd and eth-usd) in unprocessed_data folder
# creating folder unprocessed_data if not present
# $(mkdir -p unprocessed_data)
# $(cp ./all_currencies/btcusd.csv ./unprocessed_data/)
# $(cp ./all_currencies/ethusd.csv ./unprocessed_data/)
###################################################################################################################


# creating folder unprocessed_data if not present
$(mkdir -p unprocessed_data)

# writing csv files in unprocessed folder using data from coinapi
# running download_update_csv.py
echo $spacer
./download_update_csv.py

# making folder for processed_data
$(mkdir -p processed_data)

echo $spacer

# keep this at second last position
deactivate
