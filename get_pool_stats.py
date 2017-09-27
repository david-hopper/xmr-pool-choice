import json
import requests
import itertools

#Make the HTTP request and parse data
def get_pool_data(address_list, snipa_format):
	
	#Find the number of ips looping over and initiate the progress bar
	num_pools = len(address_list)
	i = 0
	printProgressBar(i, num_pools, prefix = 'Progress', suffix = 'Complete', length = 40, fill = '█')

	hashrate_list = []
	miners_list = []
	for address in address_list:
		#Handle the *one* case that decided not to conform to standards
		if address == 'https://api.nanopool.org/v1/xmr/pool/hashrate/':
			#The try except blocks are in case the pool api is down
			try:
				r = requests.get(address, timeout = 9)
				data = r.json()
				hashrate = data['data']

				r = requests.get('https://api.nanopool.org/v1/xmr/pool/activeminers/')
				data = r.json()
				miners = data['data']
			except:
				#If the API request fails just set the hashrate and miners to 0, it will be handled elsewhere
				hashrate = 0
				miners = 0
		else:
			try:
				r = requests.get(address, timeout = 9)
				data = r.json()

				#Handle the special use cases of new pools altering the API format (this isn't pretty)
				if address == 'https://xmr.suprnova.cc/index.php?page=api&action=public':
					hashrate = data['hashrate']
					miners = data['workers']
				elif address in snipa_format:
					hashrate = data['pool_statistics']['hashRate']
					miners = data['pool_statistics']['miners']
				else:
					hashrate = data['pool']['hashrate']
					miners = data['pool']['miners']
			except:
				#If the API request fails just set the hashrate and miners to 0, it will be handled elsewhere
				hashrate = 0
				miners = 0

		#Update and iterate
		hashrate_list.append(float(hashrate))
		miners_list.append(float(miners))
		i += 1
		printProgressBar(i, num_pools, prefix = 'Progress', suffix = 'Complete', length = 40, fill = '█')

	return hashrate_list, miners_list

#Grab the network hashrate from a fixed address
def get_network_hashrate():

	#Hard coded address to get the network hashrate from xmr.suprnova.cc -> it is the easiest to access from the api
	address = 'https://xmr.suprnova.cc/index.php?page=api&action=public'
	r = requests.get(address, timeout = 9)
	data = r.json()

	network_hashrate = data['network_hashrate']

	return float(network_hashrate)

#Convert the raw H/s to something more easily viewable in terms of H/s, kH/s, MH/s etc
def readable_hashrate(hashrate):
	units = ['H/s', 'kH/s', 'MH/s', 'GH/s', 'TH/s']

	#Handle a 0 hash rate as a N/A, parse the others
	if hashrate == 0:
		converted_hashrate = 'N/A'
	else:
		ii = 0
		while hashrate > 1000:
			hashrate = hashrate/1000
			ii = ii + 1

		converted_hashrate = '%.1f ' % hashrate + units[ii]

	return converted_hashrate

#Convert the fee number to a percent, if 'Unknown' or 'Variable' leave alone
def readable_fee(fee):
	import re

	match = re.search('(Unknown|Variable|Optional|Adjustable)', str(fee))

	if not(match is None):
		str_fee = str(fee)
	else:
		fee = float(fee)*100
		str_fee = '%.1f %%' % fee

	return str_fee

# Print iterations progress
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█'):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = '\r')
    # Print New Line on Complete
    if iteration == total: 
        print()

