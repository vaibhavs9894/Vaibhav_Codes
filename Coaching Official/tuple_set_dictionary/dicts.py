emp = {
    'name':'Raj verma',
    'designation':'Assistant level 3',
    'salary':{
        'basic':12000,
        'da':10000,
        'hra':4000,
        'misc':10000
    },
    'dept':'Account',
    'doj':{
        'year':2000,
        'month':4,
        'day':23
    },
}

print(emp)
print(emp['name'])
print(emp['salary']['hra'])
print(emp['dept'])
print(emp['doj']['year'])

stockprices = dict(google=235, facebook=211.23, netflix=200.1)
print('another dictionary')
print(stockprices)

## add a value
print('adding  a value')

stockprices['disney'] = 250.23
print(stockprices)

emp['phone'] = '928382381'
print(emp)

## update a value
print('updating  a value')

stockprices['facebook'] = 180.23
print(stockprices)

emp['dept'] = 'Sales'
print(emp)