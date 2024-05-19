# Created by Mattias Lindblom 
# Final Project
# 2024-04

from random import randint
import random
import codecs

# Creates a company name by randomly choosing a firstname, occupation and a company type. 
# Return a list of 100 company names. 
def createName():
    occupations = ["Bygg", "Måleri", "Snickeri", "Verkstad", "Advokatbyrå", "IT"]
    companyType = ["AB", "Aktiebolag", "Handelsbolag", "Kommanditbolag"]
    companyname = ""
    companyNames = []

    file = open("förnamn.txt", encoding='utf-8')
    lines = file.readlines()
    
    for firstname in lines:
        firstname = firstname.replace("\n", "")
        firstname = firstname.lower()
        firstname = firstname.capitalize()

        finalOcc = random.choice(occupations)
        finalType = random.choice(companyType)
        
        companyname = firstname + " " + finalOcc + " " + finalType

        companyNames.append(companyname)
    return companyNames