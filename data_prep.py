import pandas as pd
import numpy as np

df = pd.read_csv('./data/ABBREV.csv')

df.dropna(subset=['GmWt_1'], inplace=True)

cols_to_divide = [col for col in df.columns if 'µg' in col]
df.loc[:, cols_to_divide] = df.loc[:, cols_to_divide] / 1000

df = df.rename(columns={
    col: col.replace('µg', 'mg') for col in df.columns
})

cols_to_divide = [col for col in df.columns if '(g)' in col]
df.loc[:, cols_to_divide] = df.loc[:, cols_to_divide] * 1000

df = df.rename(columns={
    col: col.replace('(g)', '(mg)') for col in df.columns
})

df = df.round(decimals = 1)

df['Total_Fat_(mg)'] = df['FA_Mono_(mg)'] + df['FA_Sat_(mg)']
df['Vitamins_(mg)'] = df.filter(like='Vit').sum(axis=1)

unhealthy_list = ['Sugar_Tot_(mg)', 'Lipid_Tot_(mg)', 'Cholestrl_(mg)', 'FA_Sat_(mg)']
df['Unhealthy_Nutrients'] = df[unhealthy_list].sum(axis=1)

healthy_list = ['Water_(mg)', 'Protein_(mg)', 'Fiber_TD_(mg)', 'Calcium_(mg)', 'Iron_(mg)', 'Magnesium_(mg)', 'Phosphorus_(mg)', 'Potassium_(mg)', 'Sodium_(mg)', 'Zinc_(mg)', 'Copper_mg)', 'Manganese_(mg)', 'Selenium_(mg)', 'Thiamin_(mg)', 'Riboflavin_(mg)', 'Niacin_(mg)', 'Folate_Tot_(mg)', 'Folic_Acid_(mg)', 'Food_Folate_(mg)', 'Folate_DFE_(mg)', 'Retinol_(mg)', 'Alpha_Carot_(mg)', 'Beta_Carot_(mg)', 'Beta_Crypt_(mg)', 'Lycopene_(mg)', 'FA_Mono_(mg)', 'FA_Poly_(mg)', 'Vitamins_(mg)']

df['Healthy_Nutrients'] = df[healthy_list].sum(axis=1)

df['Health_Score'] = df['Healthy_Nutrients'] - df['Unhealthy_Nutrients'] / df['GmWt_1']
df = df[["NDB_No", "Shrt_Desc", "Energ_Kcal", "Protein_(mg)", "Carbohydrt_(mg)", "Fiber_TD_(mg)", "Sugar_Tot_(mg)", "Calcium_(mg)", "Sodium_(mg)", "Total_Fat_(mg)", "Potassium_(mg)", "Water_(mg)", 'Vitamins_(mg)', 'Unhealthy_Nutrients', 'Healthy_Nutrients', 'Health_Score']].copy()
df = df.rename(columns={'Energ_Kcal':'Calories',  'Shrt_Desc':'Name', 'NDB_No':'id', 'Carbohydrt_(mg)':'Carbs_(mg)', 'Protein_(mg)':'Protein_(mg)', 'Fiber_TD_(mg)':'Fiber_(mg)', 'Sugar_Tot_(mg)':'Sugar_(mg)', 'Calcium_(mg)':'Calcium_(mg)', 'Sodium_(mg)':'Sodium_(mg)'})


################################################################################################################
# Food Groups

water_keywords = ['WATER,']
water_pattern = '|'.join(water_keywords)

not_water = ['FRESHWATER', 'SUGAR']
not_water_pattern = '|'.join(not_water)

water = df[df["Name"].str.contains(water_pattern)]
water = water[~water["Name"].str.contains(not_water_pattern)]

water = water.sort_values(by='Calories', ascending=False)
#water.to_csv('./data/water.csv')

cheese_keywords = ['CHEESE,', 'PARMESAN']
cheese_pattern = '|'.join(cheese_keywords)

not_cheese = ['CRACKERS', 'FAST FOOD', 'PASTA']
not_cheese_pattern = '|'.join(not_cheese)

cheese = df[df["Name"].str.contains(cheese_pattern)]
cheese = cheese[~cheese["Name"].str.contains(not_cheese_pattern)]

cheese = cheese.sort_values(by='Calories', ascending=False)
#cheese.to_csv('./data/cheeses.csv')

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


babyfood_keywords = ['BABYFOOD', 'INF FORMULA', 'INF FORM']
babyfood_pattern = '|'.join(babyfood_keywords)

babyfood = df[df["Name"].str.contains(babyfood_pattern)]

babyfood = babyfood.sort_values(by='Calories', ascending=False)
#babyfood.to_csv('./data/babyfoods.csv')

beans_keywords = ['BEANS', 'BNS,']
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

not_pasta = ['CHINESE']
not_pasta_pattern = '|'.join(not_pasta)

pasta = df[df["Name"].str.contains(pasta_pattern)]
pasta = pasta[~pasta["Name"].str.contains(not_pasta_pattern)]

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

not_bread = ['SOUP', 'SHORTENING', 'COOKIE', 'PIE', 'CAKE', 'FRIED', 'CRUMBS', 'MIX', 'BANANA']
not_bread_pattern = '|'.join(not_bread)

bread = df[df["Name"].str.startswith('BREAD,')]
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

na_beverage_keywords = ['BEVERAGE', 'BEV,', 'JUC', 'JUICE', 'DRK']
na_beverage_keywords_pattern = '|'.join(na_beverage_keywords)

not_na_beverage = ['ALCOHOL', 'WATER,']
not_na_beverage_pattern = '|'.join(not_fish)

na_beverage = df[df["Name"].str.contains(na_beverage_keywords_pattern)]
na_beverage = na_beverage[~na_beverage["Name"].str.contains(not_na_beverage_pattern)]

na_beverage = na_beverage.sort_values(by='Calories', ascending=False)
#na_beverage_keywords.to_csv('./data/na_beverage_keywords.csv')

alcoholic_beverage_keywords = ['ALCOHOL']
alcoholic_beverage_keywords_pattern = '|'.join(alcoholic_beverage_keywords)

not_alcoholic_beverage = ['NON-ALCOHOL', 'WATER,']
not_alcoholic_beverage_pattern = '|'.join(not_fish)

alcoholic_beverage = df[df["Name"].str.contains(alcoholic_beverage_keywords_pattern)]
alcoholic_beverage = alcoholic_beverage[~alcoholic_beverage["Name"].str.contains(not_alcoholic_beverage_pattern)]

alcoholic_beverage = alcoholic_beverage.sort_values(by='Calories', ascending=False)
#alcoholic_beverage_keywords.to_csv('./data/alcoholic_beverage_keywords.csv')

dressing_keywords = ['DRSNG','CATSUP','SAUCE','CONDIMENT', 'DRESSING', "KETCHUP", "MAYONNAISE", "MUSTARD", "HOT SAUCE", "SOY SAUCE", "SRIRACHA", "TARTAR SAUCE", "WORCESTERSHIRE SAUCE", "BARBECUE SAUCE", "HONEY MUSTARD", "THOUSAND ISLAND DRESSING", "AIOLI", "RELISH", "SWEET CHILI SAUCE", "HORSERADISH", "SALSA", "CANE SYRUP", "RANCH DRESSING", "CHIMICHURRI"]
dressing_pattern = '|'.join(dressing_keywords)

not_dressings = ['OIL', 'SALSA', 'APPLE', 'PIZZA', 'GRNS', 'SPINACH', 'GREENS']
not_dressings_pattern = '|'.join(not_dressings)

dressing = df[df["Name"].str.contains(dressing_pattern)]
dressing = dressing[~dressing["Name"].str.contains(not_dressings_pattern)]

dressing = dressing.sort_values(by='Calories', ascending=False)
#dressing.to_csv('./data/dressings.csv')

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

not_butter = [ 'COOKIE', 'MARGARINE']
not_butter_pattern = '|'.join(not_butter)

butter = df[df["Name"].str.contains(butter_pattern)]
butter = butter[~butter["Name"].str.contains(not_butter_pattern)]

butter = butter.sort_values(by='Calories', ascending=False)
#butter.to_csv('./data/butters.csv')

margarine_keywords = ['MARGARINE,']
margarine_pattern = '|'.join(margarine_keywords)

not_margarine = ['BREAD']
not_margarine_pattern = '|'.join(not_margarine)

margarine = df[df["Name"].str.contains(margarine_pattern)]
margarine = margarine[~margarine["Name"].str.contains(not_margarine_pattern)]

margarine = margarine.sort_values(by='Calories', ascending=False)
#margarine.to_csv('./data/margarines.csv')

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

cow_keywords = ['STEAK,', 'BEEF,', 'BF,']
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

turkey_keywords = ['TURKEY']
turkey_pattern = '|'.join(turkey_keywords)

not_turkey = ['GRAVY']
not_turkey_pattern = '|'.join(not_turkey)

turkey = df[df["Name"].str.contains(turkey_pattern)]
turkey = turkey[~turkey["Name"].str.contains(not_turkey_pattern)]

turkey = turkey.sort_values(by='Calories', ascending=False)
#turkey.to_csv('./data/turkey.csv')

gravy_keywords = ['GRAVY,']
gravy_pattern = '|'.join(gravy_keywords)

not_gravy = ['SOUP', 'W/ GRAVY', 'W/GRAVY']
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

not_fruit = ['OIL', 'CHIP', 'PORK', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD', 'BEV']
not_fruit_pattern = '|'.join(not_fruit)

fruit = df[df["Name"].str.contains(fruit_pattern)]
fruit = fruit[~fruit["Name"].str.contains(not_fruit_pattern)]

fruit = fruit.sort_values(by='Calories', ascending=False)
#fruit.to_csv('./data/fruits.csv')

veggie_keywords = ["CARROTS," , 'GRNS',"BROCCOLI," ,"CAULIFLOWER," ,"BEETS," ,"CABBAGE," ,"SPINACH," ,"KALE," ,"ZUCCHINI," ,"EGGPLANT," ,"TOMATOES," ,"CUCUMBERS," ,"RADISHES," ,"GARLIC," ,"ONIONS," ,"PEPPERS," ,"MUSHROOMS," ,"ASPARAGUS," ,"SWEET POTATOES," ,"LETTUCE," ,"BRUSSELS SPROUTS", 'BEV']
veggie_pattern = '|'.join(veggie_keywords)

not_veggie = ['SOUP', 'OIL', 'CHIP', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD']
not_veggie_pattern = '|'.join(not_veggie)

veggie = df[df["Name"].str.contains(veggie_pattern)]
veggie = veggie[~veggie["Name"].str.contains(not_veggie_pattern)]

veggie = veggie.sort_values(by='Calories', ascending=False)
#veggie.to_csv('./data/veggies.csv')
                   
nut_keywords = ["ALMOND", "BRAZIL NUT", "CASHEW", "CHESTNUT", "COCONUT", "FILBERT", "HAZELNUT", "MACADAMIA NUT", "PEANUT", "PECAN", "PINE NUT", "PISTACHIO", "WALNUT", "CHINQUAPIN", "COLA NUT", "WATER CHESTNUT", "BUTTERNUT", "HICKORY NUT", "ACORN", "KOLA NUT"]
nut_pattern = '|'.join(nut_keywords)

not_nut = ['BUTTER', 'KEEBLER', 'SOUP', 'OIL', 'CHIP', 'COCONUT', 'BEV', 'BAR', 'SPRD', 'CANDIES', 'BEVERAGE', 'COOKIE', 'WAFER', 'MUFFIN', 'INF FORM', 'BABYFOOD', 'KELLOGG', 'CEREAL', 'CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'TSTR', 'PIE', 'APPLEBEE', 'SNACK', 'SUGAR', 'YOGURT', 'SUNDAE', 'ICE CREAM', 'SYRUP', 'BREAD']
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

snack_keywords = ['SNACK', 'CHIPS', 'CANDIES', 'CANDY', 'POPCORN', 'TRAIL MIX']
snack_pattern = '|'.join(snack_keywords)

snack = df[df["Name"].str.contains(snack_pattern)]

snack = snack.sort_values(by='Calories', ascending=False)
#snack.to_csv('./data/snacks.csv')

dessert_keywords = ['DESSERT', 'COCOA', 'COOKIE', 'DOUGHNUT','CAKE', 'PUDDING', 'PASTRY', 'TAPIOCA', 'PIE', 'ICE CREAM', 'SUNDAE', 'WAFER', 'SWEET ROLL', 'CHEESECAKE', 'TIRAMISU', 'TART', 'BROWNIE', 'MOUSSE', 'MERINGUE', 'PIZZELLE']
dessert_pattern = '|'.join(dessert_keywords)

not_dessert = ['OIL', 'MIX', 'SHORTENING', 'TOPPING', 'FILLING', 'BABYFOOD', 'INF FORMULA', 'INF FORM', 'BARBECUE']
not_dessert_pattern = '|'.join(not_dessert)

dessert = df[df["Name"].str.contains(dessert_pattern)]
dessert = dessert[~dessert["Name"].str.contains(not_dessert_pattern)]

dessert = dessert.sort_values(by='Calories', ascending=False)
#dessert.to_csv('./data/desserts.csv')

seasoning_keywords = ['SEASONING','SALT,', "BASIL", "OREGANO", "THYME", "ROSEMARY", "CUMIN", "CAYENNE PEPPER", "GINGER,", "TURMERIC", "PAPRIKA", "CINNAMON,", "NUTMEG", "FENNEL", "ALLSPICE", "CARDAMOM", "GARLIC POWDER", "ONION POWDER", "CLOVES", "LEMON PEPPER"]
seasoning_pattern = '|'.join(seasoning_keywords)

not_seasoning = ['OIL', 'BUTTER', 'MARGARINE', 'SAU', 'SAUCE', 'CHIP', 'RICE', 'BEANS', 'TUNA', 'TSTD', 'PIZZA', 'SALMON', 'CORN', 'NO SALT', 'W/ SALT', 'FRZ', 'SMOKED', 'CKD', 'SOUP', 'LO SALT']
not_seasoning_pattern = '|'.join(not_seasoning)

seasoning = df[df["Name"].str.contains(seasoning_pattern)]
seasoning = seasoning[~seasoning["Name"].str.contains(not_seasoning_pattern)]

seasoning = seasoning.sort_values(by='Calories', ascending=False)
#seasoning.to_csv('./data/seasonings.csv')

chinese_food_keywords = ['CHINESE', 'CHINA']
chinese_food_pattern = '|'.join(chinese_food_keywords)

chinese_food = df[df["Name"].str.contains(chinese_food_pattern)]

chinese_food = chinese_food.sort_values(by='Calories', ascending=False)
#chinese_food.to_csv('./data/chinese_foods.csv')

chinese_food_keywords = ['CHINESE', 'CHINA']
chinese_food_pattern = '|'.join(chinese_food_keywords)

#not_chinese_food = ['OIL', 'BUTTER', 'MARGARINE', 'SAU', 'SAUCE', 'CHIP', 'RICE', 'BEANS', 'TUNA', 'TSTD', 'PIZZA', 'SALMON', 'CORN', 'NO SALT', 'W/ SALT', 'FRZ', 'SMOKED', 'CKD', 'SOUP', 'LO SALT']
#not_chinese_food_pattern = '|'.join(not_chinese_food)

chinese_food = df[df["Name"].str.contains(chinese_food_pattern)]
#chinese_food = chinese_food[~chinese_food["Name"].str.contains(not_chinese_food_pattern)]

chinese_food = chinese_food.sort_values(by='Calories', ascending=False)
#chinese_food.to_csv('./data/chinese_foods.csv')

sea_food_keywords = ['SEAFOOD',"LOBSTER", "CRAB", 'CRUSTACEAN',"SHRIMP", "OYSTER,", "CLAM", "MUSSEL", "SCALLOP,", "SQUID", "OCTOPUS", "CRAYFISH", "LOBSTER TAIL", "LANGOUSTINE", "SEA URCHIN", "GEODUCK", "ABALONE", "REDFISH", "SEA CUCUMBER", "SEA SNAIL", "RAZOR CLAM", "SEAWEED"]
sea_food_pattern = '|'.join(sea_food_keywords)

not_sea_food = ['OIL', 'CRACKERS', 'BEEF', 'FAST FOOD', 'CHOWDER', 'SOUP']
not_sea_food_pattern = '|'.join(not_sea_food)

sea_food = df[df["Name"].str.contains(sea_food_pattern)]
sea_food = sea_food[~sea_food["Name"].str.contains(not_sea_food_pattern)]

sea_food = sea_food.sort_values(by='Calories', ascending=False)
#sea_food.to_csv('./data/sea_foods.csv')

canned_food_keywords = ['CANNED', 'CAMPBELL', 'COND']
canned_food_pattern = '|'.join(canned_food_keywords)

not_canned_food = ['CONDMNT']
not_canned_food_pattern = '|'.join(not_canned_food)

canned_food = df[df["Name"].str.contains(canned_food_pattern)]
canned_food = canned_food[~canned_food["Name"].str.contains(not_canned_food_pattern)]

canned_food = canned_food.sort_values(by='Calories', ascending=False)
#canned_food.to_csv('./data/canned_foods.csv')

frozen_food_keywords = ['FRZ ENTREE', 'FRZ, UNPRE', 'FRZ,UNPRE','FRZ, PREP', 'FRZ,PREP','FROZEN', 'MICROWAVE', ',FRZ', ', FRZ']
frozen_food_pattern = '|'.join(frozen_food_keywords)

not_frozen_food = ['BEVERAGE', 'CHOPD', 'DRND', 'CAKE', 'PASTRY', 'BERRIES', 'RHUBARB', 'ASPARAGUS', 'BERRY', 'CHERRIES', 'ARTICHOKE', 'BRUSSELS', 'CAULIFLOWER', 'CORN', 'PEAS', 'CONC', 'CARROT', 'BEV,', 'JUC', 'JUICE', 'PREVIOUSLY', 'MICROWAVEABLE', 'MICROWAVED', 'GRNS', 'SQUASH', 'VEGETABLE', 'APPLE', 'TURNIP', 'KALE', 'OKRA']
not_frozen_food_pattern = '|'.join(not_frozen_food)

frozen_food = df[df["Name"].str.contains(frozen_food_pattern)]
frozen_food = frozen_food[~frozen_food["Name"].str.contains(not_frozen_food_pattern)]

frozen_food = frozen_food.sort_values(by='Calories', ascending=False)
#frozen_food.to_csv('./data/frozen_foods.csv')

fat = ['NONFAT', 'FAT FREE', 'LOWFAT', 'LOW FAT', 'LO FAT']
pattern = '|'.join(fat)

lowfat_milk = milk[milk["Name"].str.contains(pattern)]
other_milk = milk[~milk["Name"].str.contains(pattern)]

#########################################################################################################

#Calculate Means

water.loc['9999'] = water.mean()
water.loc['9999', ['Name']] = ['water_average']
water.loc['9999', ['id']] = ['99999']
water = water.round(decimals=2)
water_average = water.tail(1)

milk.loc['9999'] = milk.mean()
milk.loc['9999', ['Name']] = ['milks_average']
milk.loc['9999', ['id']] = ['99999']
milk = milk.round(decimals=2)
milks_average = milk.tail(1)


fruit.loc['9999'] = fruit.mean()
fruit.loc['9999', ['Name']] = ['fruits_average']
fruit.loc['9999', ['id']] = ['99999']
fruit = fruit.round(decimals=2)
fruits_average = fruit.tail(1)


cheese.loc['9999'] = cheese.mean()
cheese.loc['9999', ['Name']] = ['cheeses_average']
cheese.loc['9999', ['id']] = ['99999']
cheese = cheese.round(decimals=2)
cheeses_average = cheese.tail(1)


soup.loc['9999'] = soup.mean()
soup.loc['9999', ['Name']] = ['soups_average']
soup.loc['9999', ['id']] = ['99999']
soup = soup.round(decimals=2)
soups_average = soup.tail(1)

cereal.loc['9999'] = cereal.mean()
cereal.loc['9999', ['Name']] = ['cereals_average']
cereal.loc['9999', ['id']] = ['99999']
cereal = cereal.round(decimals=2)
cereals_average = cereal.tail(1)

cookies.loc['9999'] = cookies.mean()
cookies.loc['9999', ['Name']] = ['cookies_Average']
cookies.loc['9999', ['id']] = ['99999']
cookies = cookies.round(decimals=2)
cookies_average = cookies.tail(1)


babyfood.loc['9999'] = babyfood.mean()
babyfood.loc['9999', ['Name']] = ['babyfoods_average']
babyfood.loc['9999', ['id']] = ['99999']
babyfood = babyfood.round(decimals=2)
babyfoods_average = babyfood.tail(1)


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
ice_cream.loc['9999', ['Name']] = ['ice_creams_average']
ice_cream.loc['9999', ['id']] = ['99999']
ice_cream = ice_cream.round(decimals=2)
ice_creams_average = ice_cream.tail(1)


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
school_lunches_average = school_lunch.tail(1)

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

na_beverage.loc['9999'] = na_beverage.mean()
na_beverage.loc['9999', ['Name']] = ['na_beverages_average']
na_beverage.loc['9999', ['id']] = ['99999']
na_beverage = na_beverage.round(decimals=2)
na_beverages_average = na_beverage.tail(1)

alcoholic_beverage.loc['9999'] = alcoholic_beverage.mean()
alcoholic_beverage.loc['9999', ['Name']] = ['alcoholic_beverages_average']
alcoholic_beverage.loc['9999', ['id']] = ['99999']
alcoholic_beverage = alcoholic_beverage.round(decimals=2)
alcoholic_beverages_average = alcoholic_beverage.tail(1)

dressing.loc['9999'] = dressing.mean()
dressing.loc['9999', ['Name']] = ['dressings/condiments_average']
dressing.loc['9999', ['id']] = ['99999']
dressing = dressing.round(decimals=2)
dressings_average = dressing.tail(1)

yogurt.loc['9999'] = yogurt.mean()
yogurt.loc['9999', ['Name']] = ['yogurts_average']
yogurt.loc['9999', ['id']] = ['99999']
yogurt = yogurt.round(decimals=2)
yogurts_average = yogurt.tail(1)


oil.loc['9999'] = oil.mean()
oil.loc['9999', ['Name']] = ['oils_average']
oil.loc['9999', ['id']] = ['99999']
oil = oil.round(decimals=2)
oils_average = oil.tail(1)


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

ostrich.loc['9999'] = ostrich.mean()
ostrich.loc['9999', ['Name']] = ['ostrich_Average']
ostrich.loc['9999', ['id']] = ['99999']
ostrich = ostrich.round(decimals=2)
ostrich_average = ostrich.tail(1)

emu.loc['9999'] = emu.mean()
emu.loc['9999', ['Name']] = ['emu_Average']
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
soup.loc['9999', ['Name']] = ['soups_average']
soup.loc['9999', ['id']] = ['99999']
soup = soup.round(decimals=2)
soups_average = soup.tail(1)

apple.loc['9999'] = apple.mean()
apple.loc['9999', ['Name']] = ['apples_average']
apple.loc['9999', ['id']] = ['99999']
apple = apple.round(decimals=2)
apples_average = apple.tail(1)

apricot.loc['9999'] = apricot.mean()
apricot.loc['9999', ['Name']] = ['apricots_average']
apricot.loc['9999', ['id']] = ['99999']
apricot = apricot.round(decimals=2)
apricots_average = apricot.tail(1)

veggie.loc['9999'] = veggie.mean()
veggie.loc['9999', ['Name']] = ['veggies_average']
veggie.loc['9999', ['id']] = ['99999']
veggie = veggie.round(decimals=2)
veggies_average = veggie.tail(1)

nut.loc['9999'] = nut.mean()
nut.loc['9999', ['Name']] = ['nuts_average']
nut.loc['9999', ['id']] = ['99999']
nut = nut.round(decimals=2)
nuts_average = nut.tail(1)

chocolate.loc['9999'] = chocolate.mean()
chocolate.loc['9999', ['Name']] = ['chocolates_Average']
chocolate.loc['9999', ['id']] = ['99999']
chocolate = chocolate.round(decimals=2)
chocolates_average = chocolate.tail(1)

snack.loc['9999'] = snack.mean()
snack.loc['9999', ['Name']] = ['snacks_Average']
snack.loc['9999', ['id']] = ['99999']
snack = snack.round(decimals=2)
snacks_average = snack.tail(1)

dessert.loc['9999'] = dessert.mean()
dessert.loc['9999', ['Name']] = ['dessert_average']
dessert.loc['9999', ['id']] = ['99999']
dessert = dessert.round(decimals=2)
dessert_average = dessert.tail(1)

seasoning.loc['9999'] = seasoning.mean()
seasoning.loc['9999', ['Name']] = ['seasonings_average']
seasoning.loc['9999', ['id']] = ['99999']
seasoning = seasoning.round(decimals=2)
seasonings_average = seasoning.tail(1)

chinese_food.loc['9999'] = chinese_food.mean()
chinese_food.loc['9999', ['Name']] = ['chinese_foods_average']
chinese_food.loc['9999', ['id']] = ['99999']
chinese_food = chinese_food.round(decimals=2)
chinese_foods_average = chinese_food.tail(1)

sea_food.loc['9999'] = sea_food.mean()
sea_food.loc['9999', ['Name']] = ['sea_foods_average']
sea_food.loc['9999', ['id']] = ['99999']
sea_food = sea_food.round(decimals=2)
seafoods_average = sea_food.tail(1)

frozen_food.loc['9999'] = frozen_food.mean()
frozen_food.loc['9999', ['Name']] = ['frozen_foods_average']
frozen_food.loc['9999', ['id']] = ['99999']
frozen_food = frozen_food.round(decimals=2)
frozen_food_average = frozen_food.tail(1)

turkey.loc['9999'] = turkey.mean()
turkey.loc['9999', ['Name']] = ['turkeys_average']
turkey.loc['9999', ['id']] = ['99999']
turkey = turkey.round(decimals=2)
turkey_average = turkey.tail(1)

meats_list = [cow_average, turkey_average, pig_average, chicken_average, game_average, lamb_average, veal_average, emu_average, ostrich_average, duck_average, goose_average, fish_average]
              
# combine all the dataframes into one using concat
meat_averages = pd.concat(meats_list, ignore_index=True)
meat_averages = pd.DataFrame(meat_averages)
meat_averages.loc['9999'] = meat_averages.mean()
meat_averages.loc['9999', ['Name']] = ['meat_average']
meat_averages.loc['9999', ['id']] = ['99999']
meat_averages = meat_averages.round(decimals=2)
meat_average = meat_averages.tail(1)

pizza.loc['9999'] = pizza.mean()
pizza.loc['9999', ['Name']] = ['pizza_Average']
pizza.loc['9999', ['id']] = ['99999']
pizza = pizza.round(decimals=2)
pizza_average = pizza.tail(1)

margarine.loc['9999'] = margarine.mean()
margarine.loc['9999', ['Name']] = ['margarine_Average']
margarine.loc['9999', ['id']] = ['99999']
margarine = margarine.round(decimals=2)
margarine_average = margarine.tail(1)

canned_food.loc['9999'] = canned_food.mean()
canned_food.loc['9999', ['Name']] = ['canned_food_average']
canned_food.loc['9999', ['id']] = ['99999']
canned_food = canned_food.round(decimals=2)
canned_food_average = canned_food.tail(1)

#Create row for "low fat" milk with averages for all columns
lowfat_milk.loc['9998'] = lowfat_milk.mean()
lowfat_milk.loc['9998', ['Name']] = ['Low_Fat_Milk_Average']
lowfat_milk.loc['9998', ['id']] = ['99998']
lowfat_milk = lowfat_milk.round(decimals=2)

#Create row for all other milk with averages for all columns
other_milk.loc['9999'] = other_milk.mean()
other_milk.loc['9999', ['Name']] = ['Other_Milk_Average']
other_milk.loc['9999', ['id']] = ['99999']
other_milk = other_milk.round(decimals=2)