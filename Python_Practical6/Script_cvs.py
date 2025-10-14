#!/usr/bin/env python3

import csv
import sys
import argparse

parser = argparse.ArgumentParser(
    description="Process some integers.", 
    prog, 
    usage, 
    )
parser.add_argument('--course', help='Course code')
parser.add_argument('--year', help='Year of the course')
args = parser.parse_args()
print(f'Course: {args.course} from HT {args.year}')

data = [
    ["Name", "Age", "City"],
    ["Alice", 25, "Berlin"],
    ["Bob", 30, "Munich"]]

with open('data.csv', 'w', newline='') as file1: #name of the file, mode (read = r , write = w, append = a) 
    writer = csv.writer(file1) #creates a csv writer object
    file1.write('Name, Age, City\n') #writes the header of the csv file
    writer.writerows(data) #writes the data to the csv file

    
    


