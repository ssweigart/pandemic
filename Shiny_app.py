#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  8 19:15:47 2022

@author: sarahsweigart
"""

import pickle
#function

def checkList(country, listToCompare):
    while country not in listToCompare:
        print(listToCompare)
        country = input('Are you sure you spelled it right?:')
    return(country)







cities = ['London','New York','Washington','Jacksonville','Sao Paulo','Lagos','Tripoli','Cairo','Istanbul']

newCities = ['Chicago','Denver','San Francisco']

lowCities = ['Atlanta']



all_infection_cards = cities + cities + cities + newCities + newCities + lowCities
max_deck = all_infection_cards[:]

current_deck = []


MaxPulled_Cards= []
Available_Cards = []
This_pandemics_Cards = []

MaxCardsPulled = []

restart = input('is this a restart?')




 



if restart == 'Yes':
    epidemic = input('how many epidemics?: ')
    with open('Pandemic_order.txt', 'rb') as f:
        saved_info = pickle.load(f)
        current_deck = saved_info[0]
        current_structure  = saved_info[1]
        print(current_deck)
        print(current_structure)
        file = open('Pandemic_order.txt', 'wb')
        pickle.dump([current_deck, current_structure], file)
        
else:
    file = open('Pandemic_order.txt', 'wb')
    for infect in range(3):
        apull = input('What city has been pulled as the '+str(infect+1) + ' card?:')
        apull = checkList(apull, max_deck)
        current_deck.append(apull)
        max_deck.remove(apull)
        print(current_deck)
        print(max_deck)
        current_structure = max_deck
        epidemic = 0
        file = open('Pandemic_order.txt', 'wb')
        pickle.dump([current_deck, current_structure], file)
        


#Here is where the game starts
for rounds in range(150):
    print(' Epidemic: ' +str(epidemic+1))
    newcountry = input('What city has been pulled?: ')
    #okay if its the beginning of the game just start the first split of the deck
    if newcountry == 'Epidemic' and epidemic == 0:
        #add the bottom card
        bad_news = input('What city is on the bottom of the deck?:')
        bad_news = checkList(bad_news, max_deck)
        current_deck.append(bad_news)
        max_deck.remove(bad_news)
        #now structure the data anew!
        epidemic = epidemic + 1
        current_structure = [current_deck, max_deck]
        current_deck = []
        pickle.dump([current_deck, current_structure], file)
        
        print(':O')
    elif newcountry == 'End':
        results = input('Game over! Did you win?')
        pickle.dump([current_deck, current_structure], file)
        file.close()
        break
        
    elif epidemic == 0:
        newcountry = checkList(newcountry, max_deck)
        current_deck.append(newcountry)
        max_deck.remove(newcountry)
        pickle.dump([current_deck, max_deck], file)
        print('This is a fresh Pull')
        
        
        
        
    elif newcountry == 'Epidemic':
        
        #add the bottom card
        bad_news = input('What city is on the bottom of the deck?:')
        bad_news = checkList(bad_news, max_deck)
        current_deck.append(bad_news)
        current_structure[-1].remove(bad_news)

        current_structure.insert(0,current_deck)
        current_deck = []
        pickle.dump([current_deck, current_structure], file)
        epidemic += 1
        print(':O')
        
    #if its the first epidemic the create the current structure as two lists, the ones that have been pulled and those that haven't    
    
        
        
    elif epidemic != 0:
        remaining = current_structure[0]
        newcountry = checkList(newcountry, remaining)
        if len(current_structure[0]) == 1:
            print('this is the last of this draw')  
            current_structure.pop(0)
            print(current_deck)
            print(current_structure[0])
        else:
            newcountry = checkList(newcountry, remaining)
            remaining.remove(newcountry)
            current_deck.append(newcountry)
        if len(current_structure) == 1:
            print('The next draw is a fresh draw!')
        else:
            print('There are ' + str(len(remaining))+ ' cards left before we go back')
        print(current_deck)
        print(current_structure)
        pickle.dump([current_deck, current_structure], file)
    
        
         
         
    
        

    
        
        
    






#def check_for_allpulled(all_infection_cards, max_deck):
    
