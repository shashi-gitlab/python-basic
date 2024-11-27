# iterate dictonary data type

product = {
    "name":"product1",
    "price":1000,
    "discounts":20,
    "size": ["xl","xxl"]
}

# for val in product: # in this val will print key only
#     print(val)


# for val in product.values(): # in this val will print valye only
#     print(val)

# for val in product.keys(): # in this val will print key only, this is second way to get key only
#     print(val)

for key, val in product.items(): # in this val will print key and value both
    print(key, val)