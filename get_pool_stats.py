import json
import requests
import itertools

#Make the HTTP request and parse data
def get_pool_data(address):

	#Handle the *one* case that decided not to conform to standards
	if address == 'https://api.nanopool.org/v1/xmr/pool/hashrate/':
		#The try except blocks are in case the pool api is down
		try:
			r = requests.get(address)
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
			r = requests.get(address)
			data = r.json()
			if address == 'https://xmr.suprnova.cc/index.php?page=api&action=public':
				hashrate = data['hashrate']
				miners = data['workers']
			else:
				hashrate = data['pool']['hashrate']
				miners = data['pool']['miners']
		except:
			#If the API request fails just set the hashrate and miners to 0, it will be handled elsewhere
			hashrate = 0
			miners = 0

	return hashrate, miners

#Grab the network hashrate from a fixed address
def get_network_hashrate():

	#Hard coded address to get the network hashrate from xmr.suprnova.cc -> it is the easiest to access from the api
	address = 'https://xmr.suprnova.cc/index.php?page=api&action=public'
	r = requests.get(address)
	data = r.json()

	network_hashrate = data['network_hashrate']

	return network_hashrate

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

