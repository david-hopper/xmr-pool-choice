#Script for running the xmr-pool-choice code base
import ip_stats
import get_pool_stats as gps
import json
import itertools
from tabulate import tabulate

#Gather the pool data
with open('pool_list.json') as data_file:
	pool_data = json.load(data_file)

#Pull out the pool names and corresponding addresses from the json data
pool_names = []
pool_addresses = []
pool_apis = []

eur_dict = pool_data['Europe']
us_dict = pool_data['USA']
global_dict = pool_data['Global']
asia_dict = pool_data['Asia']

#Pull out the 3 sections of pool information we will be using
pool_names.append(eur_dict['Pool Names'])
#pool_names.append(us_dict['Pool Names'])
#pool_names.append(asia_dict['Pool Names'])
#pool_names.append(global_dict['Pool Names'])

pool_addresses.append(eur_dict['Addresses'])
#pool_addresses.append(us_dict['Addresses'])
#pool_addresses.append(asia_dict['Addresses'])
#pool_addresses.append(global_dict['Addresses'])

pool_apis.append(eur_dict['API'])
#pool_apis.append(us_dict['API'])
#pool_apis.append(asia_dict['API'])
#pool_apis.append(global_dict['API'])

#Fix up the lists to be flat lists for easy parsing
pool_names = list(itertools.chain.from_iterable(pool_names))
pool_addresses = list(itertools.chain.from_iterable(pool_addresses))
pool_apis = list(itertools.chain.from_iterable(pool_apis))

#How many ping repeats, this must be >1 to get a standard deviation
repeats = 3

#Gather the average and standard deviation of the ping request, returns 0 if a connection couldn't be made
print('Gathering latency statistics. This can take some time..')
avg, stddev = zip(*(ip_stats.get_ping_stats(x, repeats) for x in pool_addresses))


print('Gathering Hash Rates. This can take some time...')
hashrate, miners = zip(*(gps.get_pool_data(x) for x in pool_apis))
network_hashrate = gps.get_network_hashrate()

print('Sorting...')
sorted_idx = sorted(range(len(avg)), key=lambda k: avg[k])

sorted_ips = [pool_names[x] for x in sorted_idx]
sorted_avg = [avg[x] for x in sorted_idx]
sorted_hashrate = [hashrate[x] for x in sorted_idx]
sorted_miners = [miners[x] for x in sorted_idx]
sorted_hash_percentage = [x/network_hashrate*100 for x in sorted_hashrate]

sorted_hashrate_str = [gps.readable_hashrate(x) for x in sorted_hashrate]
#failed pings report zero and are thus popped off the list
ii = 0
for x in sorted_avg:
	if x==0:
		sorted_avg.pop(ii)
		sorted_ips.pop(ii)
		sorted_hashrate.pop(ii)
		sorted_hashrate_str.pop(ii)
		sorted_miners.pop(ii)
		sorted_hash_percentage.pop(ii)
	ii=ii+1


print('The top 10 latency pools are listed below. \n' \
	  'The full results are written to the text file pool_results.txt \n' \
	  '-------------------------------------------------------------')

headers = ['Rank', 'Pool', 'Latency', 'Network %', 'Hash Rate', 'Miners']
ii = 0
combined_list = []
for x in sorted_avg:
	combined_list.append([str(ii+1) + '.', sorted_ips[ii], '%.2f ms' % sorted_avg[ii], '%.3f' % sorted_hash_percentage[ii], \
							sorted_hashrate_str[ii], '%d' % sorted_miners[ii]])
	ii = ii+1

with open('pool_results.txt', 'w') as text_file:
	text_file.write(tabulate(combined_list, headers))

print(tabulate(combined_list[0:10], headers))
