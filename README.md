### xmr-pool-choice 
Toolkit for helping to choose the right Monero minging pool based off of latency and decentralization of the network.

### Requirements
Python 3 \n
tabular \n
requests \n

Using pip these can be installed using:
```
	pip install tabular requests
```


### Summary
This collection of python scripts scans the currently posted mining pools on moneropools.com
and reports back the data a potential miner would be interested in. Latency and network hash
rate percentage. I give a recommendation as the top pool for the miner based on simple figure
of merit defined as
\n
FOM = (Latency)X(Network Hash %)
\n
Thus, the lower the FOM, the better the pool choice. I reject pools from this scoring that 
disconnect and have a 0 reported hash rate for obvious reasons.

Currently this only functi
The best pool is determined by taking into account a few quantities that are important for both the miner as well
as the Monero network as a whole. First and foremost, decentralization is favored, thus pools with lower hash rates are favored. 
Second in importance is the ping time, as I have found lower ping times lead to better stabilitity and longetivity of a miner staying connected. These two criteria are the first to be implemented, but I intend to add functionality for measuring the normalized variance in the pool hash rate (with the idea of avoiding pool hoppers) as well as analyzing the luck factor of the last N blocks. However, these will require some more work I haven't fully thought out.

### Usage:
Currently there are no user supplied arguments, so you just have to open a terminal and run:
```
	python run.py
```

The top 10 latency results, along with their hash rates will be displayed. The top two recommended
pools will also be displayed. All details are saved to ip_results.txt
