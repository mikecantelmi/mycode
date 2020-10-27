import csv

with open('myfile.csv', 'r') as csvfile:
    credz = csv.reader(csvfile, delimiter=',')

print(credz[])

