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
pool_fees = []

regions = ['Global', 'Europe', 'USA', 'Asia']

[pool_names.append(pool_data[x]['Pool Names']) for x in regions]
[pool_addresses.append(pool_data[x]['Addresses']) for x in regions]
[pool_apis.append(pool_data[x]['API']) for x in regions]
[pool_fees.append(pool_data[x]['Fees']) for x in regions]

#Flatten lists for easy parsing
pool_names = list(itertools.chain.from_iterable(pool_names))
pool_addresses = list(itertools.chain.from_iterable(pool_addresses))
pool_apis = list(itertools.chain.from_iterable(pool_apis))
pool_fees = list(itertools.chain.from_iterable(pool_fees))

#How many ping repeats, this must be >1 to get a standard deviation
repeats = 5

#Gather the average and standard deviation of the ping request, returns 0 if a connection couldn't be made
print('Gathering latency statistics...')
avg, stddev = zip(*(ip_stats.get_ping_stats(x, repeats) for x in pool_addresses))


print('Gathering pool stats (hash rates, miners, network hashrate) ...')
hashrate, miners = zip(*(gps.get_pool_data(x) for x in pool_apis))
network_hashrate = gps.get_network_hashrate()
hashrate_percentage = [x/network_hashrate*100 for x in hashrate]

#Convert tuples to lists for popping
avg = list(avg)
hashrate = list(hashrate)
miners = list(miners)

#failed pings and hashrates report zero and are thus popped off the list
ii = 0
for x, y in zip(avg, hashrate_percentage) :
	if x == 0 or y == 0:
		avg.pop(ii)
		pool_names.pop(ii)
		pool_fees.pop(ii)
		hashrate.pop(ii)
		miners.pop(ii)
		hashrate_percentage.pop(ii)
	ii=ii+1

#Sort the results based on latency, prepare for output to console and text file
print('Sorting...')
sorted_idx = sorted(range(len(avg)), key=lambda k: avg[k])

sorted_ips = [pool_names[x] for x in sorted_idx]
sorted_avg = [avg[x] for x in sorted_idx]
sorted_hashrate = [hashrate[x] for x in sorted_idx]
sorted_miners = [miners[x] for x in sorted_idx]
sorted_hash_percentage = [hashrate_percentage[x] for x in sorted_idx]
sorted_fees = [pool_fees[x] for x in sorted_idx]

sorted_hashrate_str = [gps.readable_hashrate(x) for x in sorted_hashrate]
sorted_fees_str = [gps.readable_fee(x) for x in sorted_fees]

print('The top 10 pools based on latency are listed below. \n' \
	  'It is recommended to choose a low latency, reliable, \n' \
	  'and small pool with <10 % Network Hashrate. \n' \
	  'The full results are written to the text file pool_results.txt \n')

headers = ['Rank', 'Pool', 'Latency', 'Fee', 'Network %', 'Hash Rate', 'Miners']
ii = 0
combined_list = []
for x in sorted_avg:
	combined_list.append([str(ii+1) + '.', sorted_ips[ii], '%.2f ms' % sorted_avg[ii], sorted_fees_str[ii],
						 '%.3f' % sorted_hash_percentage[ii], sorted_hashrate_str[ii], '%d' % sorted_miners[ii]])
	ii = ii+1

with open('pool_results.txt', 'w') as text_file:
	text_file.write(tabulate(combined_list, headers))

print(tabulate(combined_list[0:10], headers))
