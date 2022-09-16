inventory =[
{'brand': 'ford', 'model': 'mustang', 'year': '1970'},
{'brand': 'toyota', 'model': 'tundra', 'year': '2022'},
{'brand': 'toyota', 'model': 'corola', 'year': '2020'},
{'brand': 'mitsubishi', 'model': 'outlander', 'year': '2021'},
{'brand': 'ford', 'model': 'mustang', 'year': '1970'},
{'brand': 'toyota', 'model': 'tundra', 'year': '2022'},
{'brand': 'toyota', 'model': 'tundra', 'year': '2021'},
{'brand': 'toyota', 'model': 'tundra', 'year': '2020'},
{'brand': 'ford', 'model': 'mustang', 'year': '2019'},
{'brand': 'ford', 'model': 'mustang', 'year': '2020'},
{'brand': 'mitsubishi', 'model': 'mirage', 'year': '2019'},
{'brand': 'honda', 'model': 'accord', 'year': '2019'},
{'brand': 'honda', 'model': 'accord', 'year': '2019'},
{'brand': 'honda', 'model': 'accord', 'year': '2020'},
{'brand': 'honda', 'model': 'accord', 'year': '2022'},
{'brand': 'ford', 'model': 'mustang', 'year': '2018'},
{'brand': 'ford', 'model': 'maverick', 'year': '2020'},
{'brand': 'ford', 'model': 'maverick', 'year': '2006'}]

count = 0

print("-------------\nGET THE AMOUNT OF CARS BY DESCRIPTION IN YOUR DATABASE:\n-------------\n")
brand_user = input("What brand are you looking for? ").strip().lower()
model_user = input("\nWhat model are you looking for? ").strip().lower()
year1 = int(input("\nStarting from which build year? ").strip().lower())
year2 = int(input("\nUp to which build year? ").strip().lower())


year_counter = year1
year_count = [year1] 
while year_counter < year2:
    year_counter += 1
    year_count.append(year_counter)

for cars in inventory:
    if cars['brand'] == brand_user:
        if cars['model'] == model_user:
            if int(cars['year']) in year_count:
                count += 1
                

if count == 0: 
    print(f"-----\nThere are no cars that fit the description. \nDid you mistype anything?\n")
if count == 1:
    print(f"----- \nThere is {count} car available.")
if count > 2:
    print(f"----- \nThere are {count} cars available.")
