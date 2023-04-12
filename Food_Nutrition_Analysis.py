#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
#ML
from prophet import Prophet
sns.set(font_scale=1.5)


# ## Read in data

# In[102]:


df = pd.read_csv('./data/ABBREV.csv')

# Convert the "Name" column to uppercase
df['Shrt_Desc'] = df['Shrt_Desc'].str.upper()
df = df.sort_values(by='Shrt_Desc', ascending=False)

# Write the modified data back to the CSV file
df.to_csv('./data/ABBREV.csv', index=False)

df['Total_Fat_(g)'] = df['FA_Mono_(g)'] + df['FA_Sat_(g)']
df = df[["NDB_No", "Shrt_Desc", "Energ_Kcal", "Protein_(g)", "Carbohydrt_(g)", "Fiber_TD_(g)", "Sugar_Tot_(g)", "Calcium_(mg)", "Sodium_(mg)", "Total_Fat_(g)"]].copy()
df = df.rename(columns={'Energ_Kcal':'Calories',  'Shrt_Desc':'Name', 'NDB_No':'id', 'Carbohydrt_(g)':'Carbs_(g)', 'Protein_(g)':'Protein_(g)', 'Fiber_TD_(g)':'Fiber_(g)', 'Sugar_Tot_(g)':'Sugar_(g)', 'Calcium_(mg)':'Calcium_(mg)', 'Sodium_(mg)':'Sodium_(mg)'})
df.head()


# In[3]:


#Create heatmap to check correlation in data
correlation = df[["Calories", 'Carbs_(g)', 'Protein_(g)', "Sugar_(g)", "Calcium_(mg)", "Total_Fat_(g)", "Sodium_(mg)"]].copy()
sns.set_theme(style="white")
corr = correlation.corr(method = 'pearson',  # The method of correlation
                  min_periods = 1 )
corr.style.background_gradient(cmap='coolwarm')


# #### Notes: It appears that there isn't any strong correlations between any of the fields. The highest is between calories and fat, then sugar and carbs.

# ## Cheese

# In[4]:


cheese = df[df["Name"].str.startswith("CHEESE,")]
cheese = cheese.sort_values(by='Calories', ascending=False)
#cheese.to_csv('./data/cheese.csv')


# In[5]:


sns.set_theme(style="white")
corr = cheese.corr(method = 'pearson',  # The method of correlation
                  min_periods = 1)
corr.style.background_gradient(cmap='coolwarm')


# In[6]:


#Scatter plot comparing Calories with Saturated Fat in Cheese
sns.set(rc={"figure.figsize":(20, 5)})
scatter = sns.scatterplot(data=cheese, x='Calories', y='Total_Fat_(g)', legend='auto', s=50)
scatter.set_title("Correlation between Calories and Saturated Fat in Cheese", fontdict={'size': 20, 'weight': 'bold'})
scatter.set_xlabel('Calories', fontdict={'size': 15})
scatter.set_ylabel('Total Fat (g)', fontdict={'size': 15})
plt.ylim(-2, 35)
plt.xlim(0, 500)
plt.show()


# ### Notes: Strong correlation between fat and calorie content in cheese

# ## Milk

# In[19]:


milk = df[df["Name"].str.startswith("MILK,")]
milk = milk.sort_values(by='Calories', ascending=False)
#milk.to_csv('./data/milks.csv')
milk.head()


# In[8]:


sns.set_theme(style="white")
corr = milk.corr(method = 'pearson', min_periods = 1)
corr.style.background_gradient(cmap='coolwarm')


# #### Notes: High correlation among many fields, especially sugar, protein, carbs, and calcium

# ### Are "lowfat milks" really low in fat?

# In[15]:


#milk = milk.sort_values(by='Saturated_Fat_(g)', ascending=False)
fat = ['NONFAT', 'FAT FREE', 'LOWFAT', 'LOW FAT', 'LO FAT']
pattern = '|'.join(fat)

lowfat_milk = milk[milk["Name"].str.contains(pattern)]
other_milk = milk[~milk["Name"].str.contains(pattern)]


# In[16]:


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

#Combine the two and compare
compare_milk = pd.concat([lowfat_milk.loc['9998'], other_milk.loc['9999']], axis=1)
compare_milk.rename(columns={'9998': 'Low_Fat_Milk_Average', '9999': 'Other_Milk_Average'}, inplace=True)

#drop first two rows
compare_milk = compare_milk.iloc[2:]
compare_milk


# ### Notes: The Low Fat Milk option does have less fat than other milks, as well as more protein and calcium. However, the calorie count remains similar among both

# # Soup

# In[83]:


soup_keywords = ['SOUP', 'CAMPBELL', 'SOUP', 'CHILI']
soup_pattern = '|'.join(soup_keywords)

not_soup = ['BROTH', 'BOUILLON', 'STOCK','GRAVY', 'MIX', 'ON THE GO', 'JUC', 'CRACKERS', 'SPAGHETTI']
not_soup_pattern = '|'.join(not_soup)

soups = df[df["Name"].str.contains(soup_pattern)]
soups = soups[~soups["Name"].str.contains(not_soup_pattern)]

soups = soups.sort_values(by='Calories', ascending=False)
#soups.to_csv('./data/soups.csv')


# ## Cereal

# In[42]:


cereal_keywords = ['CEREAL']
cereal_pattern = '|'.join(cereal_keywords)

cereals = df[df["Name"].str.contains(cereal_pattern)]

cereals = cereals.sort_values(by='Calories', ascending=False)
#cereals.to_csv('./data/cereals.csv')


# ## Cookies

# In[86]:


cookies_keywords = ['COOKIE', 'WAFER']
cookies_pattern = '|'.join(cookies_keywords)

not_cookies = ['ICE CRM']
not_cookies_pattern = '|'.join(not_cookies)

cookies = df[df["Name"].str.contains(cookies_pattern)]
cookies = cookies[~cookies["Name"].str.contains(not_cookies_pattern)]

cookies = cookies.sort_values(by='Calories', ascending=False)
#cookies.to_csv('./data/cookies.csv')


# In[105]:


babyfood_keywords = ['BABYFOOD', 'INF FORMULA']
babyfood_pattern = '|'.join(babyfood_keywords)

babyfoods = df[df["Name"].str.contains(babyfood_pattern)]

babyfoods = babyfoods.sort_values(by='Calories', ascending=False)
#babyfoods.to_csv('./data/babyfoods.csv')


# In[52]:


beans_keywords = ['BEANS']
beans_pattern = '|'.join(beans_keywords)

not_beans = ['CANDIES']
not_beans_pattern = '|'.join(not_beans)

beans = df[df["Name"].str.contains(beans_pattern)]
beans = beans[~beans["Name"].str.contains(not_beans_pattern)]

beans = beans.sort_values(by='Calories', ascending=False)
#beans.to_csv('./data/beans.csv')


# In[51]:


rice_keywords = ['RICE,']
rice_pattern = '|'.join(rice_keywords)

not_rice = ['CEREAL', 'CRACKERS', 'NOODLES', 'BABYFOOD', 'SOUP']
not_rice_pattern = '|'.join(not_rice)

rice = df[df["Name"].str.contains(rice_pattern)]
rice = rice[~rice["Name"].str.contains(not_rice_pattern)]

rice = rice.sort_values(by='Calories', ascending=False)
#rice.to_csv('./data/rices.csv')


# In[56]:


ice_cream_keywords = ['ICE_CREAM', 'ICE CREAM', 'ICECREAM', 'ICE CRM']
ice_cream_pattern = '|'.join(ice_cream_keywords)

not_ice_cream = ['POP-TART', 'COATING', 'CUP']
not_ice_cream_pattern = '|'.join(not_ice_cream)

ice_cream = df[df["Name"].str.contains(ice_cream_pattern)]
ice_cream = ice_cream[~ice_cream["Name"].str.contains(not_ice_cream_pattern)]

ice_cream = ice_cream.sort_values(by='Calories', ascending=False)
#ice_cream.to_csv('./data/ice_creams.csv')


# In[62]:


chips_keywords = ['CHIPS']
chips_pattern = '|'.join(chips_keywords)

chips = df[df["Name"].str.contains(chips_pattern)]

chips = chips.sort_values(by='Calories', ascending=False)
#chips.to_csv('./data/chips.csv')


# In[81]:


pasta_keywords = ['PASTA', 'SPAGHETTI', 'MACARONI']
pasta_pattern = '|'.join(pasta_keywords)

pasta = df[df["Name"].str.contains(pasta_pattern)]

pasta = pasta.sort_values(by='Calories', ascending=False)
#pasta.to_csv('./data/pasta.csv')


# In[77]:


fast_food_keywords = ['FASTFOOD', 'FAST FOOD', 'FAST FD', 'SUBWAY', 'MCDONALD', "WENDY'S", 'BURGER KING', "DOMINO'S", 'PIZZA HUT', 'KFC', 'POPEYE', 'DIGIORNO', "ARBY'S", 'CHICK-FIL-A', "CAESAR'S"]
fast_food_pattern = '|'.join(fast_food_keywords)

fast_food = df[df["Name"].str.contains(fast_food_pattern)]

fast_food = fast_food.sort_values(by='Calories', ascending=False)
#fast_food.to_csv('./data/fast_foods.csv')


# In[78]:


pizza_keywords = ['PIZZA']
pizza_pattern = '|'.join(pizza_keywords)

not_pizza = ['CRACKER', 'BREADSTICK']
not_pizza_pattern = '|'.join(not_pizza)

pizza = df[df["Name"].str.contains(pizza_pattern)]
pizza = pizza[~pizza["Name"].str.contains(not_pizza_pattern)]

pizza = pizza.sort_values(by='Calories', ascending=False)
#pizza.to_csv('./data/pizzas.csv')


# In[79]:


school_lunch_keywords = ['SCHOOL']
school_lunch_pattern = '|'.join(school_lunch_keywords)

school_lunch = df[df["Name"].str.contains(school_lunch_pattern)]

school_lunch = school_lunch.sort_values(by='Calories', ascending=False)
#school_lunch.to_csv('./data/school_lunches.csv')


# In[85]:


beef_keywords = ['BEEF,', 'BF,']
beef_pattern = '|'.join(beef_keywords)

not_beef = ['SOUP']
not_beef_pattern = '|'.join(not_beef)

beef = df[df["Name"].str.contains(beef_pattern)]
beef = beef[~beef["Name"].str.contains(not_beef_pattern)]

beef = beef.sort_values(by='Calories', ascending=False)
#beef.to_csv('./data/beef.csv')


# In[95]:


bread_keywords = ['BREAD,']
bread_pattern = '|'.join(bread_keywords)

not_bread = ['SOUP', 'SHORTENING', 'COOKIE', 'PIE', 'CAKE', 'FRIED', 'CRUMBS', 'MIX']
not_bread_pattern = '|'.join(not_bread)

bread = df[df["Name"].str.contains(bread_pattern)]
bread = bread[~bread["Name"].str.contains(not_bread_pattern)]

bread = bread.sort_values(by='Calories', ascending=False)
#bread.to_csv('./data/breads.csv')


# In[97]:


fish_keywords = ['FISH', 'COD', 'FRESHWATER', 'SALTWATER', 'BASS', 'CAVIAR', 'EEL', 'GROUPER', 'HADDOCK', 'HERRING', 'MACKEREL', 'PERCH', 'MULLET', 'TUNA', 'POMPANO',  'SALMON', 'SHARK', 'TROUT']
fish_pattern = '|'.join(fish_keywords)

not_fish = ['CRACKERS']
not_fish_pattern = '|'.join(not_fish)

fish = df[df["Name"].str.contains(fish_pattern)]
fish = fish[~fish["Name"].str.contains(not_fish_pattern)]

fish = fish.sort_values(by='Calories', ascending=False)
#fish.to_csv('./data/fish.csv')


# In[98]:


candy_keywords = ['CANDY', 'CANDIES']
candy_pattern = '|'.join(candy_keywords)

candy = df[df["Name"].str.contains(candy_pattern)]

candy = candy.sort_values(by='Calories', ascending=False)
#candy.to_csv('./data/candy.csv')


# In[137]:


beverage_keywords = ['BEVERAGE', 'BEV,']
beverage_pattern = '|'.join(beverage_keywords)

beverage = df[df["Name"].str.contains(beverage_pattern)]

beverage = beverage.sort_values(by='Calories', ascending=False)
#beverage.to_csv('./data/beverages.csv')


# In[101]:


dressing_keywords = ['DRSNG']
dressing_pattern = '|'.join(dressing_keywords)

dressing = df[df["Name"].str.contains(dressing_pattern)]

dressing = dressing.sort_values(by='Calories', ascending=False)
#dressing.to_csv('./data/dressings.csv')


# In[103]:


egg_keywords = ['EGG,']
egg_pattern = '|'.join(egg_keywords)

egg = df[df["Name"].str.contains(egg_pattern)]

egg = egg.sort_values(by='Calories', ascending=False)
#egg.to_csv('./data/eggs.csv')


# In[104]:


yogurt_keywords = ['YOGURT,']
yogurt_pattern = '|'.join(yogurt_keywords)

yogurt = df[df["Name"].str.contains(yogurt_pattern)]

yogurt = yogurt.sort_values(by='Calories', ascending=False)
#yogurt.to_csv('./data/yogurts.csv')


# In[106]:


oil_keywords = ['OIL,']
oil_pattern = '|'.join(oil_keywords)

oil = df[df["Name"].str.contains(oil_pattern)]

oil = oil.sort_values(by='Calories', ascending=False)
#oil.to_csv('./data/oils.csv')


# In[108]:


cake_keywords = ['CAKE', 'SHORTENING']
cake_pattern = '|'.join(cake_keywords)

cake = df[df["Name"].str.contains(cake_pattern)]

cake = cake.sort_values(by='Calories', ascending=False)
#cake.to_csv('./data/cakes.csv')


# In[112]:


butter_keywords = ['BUTTER,', 'MARGARINE']
butter_pattern = '|'.join(butter_keywords)

not_butter = [ 'COOKIE']
not_butter_pattern = '|'.join(not_butter)

butter = df[df["Name"].str.contains(butter_pattern)]
butter = butter[~butter["Name"].str.contains(not_butter_pattern)]

butter = butter.sort_values(by='Calories', ascending=False)
#butter.to_csv('./data/butters.csv')


# In[131]:


chicken_keywords = ['CHICKEN', 'POULTRY', 'CHCKN']
chicken_pattern = '|'.join(chicken_keywords)

chicken = df[df["Name"].str.contains(chicken_pattern)]

chicken = chicken.sort_values(by='Calories', ascending=False)
#chicken.to_csv('./data/chickens.csv')


# In[126]:


duck_keywords = ['DUCK,']
duck_pattern = '|'.join(duck_keywords)

not_duck = ['SOUP']
not_duck_pattern = '|'.join(not_duck)

duck = df[df["Name"].str.contains(duck_pattern)]
duck = duck[~duck["Name"].str.contains(not_duck_pattern)]

duck = duck.sort_values(by='Calories', ascending=False)
#duck.to_csv('./data/ducks.csv')


# In[127]:


goose_keywords = ['GOOSE,']
goose_pattern = '|'.join(goose_keywords)

not_goose = ['SOUP']
not_goose_pattern = '|'.join(not_goose)

goose = df[df["Name"].str.contains(goose_pattern)]
goose = goose[~goose["Name"].str.contains(not_goose_pattern)]

goose = goose.sort_values(by='Calories', ascending=False)
#goose.to_csv('./data/gooses.csv')


# In[130]:


emu_keywords = ['EMU,']
emu_pattern = '|'.join(emu_keywords)

not_emu = ['BABYFOOD', 'SOUP']
not_emu_pattern = '|'.join(not_emu)

emu = df[df["Name"].str.contains(emu_pattern)]
emu = emu[~emu["Name"].str.contains(not_emu_pattern)]

emu = emu.sort_values(by='Calories', ascending=False)
#emu.to_csv('./data/emus.csv')


# In[129]:


ostrich_keywords = ['OSTRICH,']
ostrich_pattern = '|'.join(ostrich_keywords)

not_ostrich = ['BABYFOOD', 'SOUP']
not_ostrich_pattern = '|'.join(not_ostrich)

ostrich = df[df["Name"].str.contains(ostrich_pattern)]
ostrich = ostrich[~ostrich["Name"].str.contains(not_ostrich_pattern)]

ostrich = ostrich.sort_values(by='Calories', ascending=False)
#ostrich.to_csv('./data/ostrichs.csv')


# In[135]:


cow_keywords = ['STEAK,', 'BEEF,']
cow_pattern = '|'.join(cow_keywords)

cow = df[df["Name"].str.contains(cow_pattern)]

cow = cow.sort_values(by='Calories', ascending=False)
#cow.to_csv('./data/cows.csv')


# In[136]:


pig_keywords = ['PORK,', 'SAUSAGE,', 'HAM,']
pig_pattern = '|'.join(pig_keywords)

pig = df[df["Name"].str.contains(pig_pattern)]

pig = pig.sort_values(by='Calories', ascending=False)
#pig.to_csv('./data/pigs.csv')


# In[138]:


lamb_keywords = ['LAMB,']
lamb_pattern = '|'.join(lamb_keywords)

lamb = df[df["Name"].str.contains(lamb_pattern)]

lamb = lamb.sort_values(by='Calories', ascending=False)
#lamb.to_csv('./data/lambs.csv')


# In[134]:


gravy_keywords = ['GRAVY,']
gravy_pattern = '|'.join(gravy_keywords)

not_gravy = ['SOUP']
not_gravy_pattern = '|'.join(not_gravy)

gravy = df[df["Name"].str.contains(gravy_pattern)]
gravy = gravy[~gravy["Name"].str.contains(not_gravy_pattern)]

gravy = gravy.sort_values(by='Calories', ascending=False)
#gravy.to_csv('./data/gravy.csv')


# In[139]:


veal_keywords = ['VEAL,']
veal_pattern = '|'.join(veal_keywords)

veal = df[df["Name"].str.contains(veal_pattern)]

veal = veal.sort_values(by='Calories', ascending=False)
#veal.to_csv('./data/veal.csv')


# In[140]:


game_keywords = ['GAME MEAT,']
game_pattern = '|'.join(game_keywords)

game = df[df["Name"].str.contains(game_pattern)]

game = game.sort_values(by='Calories', ascending=False)
#game.to_csv('./data/game.csv')


# In[141]:


pie_keywords = ['PIE,']
pie_pattern = '|'.join(pie_keywords)

pie = df[df["Name"].str.contains(pie_pattern)]

pie = pie.sort_values(by='Calories', ascending=False)
#pie.to_csv('./data/pies.csv')


# In[142]:


pudding_keywords = ['PUDDING']
pudding_pattern = '|'.join(pudding_keywords)

pudding = df[df["Name"].str.contains(pudding_pattern)]

pudding = pudding.sort_values(by='Calories', ascending=False)
#pudding.to_csv('./data/puddings.csv')


# In[ ]:


#nuts
#veggies
#fruits

