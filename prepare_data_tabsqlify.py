import json
import csv

# Define file paths
jsonl_file_path = 'datasets/wtq_test3.jsonl'
csv_file_path = 'outputs_C/normTab_targeted_wtq_june10_f.csv'
output_jsonl_file_path = 'datasets/normtab_tabsqlify_data_C.jsonl'

# Create a dictionary to map ids to norm_table from B.csv
id_to_norm_table = {}

# Read the CSV file and populate the dictionary
with open(csv_file_path, mode='r', encoding='utf-8') as csvfile:
    csv_reader = csv.DictReader(csvfile)
    for row in csv_reader:
        ids = row['id']
        norm_table = row['norm_table']
        id_to_norm_table[ids] = norm_table

# Open the output file in write mode
with open(output_jsonl_file_path, mode='w', encoding='utf-8') as output_file:
    # Read the JSONL file and augment each entry
    with open(jsonl_file_path, mode='r', encoding='utf-8') as jsonl_file:
        for line in jsonl_file:
            # Parse each JSON line
            data = json.loads(line)
            id = data['ids']

            # Check if there's a matching norm_table for the id
            if id in id_to_norm_table:
                # Add the norm_table attribute to the JSON object
                data['norm_table'] = id_to_norm_table[id]
            else:
                # If there's no match, you can decide what to do, e.g., set it to None
                data['norm_table'] = None

            # Write the augmented JSON object to the output file
            output_file.write(json.dumps(data) + '\n')

print(f'Merged data has been written to {output_jsonl_file_path}')
