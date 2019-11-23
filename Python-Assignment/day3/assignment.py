'''class product:
    def __init__(o, name, cost, brand, rating, discount, category):
        o.name = name
        o.cost = cost
        o.brand = brand
        o.rating = rating
        o.discount = discount
        o.category = category
    d


obj = [product("AC", 27000, "LG", 4, 20, "Electronics"),
       product("Fridge", 4000, "LG", 5, 10, "Electronics"),
       product("WashingMachine", 5000, "Samsung", 4, 15, "Electronics"),
       product("HP202", 50000, "HP", 4, 15, "Laptops"),
       product( "Le202", 20000, "Lenovo", 5, 15, "Laptops")
       ]'''
class product:
    def __init__(o,n,p,d,r,c):
        o.name = n
        o.price = p
        o.discount=d
        o.rating=r
        o.category=c

li=[product("Fridge",6000,20,3,"electronic"),
 product("AC",24000,10,4,"electronic"),
 product("Vaccumm Cleaner",4000,15,2,"electronic"),
 product("TV",50000,5,3,"electronic"),
 product("Speaker",3500,20,3,"electronic")
]

for l in li:
    print(l.name,l.price,l.discount,l.rating,l.category)

dict={
    "1": ["rating", False],
    "2": ["rating", True],
    "3":["price", True],
    "4":["price", False]
}
choice= input("Enter 1 for")

li.sort(key= lambda el: getattr(el,dict[choice][0]), reverse=dict[choice][1])
for l in li:
    print(l.name,l.price,l.discount,l.rating,l.category)








