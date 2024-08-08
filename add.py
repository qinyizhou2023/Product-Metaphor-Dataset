import csv

# Define a images structure to hold product information
class ProductMetaphor:
    def __init__(self, name, image_path, source, target, link, mapping):
        self.name = name
        self.image_path = image_path
        self.source = source
        self.target = target
        self.link = link
        self.mapping = mapping

# Define the CSV file path
csv_file_path = "product_metaphor_list.csv"

# Append a new product metaphor to the CSV file
def append_to_csv(file_path, product_metaphor):
    with open(file_path, mode='a', newline='', encoding='utf-8') as csv_file:
        fieldnames = ['name', 'image_path', 'source', 'target', 'link', 'mapping']
        writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

        writer.writerow({
            'name': product_metaphor.name,
            'image_path': product_metaphor.image_path,
            'source': product_metaphor.source,
            'target': product_metaphor.target,
            'link': product_metaphor.link,
            'mapping': product_metaphor.mapping
        })

# Example new images entry
new_product_metaphor = ProductMetaphor(
    name="Firephant fire extinguisher",
    image_path="/mnt/images/e5e52971-6cd6-4f6e-87ec-2ae914a67910.png",
    source="elephant",
    target="fire extinguisher",
    link="Elephants are known to spray water out of their trunks in a skillful manner",
    mapping="The form of an elephant and the form of a fire extinguisher were merged into one coherent product by projecting the former onto the latter"
)

# Append the new entry to the CSV file
append_to_csv(csv_file_path, new_product_metaphor)
print(f"Appended new product metaphor to {csv_file_path}")
