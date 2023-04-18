#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')
sns.set(font_scale=1.5)
sns.set(rc={"figure.figsize":(40, 10)})


# ## Read in data

# In[2]:


# Prepare the data. This script fixes the ABBREV.csv file and pulls the foods into their respective food groups
get_ipython().run_line_magic('run', 'data_prep.py')


# In[26]:


averages_list = [water_average, meat_average, canned_food_average, frozen_food_average, seafoods_average, seasonings_average, dessert_average, fruits_average, cheeses_average, milks_average, cereals_average, babyfoods_average, beans_average, rice_average, pasta_average, fast_food_average, pizza_average, school_lunches_average, bread_average, fish_average, na_beverages_average, alcoholic_beverages_average, dressings_average, oils_average, butter_average, gravy_average, veggies_average, nuts_average, snacks_average]

# combine all the dataframes into one using concat
all_averages = pd.concat(averages_list, ignore_index=True)

all_averages = all_averages.sort_values(by='Health_Score', ascending=False)
all_averages['Name'] = all_averages['Name'].str.replace('_Average', '')
all_averages['Name'] = all_averages['Name'].str.replace('_average', '')
all_averages = all_averages.drop('id', axis=1)
all_averages


# In[4]:


#Create bar graph of Health Scores by Food/Food Group

nutrition_barplot = sns.barplot(x=all_averages['Name'], y = all_averages['Health_Score'])
nutrition_barplot.set_ylabel('Health Score')
nutrition_barplot.set_xlabel('Food/Food Type')
nutrition_barplot.set_title('Health Score by Food/Food Group', fontdict={'size': 30, 'weight': 'bold'})
nutrition_barplot.set_xticklabels(nutrition_barplot.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[5]:


#Create bar graph of Fat by Food/Food Group

all_averages = all_averages.sort_values(by='Total_Fat_(mg)', ascending=False)
nutrition_barplot = sns.barplot(x=all_averages['Name'], y = all_averages['Total_Fat_(mg)'])
nutrition_barplot.set_ylabel('Fat (mg)')
nutrition_barplot.set_xlabel('Food/Food Type')
nutrition_barplot.set_title('Fat per Food or Food Group', fontdict={'size': 30, 'weight': 'bold'})
nutrition_barplot.set_xticklabels(nutrition_barplot.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# In[6]:


#Create bar graph of Calories by Food/Food Group

all_averages = all_averages.sort_values(by='Calories', ascending=False)
nutrition_barplot = sns.barplot(x=all_averages['Name'], y = all_averages['Calories'])
nutrition_barplot.set_ylabel('Calories (kcal)')
nutrition_barplot.set_xlabel('Food/Food Type')
nutrition_barplot.set_title('Calories per Food or Food Group', fontdict={'size': 30, 'weight': 'bold'})
nutrition_barplot.set_xticklabels(nutrition_barplot.get_xticklabels(), rotation=45, horizontalalignment='right')
plt.show()


# ## Top 5 foods by Health Score

# In[7]:


df = df.sort_values(by='Health_Score', ascending=False)
top_health_score = df.loc[:, ['Name', 'Calories', 'Healthy_Nutrients', 'Unhealthy_Nutrients', 'Health_Score']]
top_health_score.head(10)


# ## Bottom 5 foods by Health Score

# In[8]:


top_health_score.tail(10)


# In[9]:


#Create heatmap to check correlation in data
correlation = df[["Calories", 'Carbs_(mg)', 'Protein_(mg)', "Sugar_(mg)", "Calcium_(mg)", "Total_Fat_(mg)", "Sodium_(mg)", "Potassium_(mg)", "Water_(mg)", 'Vitamins_(mg)', 'Health_Score']].copy()
sns.set_theme(style="white")
corr = correlation.corr(method = 'pearson', min_periods = 1 )
corr.style.background_gradient(cmap='coolwarm')


# #### Notes: It appears that there isn't any strong correlations between any of the fields except Water's negative correlation with Calories. The highest positive correlation is between calories and fat, then sugar and carbs.

# In[10]:


#Scatter plot comparing Calories with Fat
sns.set(rc={"figure.figsize":(20, 5)})
scatter = sns.scatterplot(data=df, x='Calories', y='Total_Fat_(mg)', legend='auto', s=50)
scatter.set_title("Correlation between Calories and Fat", fontdict={'size': 20, 'weight': 'bold'})
scatter.set_xlabel('Calories', fontdict={'size': 15})
scatter.set_ylabel('Total Fat (mg)', fontdict={'size': 15})
plt.show()


# In[11]:


#Scatter plot comparing sugar and carbs
sns.set(rc={"figure.figsize":(20, 5)})
scatter = sns.scatterplot(data=df, x='Sugar_(mg)', y='Carbs_(mg)', legend='auto', s=50)
scatter.set_title("Correlation between Sugar and Carbs", fontdict={'size': 20, 'weight': 'bold'})
scatter.set_xlabel('Sugar', fontdict={'size': 15})
scatter.set_ylabel('Carbs (mg)', fontdict={'size': 15})
plt.show()


# In[12]:


#Scatter plot comparing Calories with Fat
sns.set(rc={"figure.figsize":(20, 5)})
scatter = sns.scatterplot(data=df, x='Calories', y='Health_Score', legend='auto', s=50)
scatter.set_title("Correlation between Calories and Health Score", fontdict={'size': 20, 'weight': 'bold'})
scatter.set_xlabel('Calories', fontdict={'size': 15})
scatter.set_ylabel('Health Score', fontdict={'size': 15})
plt.ylim(-100000, 250000)
plt.show()


# ## Milk vs Cheese vs Butter

# In[13]:


#combine averages and transpose the data
mk_ch_btr_averages = pd.concat([milks_average, cheeses_average, butter_average])
mk_ch_btr_averages = mk_ch_btr_averages.transpose()
mk_ch_btr_averages.columns = ('Milk', 'Cheese', 'Butter')

#drop first two rows
mk_ch_btr_averages = mk_ch_btr_averages.iloc[2:]
mk_ch_btr_averages


# #### Notes: Milk has the highest health score, followed by Cheese in a close second and Butter in a distant third. Butter has by far the highest calories.

# ## Analyze Milk: Are "lowfat milks" really low in fat?

# In[14]:


#Combine the two and compare
compare_milk = pd.concat([lowfat_milk.loc['9998'], other_milk.loc['9999']], axis=1)
compare_milk.rename(columns={'9998': 'Low_Fat_Milk_Average', '9999': 'Other_Milk_Average'}, inplace=True)

#drop first two rows
compare_milk = compare_milk.iloc[2:]
compare_milk


# #### Notes: The Low Fat Milk option does have less fat than other milks, but it also has a lower health score and more calories.

# ## Butter vs Margarine

# In[15]:


#combine averages and transpose the data
butter_margarine_averages = pd.concat([butter_average, margarine_average])
butter_margarine_averages = butter_margarine_averages.transpose()
butter_margarine_averages.columns = ('Butter', 'Margarine')

#drop first two rows
butter_margarine_averages = butter_margarine_averages.iloc[2:]
butter_margarine_averages


# #### Notes: Margarine has a MUCH higher health score, but also more calories compared to Butter. Butter also has less fat and much more protein.

# ## Compare Fruits and Veggies

# In[16]:


#combine averages and transpose the data
fruits_veggies_averages = pd.concat([fruits_average, veggies_average])
fruits_veggies_averages = fruits_veggies_averages.transpose()
fruits_veggies_averages.columns = ('Fruits', 'Veggie')

#drop first two rows
fruits_veggies_averages = fruits_veggies_averages.iloc[2:]
fruits_veggies_averages


# #### Notes: Veggies tend to be lower in calories, carbs, sugar, and fat, while much higher in Sodium and Vitamins compared to Fruit. Fruit has a slightly higher Health Score.

# ## Compare Meats

# In[25]:


meat_averages = meat_averages.drop('id', axis=1)
meat_averages


# #### Notes: Ostrich and Goose have the highest Health Scores, Chicken contains the most calories, Game and Emu contain the most protein, Lamb contains the most fat, Pig contains (by far) the most sodium, and fish contains the most vitamins and potassium.

# ## Compare Alcoholic Beverages, Non-Alcohol Beverages, and Water

# In[18]:


#combine averages and transpose the data
beverage_averages = pd.concat([na_beverages_average, alcoholic_beverages_average, water_average])
beverage_averages = beverage_averages.transpose()
beverage_averages.columns = ('Non-Alcoholic Beverages', 'Alcoholic Beverages', 'Water')

#drop first two rows
beverage_averages = beverage_averages.iloc[2:]
beverage_averages


# #### Notes: Non-Alcoholic Beverages have a higher Health Score, but generally have more carbs and sugar, while Alcoholic Beverages have more calories and sodium.

# ## Compare Baby Food, fast Food, Frozen Foods, Canned Foods, and School Lunches

# In[19]:


#combine averages and transpose the data
bf_ff_sl_averages = pd.concat([babyfoods_average, fast_food_average, frozen_food_average, canned_food_average, school_lunches_average])
bf_ff_sl_averages = bf_ff_sl_averages.transpose()
bf_ff_sl_averages.columns = ('Baby Foods', 'Fast Foods', 'Frozen Foods', 'Canned Food', 'School Lunches')

#drop first two rows
bf_ff_sl_averages = bf_ff_sl_averages.iloc[2:]
bf_ff_sl_averages


# #### Notes: Canned foods have by far the highest health score, followed by School Lunches. Nutrients in Fast food and School Lunches are comparable on all metrics but calcium, while baby foods are lowest in most metrics, but very high in vitamins

# ## Chinese Food vs Sea Food vs Pasta vs Pizza

# In[20]:


#combine averages and transpose the data
cf_sf_pas_pz_averages = pd.concat([chinese_foods_average, seafoods_average, pasta_average, pizza_average])
cf_sf_pas_pz_averages = cf_sf_pas_pz_averages.transpose()
cf_sf_pas_pz_averages.columns = ('Chinese Food', 'Sea Food', 'Pasta', 'Pizza')

#drop first two rows
cf_sf_pas_pz_averages = cf_sf_pas_pz_averages.iloc[2:]
cf_sf_pas_pz_averages


# #### Notes: Sea Food has easily the highest health score and lowest calories. Chinese Food and Pasta are close for second place, while Pizza is in a distant last.

# ## Desserts vs Snacks vs Cereal

# In[21]:


#combine averages and transpose the data
des_snck_averages = pd.concat([dessert_average, snacks_average, cereals_average])
des_snck_averages = des_snck_averages.transpose()
des_snck_averages.columns = ('Desserts', 'Snacks', 'Cereal')

#drop first two rows
des_snck_averages = des_snck_averages.iloc[2:]
des_snck_averages


# #### Notes: Desserts have the highest health score, while cereal has the lowest calories.

# ## Dressings vs Oils vs Seasonings vs Gravy

# In[22]:


#combine averages and transpose the data
drs_oil_ssngs_averages = pd.concat([dressings_average, oils_average, seasonings_average, gravy_average])
drs_oil_ssngs_averages = drs_oil_ssngs_averages.transpose()
drs_oil_ssngs_averages.columns = ('Dressings', 'Oils', 'Seasonings', 'Gravy')

#drop first two rows
drs_oil_ssngs_averages = drs_oil_ssngs_averages.iloc[2:]
drs_oil_ssngs_averages


# #### Notes: Dressings have the highest health score, Gravy has the lowest calories, Oils has by far the highest calories.

# ## Nuts vs Bread vs Beans

# In[23]:


#combine averages and transpose the data
nts_brd_bns_averages = pd.concat([nuts_average, bread_average, beans_average])
nts_brd_bns_averages = nts_brd_bns_averages.transpose()
nts_brd_bns_averages.columns = ('Nuts', 'Bread', 'Beans')

#drop first two rows
nts_brd_bns_averages = nts_brd_bns_averages.iloc[2:]
nts_brd_bns_averages


# #### Notes: Beans have by far the highest health score, followed by Nuts in second and Bread in a distant third. Nuts have by far the most calories, but also the most protein. Beans seem to be high in vitamins.

# ## Compare EVERYTHING

# In[24]:


averages_list = [milks_average, water_average, canned_food_average, fruits_average, cheeses_average, soups_average, cereals_average, cookies_average, babyfoods_average, beans_average, rice_average, ice_creams_average, chips_average, pasta_average, fast_food_average, school_lunches_average, bread_average, fish_average, candy_average, na_beverages_average, alcoholic_beverages_average, dressings_average, yogurts_average, oils_average, cake_average, butter_average, chicken_average, duck_average, goose_average, ostrich_average, emu_average, cow_average, pig_average, lamb_average, veal_average, game_average, gravy_average, pie_average, pudding_average, soups_average, apples_average, apricots_average, veggies_average, nuts_average, chocolates_average, snacks_average, dessert_average, seasonings_average, chinese_foods_average, seafoods_average, frozen_food_average, turkey_average, meat_average, pizza_average, margarine_average,]

#combine all the dataframes into one using concat
all_averages = pd.concat(averages_list, ignore_index=True)

all_averages = all_averages.sort_values(by='Health_Score', ascending=False)
all_averages['Name'] = all_averages['Name'].str.replace('_average', '')
all_averages['Name'] = all_averages['Name'].str.replace('_Average', '')

#Create bar graph of top ten Countries by coffee consumption
sns.set(rc={"figure.figsize":(40, 10)})
nutrition_barplot = sns.barplot(x=all_averages['Name'], y = all_averages['Health_Score'])
nutrition_barplot.set_ylabel('Health Score')
nutrition_barplot.set_xlabel('Food/Food Type')
nutrition_barplot.set_title('Health Score by Every Food/Food Group', fontdict={'size': 30, 'weight': 'bold'})
nutrition_barplot.set_xticklabels(nutrition_barplot.get_xticklabels(), rotation=45, horizontalalignment='right')
#plt.ylim(0,50000)
plt.show()


# #### Notes: Unsurprising results, with health score near the top being water, live animal products high in protein, then vegetables and fruits. Toward the middle and lower parts, you have manufactured products like beverages, dressings/condiments, frozen and baby foods, pasta, and alcohol. You also have animal byproducts like milk, cheese, and margarine. Leading towards the bottom of health scores, you have fast food and school lunches, pizza, oils, seasonings, rice, sweets. and various snacks.
