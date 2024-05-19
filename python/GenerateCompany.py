# Created by Mattias Lindblom 
# Final Project
# 2024-04

from random import randint
import random

# Generate a randomized number with format XXXXXX-XXXX
def createOrganisationNumber():

    number = ""

    for x in range(10):
        randomInt = randint(0, 9)
        number += str(randomInt)
        organisationNumber = number[:6] + '-' + number[6:]
    return organisationNumber

# Randomly returns one of four different types of companies. 
def createCompanyType():
    companyType = ["Aktiebolag", "Enskild Näringsverksamhet", "Handelsbolag", "Kommanditbolag"]
    return random.choice(companyType)

# Generates an adress from predefined prefix and suffix names and returns adress as a string
def createAdress():
    adressPrefix = ["Hallon" ,"Makar", "Snö", "Råg", "Vete", "Höga", "Fina", "Leka", "Syd", "Nord", "Väst", "Öst"]
    adressSuffix = ["vägen", "stigen", "gatan", "slingan"]

    prefix = random.choice(adressPrefix)
    suffix = random.choice(adressSuffix)
    return prefix + suffix

def createAdressNumber():
    number = randint(1, 150)
    return str(number)

# Generates a random phone number of 10 digits with for digit always being number zero.
# Returns number as a string
def createPhonenumber():
    phone = "0"
    for x in range(9):
        num = randint(0, 9)
        phone += str(num)
    return phone

# Used previous defined functions to generate company information to create a fictional company consisting of a
# name, adress, type, phone and organisation number. These companies are placed in a list and returned as a list. 
def generateCompany():
    orgNumber = createOrganisationNumber()
    type = createCompanyType()
    adress = createAdress()
    adressnumber = createAdressNumber()
    phone = createPhonenumber()

    company = []
    company.append(orgNumber)
    company.append(type)
    company.append(adress)
    company.append(adressnumber)
    company.append(phone)
    return company