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

  Rank  Pool                        Latency    Fee                    Network %  Hash Rate      Miners
------  --------------------------  ---------  -------------------  -----------  -----------  --------
     1  xmrpool.net                 17.28 ms   Variable 0.4 - 6.5%        0.412  218.3 kH/s         40
     2  xmr.coolpool.io             32.24 ms   0.9 %                      0.022  11.6 kH/s          35
     3  mixpools.org - us           45.55 ms   0.5 %                      0.229  121.4 kH/s          6
     4  MoneroHash.com              48.12 ms   1.6 %                      1.829  970.0 kH/s        523
     5  monero.us.to                75.64 ms   1.0 %                      0.001  448.0 H/s           4
     6  xmr.nanopool.org - useast1  78.89 ms   1.0 %                      1.932  1.0 MH/s          184
     7  xmr.nanopool.org - uswest1  79.41 ms   1.0 %                      1.932  1.0 MH/s          184
     8  mineXMR.com                 90.89 ms   1.0 %                      4.787  2.5 MH/s         1128
     9  mixpools.org - eu           92.43 ms   0.5 %                      0.229  121.4 kH/s          6
    10  monero.crypto-pool.fr       99.11 ms   2.0 %                     18.024  9.6 MH/s          946
 ```

### Plans for recommendation
Looking to develop some metric that can be calculated from the data this script acquires. This could then provide a way to suggest top pools for a miner to join that is beneificial to the miner as well as the network decentralizaition.

### Future features
- Calculate average block per day to give a miner how many additions to their account they can expect
- Choose pools from a certain region you would like to only choose from. 
- Incorporate tabulate and requests into the code base so they don't need to be installed ahead of time.


This code relies on the data gathered by the folk(s) at [moneropools.com](http://moneropools.com) and [supportXMR.com](http://supportXMR.com) for maintaining all of the pool information. Check them out.

XMR Donations if you feel this was useful:
```
49P4SVT2DewdN44NKtySdf4d3LsYN4esS3VpC3eFUFrUWW3UDp76aaZbzijwmzso14C9ZhhAEtAiU3KTq27Tf4CfKbLA1Sx
```

Pool list updated:
January 31st, 2017
