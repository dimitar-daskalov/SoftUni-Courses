import re

count_barcodes_received = int(input())

pattern = r'(@[#]+)([A-Z][A-Za-z\d]{4,}[A-Z])(@[#]+)'

for count_barcode in range(count_barcodes_received):
    match = re.fullmatch(pattern, input())
    if match:
        product_group = ""
        for ch in match.group(2):
            if ch.isdigit():
                product_group += ch
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print(f"Invalid barcode")
