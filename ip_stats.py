def get_ping_stats(ip_addresses, repeats):
	#Get the ping stats for a given IP address. These are returned via a raw string that will be parsed later on
	import subprocess
	import platform 

	#Grab os to make the right ping call
	os_result = platform.system()

	#Find the number of ips looping over and initiate the progress bar
	num_ips = len(ip_addresses)
	i = 0
	printProgressBar(i, num_ips, prefix = 'Progress', suffix = 'Complete', length = 40, fill = '█')

	avg_list = []
	stddev_list = []

	for ip in ip_addresses:
		try:
			#Handle different ping formats for *nix based and windows systems
			if os_result == 'Linux' or os_result == 'Linux2' or os_result == 'Darwin':
				response = subprocess.check_output(
				['ping', '-c', str(repeats), ip],
				stderr=subprocess.STDOUT, # get all of the output
				universal_newlines=True # return string not bytes
				)

			else:
				output = subprocess.Popen(['ping', '-n', str(repeats), ip],
				stdout = subprocess.PIPE,
				stderr=subprocess.PIPE,
				universal_newlines=True
				)
				
				response = output.communicate()
				response = str(response)

			avg, stddev = parse_ping_str(response, os_result)

		except subprocess.CalledProcessError:
			print('Failed to contact the pool server: ' + ip)
			response = ''
			avg = 0
			stddev = 0

		#iterate and save the results	
		avg_list.append(avg)
		stddev_list.append(stddev)
		i += 1
		printProgressBar(i, num_ips, prefix = 'Progress', suffix = 'Complete', length = 40, fill = '█')

	return avg_list, stddev_list

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



