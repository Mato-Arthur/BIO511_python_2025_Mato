#!/usr/bin/env python3
import csv
import sys
import argparse
#rows = 5
#cols = 5

data = [
    [1, 6, 7, 8, 15],
    [3, 4, 5, 6, 16],
    [8, 9, 10, 11, 17],
    [12, 13, 14, 15, 18],
    [20, 21, 22, 23, 24]
]

# Generate a 5x5 matrix automatically
#data = [[f"R{r+1}C{c+1}" for c in range(cols)] for r in range(rows)]

with open('matrix.csv', 'w', newline='') as file2:
    writer = csv.writer(file2)
    writer.writerows(data)

if len(sys.argv) > 1:
    user_input = sys.argv[1]
    with open('matrix.csv', 'a', newline='') as file2:
        file2.write(f"\n{user_input}\n")  # Append the argument as a comment at the end of the file
else:
    print("No user_input argument provided.")


