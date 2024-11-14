product = {
    "name":"product1",
    "price":1000,
    "discounts":20,
    "size": ["xl","xxl"]
}

print(product)

product['discounts'] = 20
product['brand'] = "puma"
del product["name"]

print(product)
