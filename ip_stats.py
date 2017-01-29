def get_ping_stats(ip_address, repeats):
	#Get the ping stats for a given IP address. These are returned via a raw string that will be parsed later on
	import subprocess
	import platform 

	os_result = platform.system()
	#print('Pinging ' + ip_address + '...')

	try:
		#Handle different ping formats for *nix based and windows systems
		if os_result == 'Linux' or os_result == 'Linux2' or os_result == 'Darwin':
			response = subprocess.check_output(
			['ping', '-c', str(repeats), ip_address],
			stderr=subprocess.STDOUT, # get all of the output
			universal_newlines=True # return string not bytes
			)

		else:
			output = subprocess.Popen(['ping', '-n', str(repeats), ip_address],
			stdout = subprocess.PIPE,
			stderr=subprocess.PIPE,
			universal_newlines=True
			)
			
			response = output.communicate()
			response = str(response)

		avg, stddev = parse_ping_str(response, os_result)

	except subprocess.CalledProcessError:
		print('Failed to contact the pool server: ' + ip_address)
		response = ''
		avg = 0
		stddev = 0

	return avg, stddev

def parse_ping_str(ip_response, os_result):
	import re

	if os_result == 'Linux' or os_result == 'Linux2' or os_result == 'Darwin':
		output_string = "(\d+\.\d+)\/(\d+\.\d+)\/(\d+\.\d+)\/(\d+\.\d+)\s+ms" #min/avg/max/mdev
		match = re.search(output_string, ip_response)

		if not(match is None):
			avg = float(match.group(2)) #avg is the 2nd index of the match group
			stddev = float(match.group(4)) #stddev is the fourth index of the match grou[]
		else:
			print('No values found!')
	else:
		output_string = 'Minimum = (\d+)+ms, Maximum = (\d+)+ms, Average = (\d+)+ms'
		match = re.search(output_string, ip_response)

		if not(match is None):
			avg = float(match.group(3)) #avg is the 3rd index of the match group
			stddev = 0 #Windows doesn't return the stddev, just pass this along as zero
		else:
			print('No ping stats found!')
			avg = 0
			stddev = 0

	return avg, stddev



