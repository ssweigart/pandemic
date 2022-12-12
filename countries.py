#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 22:07:10 2022

@author: sarahsweigart
"""

file1 = open('countries_on_the_grid.txt', 'r')
a = file1.readlines()
print(a)
file1.close()

tokeep = []
for its in range(len(a)):
    if a[its] != '\n':
        tokeep.append(its)

a = [a[i] for i in tokeep]
        
        

All_countries = []

"""
for linz in range(len(a)):
    starting_number = int(a[linz][0])
    restOfTheLine = a[linz][2:]
    restOfTheLine = restOfTheLine.replace('\n', '')
    these_countries = restOfTheLine.split(',')
    All_countries  = All_countries + these_countries * starting_number
    
print(All_countries)
    
file1.close()
  """  

#now we add a new one
newCities = ['Davis','Newark','Eugene']
Cubes = [4,0,1]

allNums = []

for linz in range(len(a)):
    starting_number = int(a[linz][0])
    allNums.append(starting_number)


for item in range(len(newCities)):
    if Cubes[item] in allNums:
        location = allNums.index(Cubes[item])
        newline = a[location].split('\n')
        a[location] = newline[0] + ',' + newCities[item] + '\n'
        
    elif Cubes[item] > max(allNums):
        a.insert(0, str(Cubes[item]) + ' ' + newCities[item] + '\n')
        allNums.insert(0, Cubes[item])
    elif Cubes[item] < min(allNums):
        a.append( str(Cubes[item]) + ' ' + newCities[item]+ '\n')
        allNums.append(Cubes[item])
        
        
        
file1 = open('countries_on_the_grid.txt', 'w')
file1.writelines(a)
file1.close()
        
        
        
    






