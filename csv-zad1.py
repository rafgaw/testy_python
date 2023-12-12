import csv

fields = ['name', 'branch', 'year', 'cgpa']
row = ['Rafał', 'coe', '3', 9]

dict2 = dict(zip(fields, row))
print(dict2)

# dict_list = [
#
# ]

filename = 'records.csv'
# context manager
with open(filename, 'w', newline='') as csv_f:
    # csvwriter = csv.writer(csv_f)
    csvwriter = csv.DictWriter(csv_f, fieldnames=fields, delimiter=';')
    # csvwriter.writerow(row)
    csvwriter.writeheader()
    csvwriter.writerow(dict2)
