import csv 

fields=['first','second','third']
print(fields)

fields.append('vic')
'''
with open(r'name', 'a') as f:
    writer = csv.writer(f)
    writer.writerow(fields)
'''
print(fields)