import pandas as pd

# Here are all of the foods we manually selected from the csv that we will be using for our food groups
food_group_dic = {"fruits": ["Bananas, raw", "Apples, with skin, f","Strawberries, raw","Grapes, raw, america","Oranges, with peel,","Watermelon, raw","Blueberries, raw",
"Lemons, without peel","Peaches, raw, yellow","Avocadoes, all commer","Pineapple, all varie","Cherries, raw, sweet",
"Melons, raw, cantalo","Pears, raw","Limes, raw","Raspberries, raw","Blackberries, raw","Clementine, raw","Plums, raw","Nectarines, raw","Apricots, raw"], 
"grains": ["Oats","Bagels, multigrain","Bread, italian","Rice, cooked medium","Rice, noodles, cooked","Cornstarch",
"Barley flour or meal","Bread, rye","Rye flour, medium","Quinoa, cooked","Cereals, dry, instan"], 
"proteins": ["Chicken, thigh meat ","Chicken breast, prep","Nuts, almonds","Nuts, pecans","Pork, cooked, lean a",
"Salami, beef, pork, ","Salami, pork, Italia","Ham, canned, chopped","Beef, raw, brisket, ","Beef, smoked, cooked",
"Sausage, pork, beef,","Egg, dried, white""Lentils, raw","Yogurt, nonfat milk,","Soybeans, raw, green","Pastrami, turkey",
"Nuts, raw, macadamia","Nuts, raw, pistachio","Nuts, raw, cashew nu","Ground turkey, raw"],
"vegetables": ["Broccoli, raw","Potatoes, skin, raw","Lettuce, raw, green","Soybeans, raw, green","Beans, raw, green, s",
"Mushrooms, raw, whit","Celery, raw","Eggplant, raw","Cauliflower, raw","Cabbage, kimchi","Asparagus, raw","Cucumber, raw, peele",
"Spinach, raw","Corn, raw, yellow, s","Mushrooms, raw, mait","Sweet potato, mashed","Onions, raw, spring ",
"Cabbage, raw, stored","Carrots, raw, baby","Tomatoes, raw, orang","Pepper, raw, banana","Peppers, raw, yellow","Kale, raw","Beets, raw"],
"dairy": ["Cheese, Mexican blen","Cheese, 1% milkfat,","Cheese, 2% milkfat,","Cheese, provolone","Cheese, cheddar",
"Cheese, monterey","Butter, salted","Ice cream cookie san","Milk, fluid, sheep","Milk, whole, fluid, ",
"Sour cream, fat free","Sour cream, light","Cheese, cream"]
}

nutrition_df = pd.read_csv('nutrition.csv')  

# keep only the macro and micro nutrients that we think will be most helpful
nutrition_df = nutrition_df[["name", "calories", "total_fat", "sodium", "protein", "carbohydrate", "sugars"]]

# take only the first five words of the name column, as there are a lot of long names with only one thing
# differentiating them and they have the same nutritional info
nutrition_df["name"] = nutrition_df["name"].str[:20]
nutrition_df = nutrition_df.drop_duplicates(subset ="name", keep = False)

# this will be the final dataframe with the food groups that we will use to export to a csv
food_groups_df = pd.DataFrame(columns=["food_group", "name", "calories", "total_fat", "sodium", "protein", "carbohydrate", "sugars"])


for group in food_group_dic:
    # create a temporary df for each food group, as it will make it easier to append everything in the end
    toAdd =  pd.DataFrame(columns=["name", "calories", "total_fat", "sodium", "protein", "carbohydrate", "sugars"])
    for food in food_group_dic[group]:
        print(food)
        # find each food and add it to the temporary df
        # nutrition_df.loc[nutrition_df['name'] == food]["food_group"] = group
        toAdd = toAdd.append(nutrition_df.loc[nutrition_df['name'] == food], ignore_index=True)

    # assign the food group
    toAdd["food_group"] = group
    food_groups_df = food_groups_df.append(toAdd)

food_groups_df.to_csv("nutrition.csv", index=False)
