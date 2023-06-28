import re

raw_log_file = '/Users/suchitbaniya/Desktop/system/raw_log.txt'

with open(raw_log_file,'r') as file:
    for line in file:
        
        match = re.match(r'(.*?)\s(\d+\.\d+\.\d+\.\d+)',line)
        if match:
            host = match.group(1)
            ip_address = match.group(2)

            
            ip_parts = ip_address.split('.')
            ip_address_reverse = '.'.join(ip_parts[::-1])
            ip_file_name = '.'.join(ip_parts[:-1])
            ip_write_here = '-'.join(ip_parts)

            file_name1 = f'FILE.{ip_file_name}'
            file_name2 = f'{ip_write_here}-write-here'

            
            with open(file_name1, 'w') as file1:
                file1.write(f'{ip_parts[-1]}\tIN\tRecord\t{host.strip()}-{ip_address_reverse}.subisu.net.np\n')

            with open(file_name2, 'w') as file2:
                file2.write(f'{host}\t\tZ\t{ip_address}\n')
