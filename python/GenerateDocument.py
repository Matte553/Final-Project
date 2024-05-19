# Created by Mattias Lindblom 
# Final Project
# 2024-04

import random

# Returns a randomly chosen type of company as a string
def createType():
    documentType = ["Protokoll", "Bankintyg", "Årsredovisning", "Bolagsordningar"]
    return random.choice(documentType)

# Creates and returns a list with all information about a document
def generateDocument():
    document = []
    documentType = createType()

    document.append(documentType)
    return document
