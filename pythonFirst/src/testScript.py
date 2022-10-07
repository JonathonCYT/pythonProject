dict_json = {"alien_0" : {'color': 'green', 'points': 5},
             "alien_1" : {'color': 'yellow', 'points': 10},
             "alien_2" : {'color': 'red', 'points': 15},
             "alien_3" : {'color' : 'black', 'points':20}}

for k in dict_json.keys():
    print(k)

print("-----------")
for v in dict_json.values():
    print(v)

print("-----------")
for k,v in dict_json.items():
    print(f"{k} : {v}")    
    for k1,v1 in v.items():
        print(f"{k1} : {v1}")
    print("--------------")    
