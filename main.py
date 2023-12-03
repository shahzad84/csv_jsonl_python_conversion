import csv
import json

# Read CSV file with UTF-8 encoding
with open('alpaca.csv', 'r', encoding='utf-8') as f:
    data = list(csv.reader(f))
    headers = data[0]
    data = data[1:]

# Convert CSV data to list of dictionaries
pairs = []
for row in data:
    pair = {}
    for i in range(len(headers)):
        pair[headers[i]] = row[i]
    pairs.append(pair)

# Export to JSON Lines (JSONL) file
with open('alpaca.jsonl', 'w', encoding='utf-8') as f:
    for pair in pairs:
        json.dump(pair, f, ensure_ascii=False)
        f.write('\n')  # Add a newline to separate JSON objects
