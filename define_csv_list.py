import csv

# Define the CSV file path
csv_file_path = "product_metaphor_list.csv"

# Create the CSV file and write the header
def initialize_csv(file_path):
    with open(file_path, mode='w', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['name', 'image_path', 'target','source',  'connection', 'mapping_strategy', 'sub_mapping_strategy']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        writer.writeheader()

# Initialize the CSV file
initialize_csv(csv_file_path)
print(f"Initialized {csv_file_path} with header")
