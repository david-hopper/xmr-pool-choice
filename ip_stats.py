def get_ping_stats(ip_address, repeats):
	#Get the ping stats for a given IP address. These are returned via a raw string that will be parsed later on
	import subprocess
	#print('Pinging ' + ip_address + '...')

	try:
		response = subprocess.check_output(
		['ping', '-c', str(repeats), ip_address],
		stderr=subprocess.STDOUT, # get all of the output
		universal_newlines=True # return string not bytes
		)

		#Immediately convert to numbers as the text is not that useful
		avg, stddev = parse_ping_str(response)
		
		#print('Average %.2f ms' % avg )
		

	except subprocess.CalledProcessError:
		print('Failed to contact the pool server:' + ip_address)
		response = ''
		avg = 0
		stddev = 0

	return avg, stddev

def parse_ping_str(ip_response):
	import re

	output_string = "(\d+\.\d+)\/(\d+\.\d+)\/(\d+\.\d+)\s+ms"
	match = re.search(output_string, ip_response)

	if not(match is None):
		avg = float(match.group(1)) #avg is the first index of the match group
		stddev = float(match.group(3)) #stddev is the third index of the match grou[]
	else:
		print('No values found!')

	return avg, stddev



