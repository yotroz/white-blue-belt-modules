#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  6 09:36:14 2018

@author: yotroz
"""

#%%

import requests

def get_lyrics(artist, song_name): 
    
    url = "https://api.lyrics.ovh/v1/" + artist + "/" + song_name
    
#    Other way to write this synthax
    
#    url = "https://api.lyrics.ovh/v1/Queen/{}/{}".format(artist, song_name)    
    
    response  = requests.get(url)
        
    print(response.json()["lyrics"])

#%%


def iss_location(): 
    
    url = "http://api.open-notify.org/iss-now.json"
    
    response = requests.get(url)
    
    position = response.json()["iss_position"]
    
    print("currently the ISS is in {}:{}".format(
            position["latitude"], 
            position["longitude"]))
    
#%% #BlackBelt
    
def countries_population(): 
    
    url = "http://api.population.io:80/1.0/countries"
    
    response = requests.get(url)
    
    countries = []
    
#    we pass the response as a set function so we can get randomized countries
    
    for country in set(response.json()["countries"]): 
#        we do this if to exclude continents, that are written in capital letters
#        the way we do it is by comparing if the conversion of the local variable
#        to upper case is the same as the original local variable itself. 
        
        if country.upper() != country: 
#            we do this next if because we only want the first ten countries
            if len(countries) < 10: 
                countries.append(country)
                

                
# now we want to get all the 
                
    for country in countries: 
        url = "http://api.population.io:80/1.0/population/" + country + "/today-and-tomorrow/"
        
        response = requests.get(url)
        
#        json = response.json()
        
        
        population = response.json()["total_population"]
        
        print(country)
        
        for day in population: 
            print(day["date"] + ": " + str(day["population"]))
        
        
    
    return countries
    
    