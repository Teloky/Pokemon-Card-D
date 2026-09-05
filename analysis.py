import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df = pd.read_csv("Pokemon.csv")

#All Pokemon
sns.regplot(data=df, x="Attack", y="Speed")
ax = sns.scatterplot(data=df, x="Attack", y="Speed", hue = "Type 1")
sns.move_legend(ax,"upper left", bbox_to_anchor=(1,1))
plt.savefig("All Pokemon")

#Pokemon that have a second type
plt.figure()
df_type2 = df[df["Type 2"].notna()]
sns.regplot(data=df_type2, x="Attack", y="Speed")
meow = sns.scatterplot(data=df_type2, x="Attack", y="Speed", hue = "Type 2")
sns.move_legend(meow, "upper left", bbox_to_anchor=(1,1))
plt.savefig("Di type")

#Pokemone that only have one typying
plt.figure()
df_type1 = df[df["Type 2"].isna()]
sns.regplot(data=df_type1, x="Attack", y="Speed")
dog = sns.scatterplot(data=df_type1, x="Attack", y="Speed", hue = "Type 1")
sns.move_legend(dog, "upper left", bbox_to_anchor=(1,1))
plt.savefig("Mono type only")

#Legendary Pokemon

plt.figure()
df_leg = df[(df["Legendary"] == True) & (~df["Name"].str.contains("Mega"))]
sns.regplot(data = df_leg, x="#", y="Total")
plt.savefig("Generation Legendary Line")

plt.figure()
df_leg = df[(df["Legendary"] == True) & (~df["Name"].str.contains("Mega"))]
sns.boxplot(data = df_leg, x="Generation", y="Total")
plt.savefig("Generation Legendary Box")