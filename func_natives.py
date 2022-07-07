from functools import reduce
#map
def multiply_by_2(item):
    return item * 2

li = [6, 4, 3 , 7, 10, 5]

print('Map : ', list(map(multiply_by_2, li)))


#filter
def pair(item):
    return item % 2 == 0

print('Filter : ', list(filter(pair, li)))

# Combine Map/Filter
print('Combine Map/Filter : ', list(map(multiply_by_2,filter(pair, li))))

#zip
model = ['id', 'name', 'age']
person1 = [1, 'serge', 53]
person2 = [2, 'aline', 57]

print(dict(zip(model, person1)))
# print(list(zip(model, person1, person2)))

#reduce
panier = [
    {
        "product": "vin",
        "price": 12,
        "quant": 6,
},{
        "product": "huitres",
        "price": 7,
        "quant": 12,
},{
        "product": "beure",
        "price": 3,
        "quant": 1,
}
]
def fn(acc, current):
     acc+= current['price'] * current['quant']
     return acc

total = reduce(fn,panier, 0)
print('Reduce : ', total)

def fn2(acc, item):
    acc[item['product']] = item['price'] * item['quant']
    return acc

detail = reduce(fn2, panier, dict())
print(detail)    
