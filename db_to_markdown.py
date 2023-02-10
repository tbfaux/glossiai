import csv

with open('db/query.csv', 'r') as file:
    reader = csv.DictReader(file)
    products = {}
    # Iterate over each row in the CSV file
    for i, row in enumerate(reader):
        products[row['product_id']] = dict((k, row[k]) for k in ['product_title', 'product_description', 'brand_name']
           if k in row)
        # Save the current row to its own text file
        with open(f"md/review_{row['guid']}.txt", 'w') as row_file:
            row_file.write(f"{row['username']} reviews {row['product_title']} by {row['brand_name']}: {row['transcription']}")

    for id, product in products.items():
        with open(f"md/product_{id}.txt", 'w') as row_file:
            row_file.write(f"{product['product_title']} by {product['brand_name']}: {product['product_description']}")