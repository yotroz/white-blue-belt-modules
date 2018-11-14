#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Nov 13 10:13:54 2018

@author: yotroz
"""

#%%

#WHITE BELT 1.1

from math import pi 


def calculate_volume_cilinder(height, radius): 
    return pi * (float (radius) ** 2) * float (height) 
    

#%%
#WHITE BELT 1.2    
def calculate_volume_sphere(radius): 
    return (float(radius) **3) * pi * 4/3



#%%BLUE BELT 2.1

import matplotlib.pyplot as plt



def histogram(total_students): 
    
    grades = ["Pass 15%", "Proficient 35%", "Excellence 35%", "Honors 15%"]
 
    #transform the argument of the function into it's percentage relative. 
    #We pass it inside the round function so we always get an integer 
    #(we can't have a student split into decimals)
    
    pass_students = round(total_students * .15) 
    proficient_students = round(total_students * .35)
    excellence_students = round(total_students * .35)
    honors_students = round(total_students * .15)
    
    #"Compile" the num variables into a list of numbers to pass it as an argument
    #in the bar function.
    
    bins = [pass_students, proficient_students, excellence_students, honors_students]
    
    
    
    #labels for the graph     
    plt.ylabel('Number of Students')
    plt.title('Grade Distribution of IE Students')
    plt.bar(grades,bins, color= "tomato")
    
    plt.show()
    
    
histogram(100)    

#%%





