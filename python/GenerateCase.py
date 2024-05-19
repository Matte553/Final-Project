# Created by Mattias Lindblom 
# Final Project
# 2024-04

import random
from random import randint
import datetime

# # Returns a string containing the name of random case manger
# def createCaseManager():
#     managers = ["Eva Nilsson", "Karl Nordström", "Frank Persson", "Sigrid Lund", "Thomas Hendriksson"]
#     return random.choice(managers)

# Returns a random date from a given start date and end date
def randomDate(start, end):
    return start + datetime.timedelta(seconds = randint(0, int((end - start).total_seconds())))

# Returns a randomized date from 2014-01-01 to current date
def createEntryDate():
    date1 = datetime.datetime(2014, 1, 1)
    date2 = datetime.datetime.now()
    randomizedDate = randomDate(date1, date2)
    return (randomizedDate)

# Returns a random chosen status that respresent a case status
def createStatus():
    status = ["Mottagen", "Pågående", "Avslutad"]
    return random.choice(status)

# Return a random choses topic that represents topic of the case that is being handled 
def createTopic():
    topic = ["Registrera Företag", "Adressbyte", "Namnbyte", "Betalning"]
    return random.choice(topic)

# Returns a list containing all randomly generated information about a case
def generateCase():
    # caseManger = createCaseManager()
    date = createEntryDate()
    status = createStatus()
    topic = createTopic()

    case = []
    # case.append(caseManger)
    case.append(date)
    case.append(status)
    case.append(topic)
    return case