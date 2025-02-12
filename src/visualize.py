#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
args = parser.parse_args()

# imports
import os
import json
from collections import Counter, defaultdict

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# print the count values
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
for k,v in items:
    print(k,':',v)

top_10 = items[:10]
# Now sort these top 10 items in ascending order (low to high)
top_10_sorted = sorted(top_10, key=lambda item: item[1])

# If there is no data, exit early.
if not top_10_sorted:
    print("No data to plot.")
    exit(1)

# Separate keys and values for plotting
keys, values = zip(*top_10_sorted)

# --- Plotting using matplotlib ---
import matplotlib.pyplot as plt

plt.figure(figsize=(10, 6))
plt.bar(keys, values, color='skyblue')
plt.xlabel(args.key)
plt.ylabel("Count")
plt.title(f"Top 10 {args.key} (sorted low to high)")
plt.xticks(rotation=45, ha='right')
plt.tight_layout()

print('got here')
# Construct an output filename based on the key and input filename.
# For example, if args.key is "#coronavirus" and the input file is "country.json",
# the output file will be "plot_coronavirus_country.json.png"
output_filename = f"plot_{args.key.strip('#')}_{os.path.basename(args.input_path)}.png"
plt.savefig(output_filename)
print(f"Plot saved as {output_filename}")
