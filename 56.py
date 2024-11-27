product1 = {
    "name": "Shirt",
    "price":1000,
    "price":2000,
    "discount":20,
    "size":["XL","XXL"]
}

# product1.clear()
# print(product1)

# print( product1.get("discount") )
# print( product1.keys() )
# print( product1.values() )
# product1.pop('discount')  # delete element by key name
# print( product1)
# product1.popitem() #delete for last item
# print( product1)

product2 = product1.copy()
product2['discount'] =100
print( product2)
print( product1)