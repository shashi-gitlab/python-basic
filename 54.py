product1 = {
    "name":"product1",
    "price":1000,
    "discounts":20,
    "size": ["xl","xxl"]
}

product2 = {
    "brand":"Adidas",
    "color":"green"
}

# product = product1 + product2 # this will give error beacuse this is not support + for concat
# print(product) 

product1.update(product2)
print(product1) 