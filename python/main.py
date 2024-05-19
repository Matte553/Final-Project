# Created by Mattias Lindblom 
# Final Project
# 2024-04

import mariadb 
from GenerateCompanyName import *
from GenerateDocument import *
from GenerateCompany import *
from GenerateCase import *

try:
    conn = mariadb.connect(
        user = "root",
        password = "123",
        host = "127.0.0.1",
        database = "bolagsverket"
    )

    cur = conn.cursor()

    #_______________ Populate the customer, case and document table in the database with 100 entries ___________________
    
    # Returns a list of 100 company names
    companyNames = createName()


    # Read all the Case managers ID's into a list. Case mangager id randomly picked from list when creating a case
    query = "select * from handläggare"
    handläggare = []
    cur.execute(query)
    for (id, name) in cur:
        handläggare.append(id)


    # Generate 100 companies with some cases for each company and some documents for each case
    for i in range(100):

        # Generates and inserts a fictional company into table 'kund'
        company = generateCompany()
        company.insert(2, companyNames[i])
        query = "insert into kund (organisationsnummer, företagsform, namn, adress, adressnummer, telefon) values (?,?,?,?,?,?)"
        cur.execute(query, company)


        # Generates and inserts a fictional case into table 'ärende'
        # Numbers of cases that can be created for a single customer
        casesPerCustomer = [1, 2, 3]
        casesPerCustomerWeight = [8, 1, 1]
        numberOfCases = random.choices(casesPerCustomer, casesPerCustomerWeight, k = 1)

        customerID = cur.lastrowid
        for x in range(numberOfCases[0]):
            case = generateCase()
            case.insert(0, customerID)
            case.insert(1, random.choice(handläggare))
            query = "insert into ärende (kund_id, handläggare_id, diarieföringsdatum, status, ämne) values (?, ?, ?, ?, ?)"
            cur.execute(query, case)
        

        # Generates and inserts a fictional document into table 'handling'
        # Numbers of documents that can be created for a single case
        documentPerCase = [1, 2, 3]
        documentPerCaseWeight = [8, 1, 1]
        numberOfDocuements = random.choices(documentPerCase, documentPerCaseWeight, k = 1)

        for x in range(numberOfDocuements[0]):
            caseID = cur.lastrowid
            document = generateDocument()
            document.insert(0, caseID)
            query = "insert into handling (ärende_id, objekt_typ) values (?, ?)"
            cur.execute(query, document)

        print("row with id: ", customerID, " created")

    conn.commit()
    conn.close()

# Cathes incoming error that can occur when connection to database
except mariadb.Error as error:
    print(f"Error : {error}")