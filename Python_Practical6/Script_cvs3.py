import argparse
import csv
import pandas as pd

parser = argparse.ArgumentParser(
    description="Reads a CSV file, prints its content and a statistical summary.",
)
parser.add_argument("Input_file", help="Define Input file", type=str)
#parser.add_argument("Output_file", help="Define Output file", type=str)
        
args = parser.parse_args()

print("\n📘 Reading CSV file using csv module:")
with open(args.Input_file, newline='') as csvfile:
    Matrix_read = csv.reader(csvfile, delimiter=',',)
    for row in Matrix_read:
        print(', '.join(row))

print("\n📗 Converting CSV file using pandas:")
df = pd.read_csv(args.Input_file, header=None) # No header in the file) 

print("Printing Statistical Summary:")
print(df.describe(include='all'))