import json

'''
I would like to make this an automated web scraper, but I figure
the pool list won't change that often so for now I can manually
update it.
This was taken from moneropools.com on 1/25/2017, 22:37 EST. I
did not include pools running at a reported 0 hash rate, or others
that were flagged as potential scams
'''

#Group the addresses into continents to reflect the moneropools.com organizational structure
us_pool_names = ['MoneroHash.com', 'xmr.coolpool.io',
				'pariah.io', 'monero.us.to',
				'usxmrpool.com']

us_addresses = ['monerohash.com', 'xmr.coolpool.io',
				'pariah.io', 'monero.us.to',
				'pool.usxmrpool.com']
us_dict = {'Pool Names' : us_pool_names, 'Addresses' : us_addresses}

eur_pool_names = ['supportXMR.com', 'xmrpool.eu',
					'xmr.poolto.be', 'mineXMR.com',
					'xmr.prohash.net', 'sheepman.mine.bz',
					'moneropool.com', 'monero.crypto-pool.fr',
					'monero.miners.pro']

eur_addresses = ['pool.supportxmr.com', 'xmrpool.eu',
					'poolto.be', 'pool.minexmr.com',
					'xmr.prohash.net', 'sheepman.mine.bz',
					'mine.moneropool.com', 'xmr.crypto-pool.fr',
					'pool.miners.pro']
eur_dict = {'Pool Names' : eur_pool_names, 'Addresses' : eur_addresses}

global_pool_names = ['xmr.suprnova.cc', 'xmrpool.net', 
						'xmr.nanopool.org - eu1', 'xmr.nanopool.org -eu2',
						'xmr.nanopool.org - useast1', 'xmr.nanopool.org - uswest1',
						'xmr.nanopool.org - asia1', 'mixpools.org - eu', 'mixpools.org - us']

global_addresses = ['xmr.suprnova.cc', 'mine.xmrpool.net',
						'xmr-eu1.nanopool.org', 'xmr-eu2.nanopool.org',
						'xmr-us-east1.nanopool.org', 'xmr-us-west1.nanopool.org',
						'xmr-asia1.nanopool.org',
						'xmr.mixpools.org', 'xmr-us.mixpools.org']
global_dict = {'Pool Names' : global_pool_names, 'Addresses' : global_addresses}

asia_pool_names = ['alimabi.cn', 'pooldd.com']

asia_addresses = ['139.129.107.21', 'xmr.pooldd.com'] #I think alimabi.cn pool address is correct?
asia_dict = {'Pool Names' : asia_pool_names, 'Addresses' : asia_addresses}

master_pool_list = {'USA' : us_dict, 'Europe' : eur_dict, 
					'Global' : global_dict, 'Asia' : asia_dict}


with open('pool_list.json', 'w') as f:
	json.dump(master_pool_list, f, indent = 4)
