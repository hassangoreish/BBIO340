# -*- coding: utf-8 -*-
"""
Created on Tue Jul  2 14:43:46 2024

@author: hggor
"""
#Starting off by importing pandas to analyze my data
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('occ_data.csv')

column_names = data.columns.tolist()
data['lithology1'] = data['lithology1'].str.replace('"','')
#This line will remove quotation marks from the lithology column in order for it to become more legible



lithology_column = 'lithology1'
species_column = 'accepted_name'
row_index = [0, 516223]

species_name = data.loc[4,species_column]
lithology_type = data.loc[5,lithology_column]
species_count = len(data['accepted_name'])
print(f"The number of species in our data is:{species_count}.")

#^This line counts the total number of species in my data sample

print(f"This species name is {species_name} and it was fossilized in {lithology_type}.")
#This series of lines will select specific species and lithology from the data

#for index, row in data.iterrows():
    #print(row[species_column], row[lithology_column])

lithology_types = set(data['lithology1'])
print(f"Here are all the lithology types in our dataset:{lithology_types}.")
#This line shows me all the different types of lithology in my data

fossil_geo = data.groupby('lithology1')['accepted_name'].count()
#This line groups the number of individuals found in each type of lithology
top_8_lithology = fossil_geo.sort_values(ascending=False).head(12)
top_8_lithology.plot(kind='bar', color ='red')
plt.xlabel('Lithology', fontsize=13)
plt.ylabel('Number of specimens', fontsize=13)
plt.title('The Most Common types of lithology for Mesozoic Fossils')

plt.show()

