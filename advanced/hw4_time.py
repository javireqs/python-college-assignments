# This program demonstrates a generator yielding the number of accesses made in each hour, from the beginning of /etc/httpd/logs/access_


import re
from collections import defaultdict
from datetime import datetime

def parse_log(file_path):
    # Regular expression to extract the timestamp from log entries
    log_pattern = re.compile(r'\[(\d{2}/\w{3}/\d{4}:\d{2}:\d{2}:\d{2} [+-]\d{4})\]')
    accesses_per_hour = defaultdict(int)
    
    with open(file_path, 'r') as f:
        for line in f:
            match = log_pattern.search(line)
            if match:
                timestamp_str = match.group(1)
                timestamp = datetime.strptime(timestamp_str, '%d/%b/%Y:%H:%M:%S %z')
                # Format the timestamp to get YYYY-MM-DD HH
                hour_key = timestamp.strftime('%Y-%m-%d %H')
                accesses_per_hour[hour_key] += 1
                
                yield hour_key, accesses_per_hour[hour_key]

# Define the path to the access_log file
file_path = '/etc/httpd/logs/access_log'

for hour, accesses in parse_log(file_path):
    print(f'{hour}: {accesses} accesses')
