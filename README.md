### xmr-pool-choice 
Toolkit for helping to choose the right Monero minging pool based off of latency and decentralization of the network. Also, a json database containing the most recent accepted pool names, mining addresses, and live stats APIs are included.

### Requirements
- Python 3
- [tabulate](https://txt.arboreus.com/2013/03/13/pretty-print-tables-in-python.html) for seeing the results
- [requests](http://docs.python-requests.org/en/master/) for interacting with the pool APIs

Using pip these can be installed by the command:
```
	pip install tabulate requests
```


### Summary
This collection of python scripts scans the currently posted mining pools on [moneropools.com](http://moneropools.com/) and reports back some of the data a potential miner would be interested in such as latency and network hash rate percentage. I give a recommendation as the top pool for the miner based on a simple figure of merit which promotes decentralization of the network. This is defined as,

FOM = (Latency)^2 x (Network Hash %)

Thus, the lower the FOM, the better the pool choice. The latency squared favors local pools, or else small pools around the globe will be in your top list. I reject pools that do not respond to a ping or have a reported 0 hash rate.


### Usage
Currently there are no user supplied arguments, so you just have to open a terminal and run:
```
	python run.py
```

This will take a few minutes to run, depending on how responsive the pings and APIs are. The top 10 results will be shown in order, along with their relevant statsitics. All details are saved to pool_stats.txt so you don't have to run again if you close your terminal.

### Future features
- Choose pools from a certain region you would like to only choose from. The pool list storage should make this straightforward.
- Incorporate tabulate and requests into the code base so they don't need to be installed ahead of time.
- Create a script for sorting the results in other ways from the pool_results.txt file
- Create an executable for Windows users.
- Pool Up-time. Currently pools don't report their up-time through the API, and I belive only supportXMR.com has a measure of it. However, this is another extremely important metric a miner cares about when choosing their pool.
- Web scraper that automatically updates the pools posted to www.moneropools.com and gathers their API information


I'd like to thank the folk(s) at [moneropools.com](www.moneropools.com) and [supportXMR.com](www.supportXMR.com) for maintaing all of the pool information that made this possible. Please support them!

Donations:
```
XMR: 49P4SVT2DewdN44NKtySdf4d3LsYN4esS3VpC3eFUFrUWW3UDp76aaZbzijwmzso14C9ZhhAEtAiU3KTq27Tf4CfKbLA1Sx
```
