### xmr-pool-choice 
Toolkit for helping to choose the right Monero minging pool based off of latency and decentralization of the network. Also, a json database containing the most recent accepted pool names, mining addresses, and live stats APIs is included.

### Requirements
- Python 3
- [tabulate](https://txt.arboreus.com/2013/03/13/pretty-print-tables-in-python.html) for seeing the results
- [requests](http://docs.python-requests.org/en/master/) for interacting with the pool APIs

### Linux Usage
For a fresh Linux install, follow these commands to download the python3 packages required
```
	sudo apt install python3-pip
	pip3 install tabulate requests
	git clone https://github.com/timekelp/xmr-pool-choice
	cd /xmr-pool-choice
	python3 run.py
```

### Windows Usage
Download Python3, I prefer the [miniconda3](https://conda.io/miniconda.html) distrubtion from Anaconda. Download the Python 3.5 exe installer and follow the instructions. Download a copy of this repository to a location of your choice, then run
```
	cd "<repository-location>\xmr-pool-choice"
	conda install pip
	pip install requests tabulate
	python run.py
```

### OSX Usage
Download Python3 if you don't already have it, I prefer the [miniconda3](https://conda.io/miniconda.html) distrubtion from Anaconda. Download the Python 3.5 bash installer and follow the instructions. Download or git clone a copy of this repository to a location of your choice, then run
```
	cd <repository-location>\xmr-pool-choice
	conda install pip
	pip install requests tabulate
	python run.py
```
General note: it takes a few minutes to get the data from the network (I am not sure why the API calls take so long, it is an issue I am trying to work on) so please allow the script to run to completion. An example output (for an eastcoast based miner) would look like
```
The top 10 pools based on latency are listed below. 
It is recommended to chose a low latency, reliable, 
and small pool with <10 % Network Hashrate. 
The full results are written to the text file pool_results.txt 
```
  Rank  Pool                        Latency      Network %  Hash Rate      Miners
------  --------------------------  ---------  -----------  -----------  --------
     1  MoneroHash.com              24.12 ms         1.703  841.4 kH/s        485
     2  xmr.coolpool.io             34.10 ms         0.045  22.1 kH/s          33
     3  mixpools.org - us           44.72 ms         0.323  159.8 kH/s          7
     4  xmr.nanopool.org - useast1  79.21 ms         1.455  719.0 kH/s        124
     5  xmr.nanopool.org - uswest1  79.36 ms         1.455  719.0 kH/s        124
     6  monero.us.to                85.32 ms         0.001  683.0 H/s           6
     7  usxmrpool.com               87.21 ms         0.127  62.6 kH/s          34
     8  mineXMR.com                 93.58 ms         6.654  3.3 MH/s         1085
     9  mixpools.org - eu           101.93 ms        0.323  159.8 kH/s          7
    10  xmr.nanopool.org -eu2       103.27 ms        1.455  719.0 kH/s        124
 ```

### Detailed Summary
This collection of python scripts scans the currently posted mining pools on [moneropools.com](http://moneropools.com/) and reports back some of the data a potential miner would be interested in such as latency and network hash rate percentage. The top 10 pools based off of latency are displayed, along with some of their stats. I reject pools that do not respond to a ping or have a reported 0 hash rate.


This will take a few minutes to run, depending on how responsive the pings and APIs are. The top 10 results will be shown in order, along with their relevant statsitics. All details are saved to pool_stats.txt so you don't have to run again if you close your terminal.

### Future features
- Choose pools from a certain region you would like to only choose from. 
- Incorporate tabulate and requests into the code base so they don't need to be installed ahead of time.
- Create a script for sorting the results in other ways from the pool_results.txt file
- Create an executable for Windows users to alleviate need to download python 3.
- Pool Up-time. Currently pools don't report their up-time through the API, and I belive only supportXMR.com has a measure of it. However, this is another extremely important metric a miner cares about when choosing their pool.
- Web scraper that automatically updates the pools posted to www.moneropools.com and gathers their API information


I'd like to thank the folk(s) at [moneropools.com](www.moneropools.com) and [supportXMR.com](www.supportXMR.com) for maintaing all of the pool information that made this possible. Please support them!

XMR Donations:
```
49P4SVT2DewdN44NKtySdf4d3LsYN4esS3VpC3eFUFrUWW3UDp76aaZbzijwmzso14C9ZhhAEtAiU3KTq27Tf4CfKbLA1Sx
```
