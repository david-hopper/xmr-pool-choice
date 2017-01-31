import json

'''
I would like to make this an automated web scraper, but I figure
the pool list won't change that often so for now I can manually
update it.
This was taken from moneropools.com on 1/31/2017, 8:00 EST. I
did not include pools running at a reported 0 hash rate, or others
that were flagged as potential scams
'''

#Group the addresses into continents to reflect the moneropools.com organizational structure
us_pool_names = ['MoneroHash.com', 'xmr.coolpool.io',
				'monero.us.to','usxmrpool.com']

us_addresses = ['monerohash.com', 'xmr.coolpool.io',
				'monero.us.to', 'pool.usxmrpool.com']

us_api = ['https://monerohash.com/api/stats', 'http://66.23.241.140:8118/stats',
		  'http://monero.us.to:8117/stats', 'https://usxmrpool.com:8119/stats']

us_fees = [.016, 0.009, .01, .004]

us_dict = {'Pool Names' : us_pool_names, 'Addresses' : us_addresses, 'API' : us_api,
			'Fees' : us_fees}

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

eur_api = ['http://supportxmr.com:8117/stats', 'http://xmrpool.eu:8117/stats',
			'http://mro.poolto.be:8117/stats', 'http://api.minexmr.com:8080/stats',
			'http://xmr.prohash.net:8117/stats', 'http://sheepman.mine.bz:8117/stats',
			'http://api.moneropool.com/live_stats', 'https://monero.crypto-pool.fr:8091/stats',
			'http://pool.miners.pro:8117/stats']

eur_fees = [.005, .01, .01, .01, .01, 0, .019, .02, .007]

eur_dict = {'Pool Names' : eur_pool_names, 'Addresses' : eur_addresses, 'API' : eur_api,
			'Fees' : eur_fees}

asia_pool_names = ['alimabi.cn', 'pooldd.com']

asia_addresses = ['139.129.107.21', 'xmr.pooldd.com'] #I think alimabi.cn pool address is correct?

asia_api = ['http://xmrapi.alimabi.cn:80/stats', 'http://api.pooldd.com:8080/stats']

asia_fees = [.007, .02]

asia_dict = {'Pool Names' : asia_pool_names, 'Addresses' : asia_addresses, 'API' : asia_api,
			'Fees' : asia_fees}

global_pool_names = ['xmr.suprnova.cc', 'xmrpool.net', 
						'xmr.nanopool.org - eu1', 'xmr.nanopool.org -eu2',
						'xmr.nanopool.org - useast1', 'xmr.nanopool.org - uswest1',
						'xmr.nanopool.org - asia1', 'mixpools.org - eu', 'mixpools.org - us']

global_addresses = ['xmr.suprnova.cc', 'mine.xmrpool.net',
						'xmr-eu1.nanopool.org', 'xmr-eu2.nanopool.org',
						'xmr-us-east1.nanopool.org', 'xmr-us-west1.nanopool.org',
						'xmr-asia1.nanopool.org',
						'xmr.mixpools.org', 'xmr-us.mixpools.org']

global_api = ['https://xmr.suprnova.cc/index.php?page=api&action=public', 'https://api.xmrpool.net/pool/stats',
				'https://api.nanopool.org/v1/xmr/pool/hashrate/', 'https://api.nanopool.org/v1/xmr/pool/hashrate/',
				'https://api.nanopool.org/v1/xmr/pool/hashrate/', 'https://api.nanopool.org/v1/xmr/pool/hashrate/', 
				'https://api.nanopool.org/v1/xmr/pool/hashrate/', 'https://mixpools.org:8117/stats',
				'https://mixpools.org:8117/stats']

global_fees = ['Optional!', 'Variable 0.4 - 6.5%', .01, .01, .01, .01, .01, .005, .005 ]

global_dict = {'Pool Names' : global_pool_names, 'Addresses' : global_addresses, 'API' : global_api,
			'Fees' : global_fees}


master_pool_list = {'USA' : us_dict, 'Europe' : eur_dict, 
					'Global' : global_dict, 'Asia' : asia_dict}


with open('pool_list.json', 'w') as f:
	json.dump(master_pool_list, f, indent = 4)
