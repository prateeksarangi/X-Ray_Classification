pip install virtualenv
virtualenv env
source env/bin/activate

alias pip='pip3'
alias python='python3'

pip install -r requirements.txt
python TunedNN.py
