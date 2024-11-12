import csv

log_file = './na-server/access.log'
csv_file = './na-server/access.csv'
    
# Define the field names for the CSV file
field_names = ['IP', 'Timestamp', 'Method', 'URL', 'Status', 'Size', 'User-Agent']

# Open the log file for reading and the CSV file for writing
with open(log_file, 'r') as file:
    with open(csv_file, 'w', newline='') as csv_file:
        writer = csv.DictWriter(csv_file, fieldnames=field_names)

        # Write the header row to the CSV file
        writer.writeheader()

        # Read each line from the log file and write it to the CSV file
        for line in file:
            # Split the line into individual fields
            fields = line.split()

            # Extract the relevant information from the fields
            ip = fields[0]
            timestamp = fields[3][1:] + ' ' + fields[4][:-1]
            method = fields[5][1:]
            url = fields[6]
            status = fields[8]
            size = fields[9]
            user_agent = ' '.join(fields[11:])

            # Write the extracted information to the CSV file
            writer.writerow({
                'IP': ip,
                'Timestamp': timestamp,
                'Method': method,
                'URL': url,
                'Status': status,
                'Size': size,
                'User-Agent': user_agent
            })

print('Conversion complete.')