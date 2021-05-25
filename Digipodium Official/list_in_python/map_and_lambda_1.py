cir = lambda r: 2 * r * 3.14

data= [3,3.42,5.56,67,78,89,89,2.3,12,23,1.2,32,9.42]

results = []

# normal
for radius in data:
    out = cir(radius)
    results.append(out)
print(results)

# comprehension
results = [cir(radius) for radius in data]
print(results)

# map function -> a func or lambda expression is always required
results = list(map(cir,data))
print(results)