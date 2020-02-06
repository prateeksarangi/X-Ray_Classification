# X-Ray_Classification-CDAC

Dataset:- https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia/download

Training dataset on local system
*git clone https://github.com/prateeksarangi/X-Ray_Classification-CDAC/*

Before running program download the dataset from the link and place the **chest_xray** folder, containing **train**, **test** and **val** folders, inside **X-Ray_Classification-CDAC** folder.

*cd X-Ray_Classification-CDAC*

*pip install virtualenv*

*virtualenv env*

*python3 -m venv env*

*source env/bin/activate*

*pip install -r requirements.txt*

*python TunedNN.py*

Running the webapp backend program:-
*python ServerSide.py*

Running the webapp frontend program:-
*python exec.py*
