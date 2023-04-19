# Food_Nutrition_Analysis
Data Science project analysing the nutritional facts of various food items and groups. I got the attached data set ABBREV.csv from data world, found here: https://data.world/awram/food-nutritional-values. I wanted to conduct this project to see if my and others' views on the nutritional value of food and food groups is accurate. What I found was generally expected save for a few surprising results here and there. You can see the results by downloading and reading the PDF report Food_Nutrition_Analysis_Report.pdf in the repository. You can check my work by observing my Jupyter Notebook and my data prep python file.

In the performance of this project, I needed to do the following:
1. Convert nutrients amounts to a common unit. Nutrients ranged from grams to milligrams to micrograms. I decided it best to convert everything to milligrams and go from there.
2. Calculate a "Health Score" for each food. This score was calculated by subtracting "unhealthy" nutrients from "healthy" nutrients, then dividing by the weight of the food. Down below, I left some reasons for why I classified each nutrients in the data set as either "healthy" or "unhealthy".
3. Divide foods into their food groups. For example, I needed to find all of the canned foods that were in the data set, so I filtered the data into one data frame that only includes the nutritional facts on any foods with the word "CANNED" in it.
4. Calculate the average Health Score for every food group and compare to others.


The reason the following I considered "healthy" nutrients:

Water: essential for hydration and bodily functions such as temperature regulation, digestion, and nutrient transport
Protein: important for building and repairing tissues, producing enzymes and hormones, and supporting the immune system
Fiber: aids in digestion, promotes satiety, and can help lower cholesterol and blood sugar levels
Calcium: important for building and maintaining strong bones and teeth, and also plays a role in nerve function and muscle contraction
Iron: essential for the production of red blood cells and hormone creation
Magnesium: involved in over 300 reactions in the body, including muscle and nerve function, regulating blood sugar levels, and supporting the immune system
Phosphorus: important for building and maintaining strong bones and teeth, and also plays a role in energy production and DNA repair
Potassium: helps regulate fluid balance, muscle contractions, and nerve signals, and can also help lower blood pressure
Sodium: important for fluid balance and nerve function, but excess intake can lead to high blood pressure and other negative health effects
Zinc: important for immune system function, wound healing, and DNA synthesis
Copper: plays a role in iron metabolism, immune system function, and nerve function
Manganese: involved in bone formation, wound healing, and metabolism
Selenium: important for thyroid function and antioxidant protection
Thiamin (B1), Riboflavin (B2), Niacin (B3), Folate_Tot, Folic_Acid, Food_Folate, Folate, Retinol, Alpha_Carot, Beta_Carot, Beta-Crypt, Lycopene: all vitamins that play important roles in bodily functions such   as energy production, DNA synthesis, and immune system function

I left carbohydrates out of the "healthy" nutrients list because, while technically they provide energy to the brain and body, they have a negative effect with an excessive quantity. Also, they were skewing my results too far in favor of foods with an excess quantity, like cereal.

Here is why I considered the following "unhealthy" nutrients:
Sugar: Consuming too much sugar can lead to health problems such as a lower level of "good" cholesterol and an increase in "bad" cholesterol. This is especially true of some sugars, such as refined fructose or sucrose, as opposed to other sugars, such as glucose.
Lipids: Consuming too much lipid can lead to health problems such as obesity, high blood pressure, and heart disease. High levels of LDL cholesterol, which is a type of lipid, can build up in the walls of your arteries and clog them, raising your chances for a heart attack or a stroke.
Cholesterol: Consuming too much dietary cholesterol can lead to an imbalance of cholesterol levels.
Saturated fat: Consuming too much saturated fat can lead to health problems such as high cholesterol, heart disease, and stroke. The American Heart Association recommends limiting saturated fat intake to less than 6% of daily calories.

Thanks for reading!
