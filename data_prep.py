import pandas as pd
import numpy as np

df = pd.read_csv('./data/ABBREV.csv')

# Convert the "Name" column to uppercase
df['Shrt_Desc'] = df['Shrt_Desc'].str.upper()
df = df.sort_values(by='Shrt_Desc', ascending=True)

# Write the modified data back to the CSV file
df.to_csv('./data/ABBREV.csv', index=False)

df['Total_Fat_(g)'] = df['FA_Mono_(g)'] + df['FA_Sat_(g)']
df = df[["NDB_No", "Shrt_Desc", "Energ_Kcal", "Protein_(g)", "Carbohydrt_(g)", "Fiber_TD_(g)", "Sugar_Tot_(g)", "Calcium_(mg)", "Sodium_(mg)", "Total_Fat_(g)"]].copy()
df = df.rename(columns={'Energ_Kcal':'Calories',  'Shrt_Desc':'Name', 'NDB_No':'id', 'Carbohydrt_(g)':'Carbs_(g)', 'Protein_(g)':'Protein_(g)', 'Fiber_TD_(g)':'Fiber_(g)', 'Sugar_Tot_(g)':'Sugar_(g)', 'Calcium_(mg)':'Calcium_(mg)', 'Sodium_(mg)':'Sodium_(mg)'})

cheese = df[df["Name"].str.startswith("CHEESE,")]
cheese = cheese.sort_values(by='Calories', ascending=False)
#cheese.to_csv('./data/cheese.csv')

milk = df[df["Name"].str.startswith("MILK,")]
milk = milk.sort_values(by='Calories', ascending=False)
#milk.to_csv('./data/milks.csv')

soup_keywords = ['SOUP', 'CAMPBELL', 'SOUP', 'CHILI']
soup_pattern = '|'.join(soup_keywords)

not_soup = ['BROTH', 'BOUILLON', 'STOCK','GRAVY', 'MIX', 'ON THE GO', 'JUC', 'CRACKERS', 'SPAGHETTI']
not_soup_pattern = '|'.join(not_soup)

soup = df[df["Name"].str.contains(soup_pattern)]
soup = soup[~soup["Name"].str.contains(not_soup_pattern)]

soup = soup.sort_values(by='Calories', ascending=False)
#soup.to_csv('./data/soups.csv')

cereal_keywords = ['CEREAL']
cereal_pattern = '|'.join(cereal_keywords)

cereal = df[df["Name"].str.contains(cereal_pattern)]

cereal = cereal.sort_values(by='Calories', ascending=False)
#cereal.to_csv('./data/cereals.csv')

cookies_keywords = ['COOKIE', 'WAFER']
cookies_pattern = '|'.join(cookies_keywords)

not_cookies = ['ICE CRM']
not_cookies_pattern = '|'.join(not_cookies)

cookies = df[df["Name"].str.contains(cookies_pattern)]
cookies = cookies[~cookies["Name"].str.contains(not_cookies_pattern)]

cookies = cookies.sort_values(by='Calories', ascending=False)
#cookies.to_csv('./data/cookies.csv')


babyfood_keywords = ['BABYFOOD', 'INF FORMULA']
babyfood_pattern = '|'.join(babyfood_keywords)

babyfood = df[df["Name"].str.contains(babyfood_pattern)]

babyfood = babyfood.sort_values(by='Calories', ascending=False)
#babyfood.to_csv('./data/babyfoods.csv')

beans_keywords = ['BEANS']
beans_pattern = '|'.join(beans_keywords)

not_beans = ['CANDIES']
not_beans_pattern = '|'.join(not_beans)

beans = df[df["Name"].str.contains(beans_pattern)]
beans = beans[~beans["Name"].str.contains(not_beans_pattern)]

beans = beans.sort_values(by='Calories', ascending=False)
#beans.to_csv('./data/beans.csv')

rice_keywords = ['RICE,']
rice_pattern = '|'.join(rice_keywords)

not_rice = ['CEREAL', 'CRACKERS', 'NOODLES', 'BABYFOOD', 'SOUP']
not_rice_pattern = '|'.join(not_rice)

rice = df[df["Name"].str.contains(rice_pattern)]
rice = rice[~rice["Name"].str.contains(not_rice_pattern)]

rice = rice.sort_values(by='Calories', ascending=False)
#rice.to_csv('./data/rices.csv')


ice_cream_keywords = ['ICE_CREAM', 'ICE CREAM', 'ICECREAM', 'ICE CRM']
ice_cream_pattern = '|'.join(ice_cream_keywords)

not_ice_cream = ['POP-TART', 'COATING', 'CUP']
not_ice_cream_pattern = '|'.join(not_ice_cream)

ice_cream = df[df["Name"].str.contains(ice_cream_pattern)]
ice_cream = ice_cream[~ice_cream["Name"].str.contains(not_ice_cream_pattern)]

ice_cream = ice_cream.sort_values(by='Calories', ascending=False)
#ice_cream.to_csv('./data/ice_creams.csv')

chips_keywords = ['CHIPS']
chips_pattern = '|'.join(chips_keywords)

chips = df[df["Name"].str.contains(chips_pattern)]

chips = chips.sort_values(by='Calories', ascending=False)
#chips.to_csv('./data/chips.csv')

pasta_keywords = ['PASTA', 'SPAGHETTI', 'MACARONI']
pasta_pattern = '|'.join(pasta_keywords)

pasta = df[df["Name"].str.contains(pasta_pattern)]

pasta = pasta.sort_values(by='Calories', ascending=False)
#pasta.to_csv('./data/pasta.csv')

fast_food_keywords = ['FASTFOOD', 'FAST FOOD', 'FAST FD', 'SUBWAY', 'MCDONALD', "WENDY'S", 'BURGER KING', "DOMINO'S", 'PIZZA HUT', 'KFC', 'POPEYE', 'DIGIORNO', "ARBY'S", 'CHICK-FIL-A', "CAESAR'S"]
fast_food_pattern = '|'.join(fast_food_keywords)

fast_food = df[df["Name"].str.contains(fast_food_pattern)]

fast_food = fast_food.sort_values(by='Calories', ascending=False)
#fast_food.to_csv('./data/fast_foods.csv')

pizza_keywords = ['PIZZA']
pizza_pattern = '|'.join(pizza_keywords)

not_pizza = ['CRACKER', 'BREADSTICK']
not_pizza_pattern = '|'.join(not_pizza)

pizza = df[df["Name"].str.contains(pizza_pattern)]
pizza = pizza[~pizza["Name"].str.contains(not_pizza_pattern)]

pizza = pizza.sort_values(by='Calories', ascending=False)
#pizza.to_csv('./data/pizzas.csv')

school_lunch_keywords = ['SCHOOL']
school_lunch_pattern = '|'.join(school_lunch_keywords)

school_lunch = df[df["Name"].str.contains(school_lunch_pattern)]

school_lunch = school_lunch.sort_values(by='Calories', ascending=False)
#school_lunch.to_csv('./data/school_lunches.csv')

beef_keywords = ['BEEF,', 'BF,']
beef_pattern = '|'.join(beef_keywords)

not_beef = ['SOUP']
not_beef_pattern = '|'.join(not_beef)

beef = df[df["Name"].str.contains(beef_pattern)]
beef = beef[~beef["Name"].str.contains(not_beef_pattern)]

beef = beef.sort_values(by='Calories', ascending=False)
#beef.to_csv('./data/beef.csv')

bread_keywords = ['BREAD,']
bread_pattern = '|'.join(bread_keywords)

not_bread = ['SOUP', 'SHORTENING', 'COOKIE', 'PIE', 'CAKE', 'FRIED', 'CRUMBS', 'MIX']
not_bread_pattern = '|'.join(not_bread)

bread = df[df["Name"].str.contains(bread_pattern)]
bread = bread[~bread["Name"].str.contains(not_bread_pattern)]

bread = bread.sort_values(by='Calories', ascending=False)
#bread.to_csv('./data/breads.csv')

fish_keywords = ['FISH', 'COD', 'FRESHWATER', 'SALTWATER', 'BASS', 'CAVIAR', 'EEL', 'GROUPER', 'HADDOCK', 'HERRING', 'MACKEREL', 'PERCH', 'MULLET', 'TUNA', 'POMPANO',  'SALMON', 'SHARK', 'TROUT']
fish_pattern = '|'.join(fish_keywords)

not_fish = ['CRACKERS']
not_fish_pattern = '|'.join(not_fish)

fish = df[df["Name"].str.contains(fish_pattern)]
fish = fish[~fish["Name"].str.contains(not_fish_pattern)]

fish = fish.sort_values(by='Calories', ascending=False)
#fish.to_csv('./data/fish.csv')

candy_keywords = ['CANDY', 'CANDIES']
candy_pattern = '|'.join(candy_keywords)

candy = df[df["Name"].str.contains(candy_pattern)]

candy = candy.sort_values(by='Calories', ascending=False)
#candy.to_csv('./data/candy.csv')

beverage_keywords = ['BEVERAGE', 'BEV,']
beverage_pattern = '|'.join(beverage_keywords)

beverage = df[df["Name"].str.contains(beverage_pattern)]

beverage = beverage.sort_values(by='Calories', ascending=False)
#beverage.to_csv('./data/beverages.csv')

dressing_keywords = ['DRSNG']
dressing_pattern = '|'.join(dressing_keywords)

dressing = df[df["Name"].str.contains(dressing_pattern)]

dressing = dressing.sort_values(by='Calories', ascending=False)
#dressing.to_csv('./data/dressings.csv')

egg_keywords = ['EGG,']
egg_pattern = '|'.join(egg_keywords)

egg = df[df["Name"].str.contains(egg_pattern)]

egg = egg.sort_values(by='Calories', ascending=False)
#egg.to_csv('./data/eggs.csv')

yogurt_keywords = ['YOGURT,']
yogurt_pattern = '|'.join(yogurt_keywords)

yogurt = df[df["Name"].str.contains(yogurt_pattern)]

yogurt = yogurt.sort_values(by='Calories', ascending=False)
#yogurt.to_csv('./data/yogurts.csv')

oil_keywords = ['OIL,']
oil_pattern = '|'.join(oil_keywords)

oil = df[df["Name"].str.contains(oil_pattern)]

oil = oil.sort_values(by='Calories', ascending=False)
#oil.to_csv('./data/oils.csv')

cake_keywords = ['CAKE', 'SHORTENING']
cake_pattern = '|'.join(cake_keywords)

cake = df[df["Name"].str.contains(cake_pattern)]

cake = cake.sort_values(by='Calories', ascending=False)
#cake.to_csv('./data/cakes.csv')

butter_keywords = ['BUTTER,', 'MARGARINE']
butter_pattern = '|'.join(butter_keywords)

not_butter = [ 'COOKIE']
not_butter_pattern = '|'.join(not_butter)

butter = df[df["Name"].str.contains(butter_pattern)]
butter = butter[~butter["Name"].str.contains(not_butter_pattern)]

butter = butter.sort_values(by='Calories', ascending=False)
#butter.to_csv('./data/butters.csv')

chicken_keywords = ['CHICKEN', 'POULTRY', 'CHCKN']
chicken_pattern = '|'.join(chicken_keywords)

chicken = df[df["Name"].str.contains(chicken_pattern)]

chicken = chicken.sort_values(by='Calories', ascending=False)
#chicken.to_csv('./data/chickens.csv')

duck_keywords = ['DUCK,']
duck_pattern = '|'.join(duck_keywords)

not_duck = ['SOUP']
not_duck_pattern = '|'.join(not_duck)

duck = df[df["Name"].str.contains(duck_pattern)]
duck = duck[~duck["Name"].str.contains(not_duck_pattern)]

duck = duck.sort_values(by='Calories', ascending=False)
#duck.to_csv('./data/ducks.csv')

goose_keywords = ['GOOSE,']
goose_pattern = '|'.join(goose_keywords)

not_goose = ['SOUP']
not_goose_pattern = '|'.join(not_goose)

goose = df[df["Name"].str.contains(goose_pattern)]
goose = goose[~goose["Name"].str.contains(not_goose_pattern)]

goose = goose.sort_values(by='Calories', ascending=False)
#goose.to_csv('./data/gooses.csv')

emu_keywords = ['EMU,']
emu_pattern = '|'.join(emu_keywords)

not_emu = ['BABYFOOD', 'SOUP']
not_emu_pattern = '|'.join(not_emu)

emu = df[df["Name"].str.contains(emu_pattern)]
emu = emu[~emu["Name"].str.contains(not_emu_pattern)]

emu = emu.sort_values(by='Calories', ascending=False)
#emu.to_csv('./data/emus.csv')

ostrich_keywords = ['OSTRICH,']
ostrich_pattern = '|'.join(ostrich_keywords)

not_ostrich = ['BABYFOOD', 'SOUP']
not_ostrich_pattern = '|'.join(not_ostrich)

ostrich = df[df["Name"].str.contains(ostrich_pattern)]
ostrich = ostrich[~ostrich["Name"].str.contains(not_ostrich_pattern)]

ostrich = ostrich.sort_values(by='Calories', ascending=False)
#ostrich.to_csv('./data/ostrichs.csv')

cow_keywords = ['STEAK,', 'BEEF,']
cow_pattern = '|'.join(cow_keywords)

cow = df[df["Name"].str.contains(cow_pattern)]

cow = cow.sort_values(by='Calories', ascending=False)
#cow.to_csv('./data/cows.csv')

pig_keywords = ['PORK,', 'SAUSAGE,', 'HAM,']
pig_pattern = '|'.join(pig_keywords)

pig = df[df["Name"].str.contains(pig_pattern)]

pig = pig.sort_values(by='Calories', ascending=False)
#pig.to_csv('./data/pigs.csv')

lamb_keywords = ['LAMB,']
lamb_pattern = '|'.join(lamb_keywords)

lamb = df[df["Name"].str.contains(lamb_pattern)]

lamb = lamb.sort_values(by='Calories', ascending=False)
#lamb.to_csv('./data/lambs.csv')

gravy_keywords = ['GRAVY,']
gravy_pattern = '|'.join(gravy_keywords)

not_gravy = ['SOUP']
not_gravy_pattern = '|'.join(not_gravy)

gravy = df[df["Name"].str.contains(gravy_pattern)]
gravy = gravy[~gravy["Name"].str.contains(not_gravy_pattern)]

gravy = gravy.sort_values(by='Calories', ascending=False)
#gravy.to_csv('./data/gravy.csv')

veal_keywords = ['VEAL,']
veal_pattern = '|'.join(veal_keywords)

veal = df[df["Name"].str.contains(veal_pattern)]

veal = veal.sort_values(by='Calories', ascending=False)
#veal.to_csv('./data/veal.csv')

game_keywords = ['GAME MEAT,']
game_pattern = '|'.join(game_keywords)

game = df[df["Name"].str.contains(game_pattern)]

game = game.sort_values(by='Calories', ascending=False)
#game.to_csv('./data/game.csv')

pie_keywords = ['PIE,']
pie_pattern = '|'.join(pie_keywords)

pie = df[df["Name"].str.contains(pie_pattern)]

pie = pie.sort_values(by='Calories', ascending=False)
#pie.to_csv('./data/pies.csv')

pudding_keywords = ['PUDDING']
pudding_pattern = '|'.join(pudding_keywords)

pudding = df[df["Name"].str.contains(pudding_pattern)]

pudding = pudding.sort_values(by='Calories', ascending=False)
#pudding.to_csv('./data/puddings.csv')

apple_keywords = ['APPLES']
apple_pattern = '|'.join(apple_keywords)

apple = df[df["Name"].str.contains(apple_pattern)]

apple = apple.sort_values(by='Calories', ascending=False)
#apple.to_csv('./data/apples.csv')

apricot_keywords = ['APRICOT']
apricot_pattern = '|'.join(apricot_keywords)

not_apricot = ['OIL']
not_apricot_pattern = '|'.join(not_apricot)

apricot = df[df["Name"].str.contains(apricot_pattern)]
apricot = apricot[~apricot["Name"].str.contains(not_apricot_pattern)]

apricot = apricot.sort_values(by='Calories', ascending=False)
#apricot.to_csv('./data/apricots.csv')

fruit_keywords = ["APPLE", "ORANGE", "BANANA", "PINEAPPLE", "WATERMELON", "KIWI", "GRAPEFRUIT", "PEAR", "PEACH", "MANGO", "BLUEBERRY", "STRAWBERRY", "CHERRY", "PLUM", "APRICOT", "LEMON,AVOCADO, BLACKBERRY", "LIME", "POMEGRANATE", "CANTALOUPE", "HONEYDEW", "AVOCADO", "BLACKBERRY"]
fruit_pattern = '|'.join(fruit_keywords)

not_fruit = ['OIL', 'CHIP', 'PORK', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD']
not_fruit_pattern = '|'.join(not_fruit)

fruit = df[df["Name"].str.contains(fruit_pattern)]
fruit = fruit[~fruit["Name"].str.contains(not_fruit_pattern)]

fruit = fruit.sort_values(by='Calories', ascending=False)
#fruit.to_csv('./data/fruits.csv')

veggie_keywords = ["CARROTS," ,"BROCCOLI," ,"CAULIFLOWER," ,"BEETS," ,"CABBAGE," ,"SPINACH," ,"KALE," ,"ZUCCHINI," ,"EGGPLANT," ,"TOMATOES," ,"CUCUMBERS," ,"RADISHES," ,"GARLIC," ,"ONIONS," ,"PEPPERS," ,"MUSHROOMS," ,"ASPARAGUS," ,"SWEET POTATOES," ,"LETTUCE," ,"BRUSSELS SPROUTS"]
veggie_pattern = '|'.join(veggie_keywords)

not_veggie = ['SOUP', 'OIL', 'CHIP', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD']
not_veggie_pattern = '|'.join(not_veggie)

veggie = df[df["Name"].str.contains(veggie_pattern)]
veggie = veggie[~veggie["Name"].str.contains(not_veggie_pattern)]

veggie = veggie.sort_values(by='Calories', ascending=False)
#veggie.to_csv('./data/veggies.csv')
                   
nut_keywords = ["ALMOND", "BRAZIL NUT", "CASHEW", "CHESTNUT", "COCONUT", "FILBERT", "HAZELNUT", "MACADAMIA NUT", "PEANUT", "PECAN", "PINE NUT", "PISTACHIO", "WALNUT", "CHINQUAPIN", "COLA NUT", "WATER CHESTNUT", "BUTTERNUT", "HICKORY NUT", "ACORN", "KOLA NUT"]
nut_pattern = '|'.join(nut_keywords)

not_nut = ['BUTTER', 'SOUP', 'OIL', 'CHIP', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD']
not_nut_pattern = '|'.join(not_nut)

nut = df[df["Name"].str.contains(nut_pattern)]
nut = nut[~nut["Name"].str.contains(not_nut_pattern)]

nut = nut.sort_values(by='Calories', ascending=False)
#nut.to_csv('./data/nuts.csv')
                   
chocolate_keywords = ['CHOCOLATE', 'COCOA']
chocolate_pattern = '|'.join(chocolate_keywords)

not_chocolate = ['BUTTER', 'SOUP', 'OIL','COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'BREAD']
not_chocolate_pattern = '|'.join(not_chocolate)

chocolate = df[df["Name"].str.contains(chocolate_pattern)]
chocolate = chocolate[~chocolate["Name"].str.contains(not_chocolate_pattern)]

chocolate = chocolate.sort_values(by='Calories', ascending=False)
#chocolate.to_csv('./data/chocolates.csv')

snack_keywords = ['SNACK']
snack_pattern = '|'.join(snack_keywords)

snack = df[df["Name"].str.contains(snack_pattern)]

snack = snack.sort_values(by='Calories', ascending=False)
#snack.to_csv('./data/snacks.csv')



#Calculate Means


milk.loc['9999'] = milk.mean()
milk.loc['9999', ['Name']] = ['milk_Average']
milk.loc['9999', ['id']] = ['99999']
milk = milk.round(decimals=2)
milk_average = milk.tail(1)


fruit.loc['9999'] = fruit.mean()
fruit.loc['9999', ['Name']] = ['Fruit_Average']
fruit.loc['9999', ['id']] = ['99999']
fruit = fruit.round(decimals=2)
fruit_average = fruit.tail(1)


cheese.loc['9999'] = cheese.mean()
cheese.loc['9999', ['Name']] = ['cheese_Average']
cheese.loc['9999', ['id']] = ['99999']
cheese = cheese.round(decimals=2)
cheese_average = cheese.tail(1)


soup.loc['9999'] = soup.mean()
soup.loc['9999', ['Name']] = ['soup_Average']
soup.loc['9999', ['id']] = ['99999']
soup = soup.round(decimals=2)
soup_average = soup.tail(1)


cereal.loc['9999'] = cereal.mean()
cereal.loc['9999', ['Name']] = ['cereal_Average']
cereal.loc['9999', ['id']] = ['99999']
cereal = cereal.round(decimals=2)
cereal_average = cereal.tail(1)


cookies.loc['9999'] = cookies.mean()
cookies.loc['9999', ['Name']] = ['cookies_Average']
cookies.loc['9999', ['id']] = ['99999']
cookies = cookies.round(decimals=2)
cookies_average = cookies.tail(1)


babyfood.loc['9999'] = babyfood.mean()
babyfood.loc['9999', ['Name']] = ['babyfood_Average']
babyfood.loc['9999', ['id']] = ['99999']
babyfood = babyfood.round(decimals=2)
babyfood_average = babyfood.tail(1)


beans.loc['9999'] = beans.mean()
beans.loc['9999', ['Name']] = ['beans_Average']
beans.loc['9999', ['id']] = ['99999']
beans = beans.round(decimals=2)
beans_average = beans.tail(1)


rice.loc['9999'] = rice.mean()
rice.loc['9999', ['Name']] = ['rice_Average']
rice.loc['9999', ['id']] = ['99999']
rice = rice.round(decimals=2)
rice_average = rice.tail(1)


ice_cream.loc['9999'] = ice_cream.mean()
ice_cream.loc['9999', ['Name']] = ['ice_cream_Average']
ice_cream.loc['9999', ['id']] = ['99999']
ice_cream = ice_cream.round(decimals=2)
ice_cream_average = ice_cream.tail(1)


chips.loc['9999'] = chips.mean()
chips.loc['9999', ['Name']] = ['chips_Average']
chips.loc['9999', ['id']] = ['99999']
chips = chips.round(decimals=2)
chips_average = chips.tail(1)


pasta.loc['9999'] = pasta.mean()
pasta.loc['9999', ['Name']] = ['pasta_Average']
pasta.loc['9999', ['id']] = ['99999']
pasta = pasta.round(decimals=2)
pasta_average = pasta.tail(1)

fast_food.loc['9999'] = fast_food.mean()
fast_food.loc['9999', ['Name']] = ['fast_food_Average']
fast_food.loc['9999', ['id']] = ['99999']
fast_food = fast_food.round(decimals=2)
fast_food_average = fast_food.tail(1)

pizza.loc['9999'] = pizza.mean()
pizza.loc['9999', ['Name']] = ['pizza_Average']
pizza.loc['9999', ['id']] = ['99999']
pizza = pizza.round(decimals=2)
pizza_average = pizza.tail(1)

school_lunch.loc['9999'] = school_lunch.mean()
school_lunch.loc['9999', ['Name']] = ['school_lunch_Average']
school_lunch.loc['9999', ['id']] = ['99999']
school_lunch = school_lunch.round(decimals=2)
school_lunch_average = school_lunch.tail(1)

beef.loc['9999'] = beef.mean()
beef.loc['9999', ['Name']] = ['beef_Average']
beef.loc['9999', ['id']] = ['99999']
beef = beef.round(decimals=2)
beef_average = beef.tail(1)

bread.loc['9999'] = bread.mean()
bread.loc['9999', ['Name']] = ['bread_Average']
bread.loc['9999', ['id']] = ['99999']
bread = bread.round(decimals=2)
bread_average = bread.tail(1)

fish.loc['9999'] = fish.mean()
fish.loc['9999', ['Name']] = ['fish_Average']
fish.loc['9999', ['id']] = ['99999']
fish = fish.round(decimals=2)
fish_average = fish.tail(1)

candy.loc['9999'] = candy.mean()
candy.loc['9999', ['Name']] = ['candy_Average']
candy.loc['9999', ['id']] = ['99999']
candy = candy.round(decimals=2)
candy_average = candy.tail(1)

beverage.loc['9999'] = beverage.mean()
beverage.loc['9999', ['Name']] = ['beverage_Average']
beverage.loc['9999', ['id']] = ['99999']
beverage = beverage.round(decimals=2)
beverage_average = beverage.tail(1)

dressing.loc['9999'] = dressing.mean()
dressing.loc['9999', ['Name']] = ['dressing_Average']
dressing.loc['9999', ['id']] = ['99999']
dressing = dressing.round(decimals=2)
dressing_average = dressing.tail(1)


egg.loc['9999'] = egg.mean()
egg.loc['9999', ['Name']] = ['egg_Average']
egg.loc['9999', ['id']] = ['99999']
egg = egg.round(decimals=2)
egg_average = egg.tail(1)


yogurt.loc['9999'] = yogurt.mean()
yogurt.loc['9999', ['Name']] = ['yogurt_Average']
yogurt.loc['9999', ['id']] = ['99999']
yogurt = yogurt.round(decimals=2)
yogurt_average = yogurt.tail(1)


oil.loc['9999'] = oil.mean()
oil.loc['9999', ['Name']] = ['oil_Average']
oil.loc['9999', ['id']] = ['99999']
oil = oil.round(decimals=2)
oil_average = oil.tail(1)


cake.loc['9999'] = cake.mean()
cake.loc['9999', ['Name']] = ['cake_Average']
cake.loc['9999', ['id']] = ['99999']
cake = cake.round(decimals=2)
cake_average = cake.tail(1)


butter.loc['9999'] = butter.mean()
butter.loc['9999', ['Name']] = ['butter_Average']
butter.loc['9999', ['id']] = ['99999']
butter = butter.round(decimals=2)
butter_average = butter.tail(1)


chicken.loc['9999'] = chicken.mean()
chicken.loc['9999', ['Name']] = ['chicken_Average']
chicken.loc['9999', ['id']] = ['99999']
chicken = chicken.round(decimals=2)
chicken_average = chicken.tail(1)


duck.loc['9999'] = duck.mean()
duck.loc['9999', ['Name']] = ['duck_Average']
duck.loc['9999', ['id']] = ['99999']
duck = duck.round(decimals=2)
duck_average = duck.tail(1)


goose.loc['9999'] = goose.mean()
goose.loc['9999', ['Name']] = ['goose_Average']
goose.loc['9999', ['id']] = ['99999']
goose = goose.round(decimals=2)
goose_average = goose.tail(1)


chocolate.loc['9999'] = chocolate.mean()
chocolate.loc['9999', ['Name']] = ['chocolate_Average']
chocolate.loc['9999', ['id']] = ['99999']
chocolate = chocolate.round(decimals=2)
chocolate_average = chocolate.tail(1)

ostrich.loc['9999'] = ostrich.mean()
ostrich.loc['9999', ['Name']] = ['ostrich_Average']
ostrich.loc['9999', ['id']] = ['99999']
ostrich = ostrich.round(decimals=2)
ostrich_average = ostrich.tail(1)

emu.loc['9999'] = emu.mean()
emu.loc['9999', ['Name']] = ['ostrich_Average']
emu.loc['9999', ['id']] = ['99999']
emu = emu.round(decimals=2)
emu_average = emu.tail(1)

cow.loc['9999'] = cow.mean()
cow.loc['9999', ['Name']] = ['cow_Average']
cow.loc['9999', ['id']] = ['99999']
cow = cow.round(decimals=2)
cow_average = cow.tail(1)

pig.loc['9999'] = pig.mean()
pig.loc['9999', ['Name']] = ['pig_Average']
pig.loc['9999', ['id']] = ['99999']
pig = pig.round(decimals=2)
pig_average = pig.tail(1)

lamb.loc['9999'] = lamb.mean()
lamb.loc['9999', ['Name']] = ['lamb_Average']
lamb.loc['9999', ['id']] = ['99999']
lamb = lamb.round(decimals=2)
lamb_average = lamb.tail(1)

veal.loc['9999'] = veal.mean()
veal.loc['9999', ['Name']] = ['veal_Average']
veal.loc['9999', ['id']] = ['99999']
veal = veal.round(decimals=2)
veal_average = veal.tail(1)

game.loc['9999'] = game.mean()
game.loc['9999', ['Name']] = ['game_Average']
game.loc['9999', ['id']] = ['99999']
game = game.round(decimals=2)
game_average = game.tail(1)

gravy.loc['9999'] = gravy.mean()
gravy.loc['9999', ['Name']] = ['gravy_Average']
gravy.loc['9999', ['id']] = ['99999']
gravy = gravy.round(decimals=2)
gravy_average = gravy.tail(1)

pie.loc['9999'] = pie.mean()
pie.loc['9999', ['Name']] = ['pie_Average']
pie.loc['9999', ['id']] = ['99999']
pie = pie.round(decimals=2)
pie_average = pie.tail(1)

pudding.loc['9999'] = pudding.mean()
pudding.loc['9999', ['Name']] = ['pudding_Average']
pudding.loc['9999', ['id']] = ['99999']
pudding = pudding.round(decimals=2)
pudding_average = pudding.tail(1)

soup.loc['9999'] = soup.mean()
soup.loc['9999', ['Name']] = ['soup_Average']
soup.loc['9999', ['id']] = ['99999']
soup = soup.round(decimals=2)
soup_average = soup.tail(1)

apple.loc['9999'] = apple.mean()
apple.loc['9999', ['Name']] = ['apple_Average']
apple.loc['9999', ['id']] = ['99999']
apple = apple.round(decimals=2)
apple_average = apple.tail(1)

apricot.loc['9999'] = apricot.mean()
apricot.loc['9999', ['Name']] = ['apricot_Average']
apricot.loc['9999', ['id']] = ['99999']
apricot = apricot.round(decimals=2)
apricot_average = apricot.tail(1)

veggie.loc['9999'] = veggie.mean()
veggie.loc['9999', ['Name']] = ['veggie_Average']
veggie.loc['9999', ['id']] = ['99999']
veggie = veggie.round(decimals=2)
veggie_average = veggie.tail(1)

nut.loc['9999'] = nut.mean()
nut.loc['9999', ['Name']] = ['nuts_Average']
nut.loc['9999', ['id']] = ['99999']
nut = nut.round(decimals=2)
nut_average = nut.tail(1)

chocolate.loc['9999'] = chocolate.mean()
chocolate.loc['9999', ['Name']] = ['chocolate_Average']
chocolate.loc['9999', ['id']] = ['99999']
chocolate = chocolate.round(decimals=2)
chocolate_average = chocolate.tail(1)

snack.loc['9999'] = snack.mean()
snack.loc['9999', ['Name']] = ['chocolate_Average']
snack.loc['9999', ['id']] = ['99999']
snack = snack.round(decimals=2)
snack_average = snack.tail(1)