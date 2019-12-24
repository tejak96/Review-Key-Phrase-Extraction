# coding=utf-8
import csv
import os
script_dir = os.path.dirname(__file__)
full_path = os.path.join(script_dir, '../dataset/data.csv')
reviews=[]

def get_data():
    with open(full_path, 'r') as csvFile:
        reader = csv.reader(csvFile)
        for row in reader:
            reviews.append(row[0])
        return reviews
