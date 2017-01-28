#Script for running the xmr-pool-choice code base
import ip_stats
import json
import itertools
from tabulate import tabulate

#List of a few pool addresses to ping
ip_test = ['pool.supportxmr.com', 'pool.minexmr.com', 'minexmr.com'] # 'monerohash.com', 'pool.usxmrpool.com']

#Gather the pool data
with open('pool_list.json') as data_file:
	pool_data = json.load(data_file)

#Pull out the pool names and corresponding addresses from the json data
pool_names = []
pool_addresses = []
eur_dict = pool_data['Europe']
us_dict = pool_data['USA']
global_dict = pool_data['Global']
asia_dict = pool_data['Asia']

pool_names.append(eur_dict['Pool Names'])
pool_names.append(us_dict['Pool Names'])
pool_names.append(asia_dict['Pool Names'])
pool_names.append(global_dict['Pool Names'])
pool_addresses.append(eur_dict['Addresses'])
pool_addresses.append(us_dict['Addresses'])
pool_addresses.append(asia_dict['Addresses'])
pool_addresses.append(global_dict['Addresses'])

#Fix up the lists to be flat lists for easy parsing
pool_names = list(itertools.chain.from_iterable(pool_names))
pool_addresses = list(itertools.chain.from_iterable(pool_addresses))

#How many ping repeats, this must be >1 to get a standard deviation
repeats = 3

#Gather the average and standard deviation of the ping request, returns 0 if a connection couldn't be made
print('Gathering latency statistics...')
avg, stddev = zip(*(ip_stats.get_ping_stats(x, repeats) for x in pool_addresses))



print('Gathering Hash Rates...')
'''
Need to incorporate the api requesting from the pools themselves, listed on the moneropools.com website.
API calls are buried in the source code, I think I can pull out the addresses and commands and put it into,
the json data base
'''

print('Sorting...')
sorted_idx = sorted(range(len(avg)), key=lambda k: avg[k])

sorted_ips = [pool_names[x] for x in sorted_idx]
sorted_avg = [avg[x] for x in sorted_idx]
ii = 0
for x in sorted_avg:
	if x==0:
		sorted_avg.pop(ii)
		sorted_ips.pop(ii)
	ii=ii+1

'''
Failed pings (they report 0 latency so it should be straightforward to pop off the resulting list)
'''

print('The top 10 latency pools are listed below. \n' \
	  'The full results are written to the text file ip_result.txt \n' \
	  '-------------------------------------------------------------')

headers = ['Rank', 'Pool', 'Latency']
ii = 0
combined_list = []
for x in sorted_avg:
	combined_list.append([str(ii+1) + '.', sorted_ips[ii], '%.2f ms' % sorted_avg[ii]])
	ii = ii+1

with open('ip_result.txt', 'w') as text_file:
	text_file.write(tabulate(combined_list, headers))

print(tabulate(combined_list[0:10], headers))
