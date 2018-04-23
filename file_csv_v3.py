import csv

with open('names.csv', 'w', newline='') as csvfile:
    fieldnames = ['First Name', 'Last Name']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'First Name': 'Baked', 'Last Name': 'Beans'})
    writer.writerow({'First Name': 'Lovely', 'Last Name': 'Spam'})
    writer.writerow({'First Name': 'Wonderful', 'Last Name': 'Spam'})