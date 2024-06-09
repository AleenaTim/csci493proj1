import json
from pymongo import MongoClient

# Connect to the MongoDB server (default is localhost on port 27017)
client = MongoClient('mongodb://localhost:27017/')

# Select the database and collection
db = client['data']
collection = db['cityinspection']

# # # Load JSON data
# # # with open('city_inspections.json') as file:
# # #     data = json.load(file)

# # # for document in data:
# # #     if '_id' in document:
# # #         del document['_id']

# # # # Insert data into MongoDB
# # # collection.insert_many(data)
# # # print("Data inserted successfully.")
# # # Count the total number of inspections

# # ######PROBLEM 2######
# # # total_inspections = collection.count_documents({})

# # Count the number of inspections performed in 2015
# inspections_2015 = collection.count_documents({"date": {"$regex": "2015"}})
# # Count the number of inspections performed in 2016
# inspections_2016 = collection.count_documents({"date": {"$regex": "2016"}})

# # Output the counts
# print(f"Number of inspections in 2015: {inspections_2015}")
# print(f"Number of inspections in 2016: {inspections_2016}")

# # ######PROBLEM 3######
# # # Prompt the user to input the name of a business
# # # business_name = input("Enter the name of the business: ")

# # # # Find the business in the collection
# # # business = collection.find_one({"business_name": business_name})

# # # if business:
# # #     # Check if the business has a violation
# # #     if "result" in business and business["result"] != "No Violation Issued":
# # #         print(f"The business '{business_name}' has a violation: {business['result']}")
# # #     else:
# # #         print(f"The business '{business_name}' has no violations.")
# # # else:
# # #     print("Business Not found.")

# # ######PROBLEM 4######
# # # Function to get violations count and first five businesses for a given borough
# # def get_violations_and_businesses(borough):
# #     query = {
# #         "address.city": borough,
# #         "result": "Violation Issued"
# #     }
# #     violations_count = collection.count_documents(query)
# #     businesses = list(collection.find(query).limit(5))
# #     return violations_count, businesses

# # def get_violations_and_businesses_arrays(boroughs):
# #     query = {
# #         "address.city": {"$in": [borough for borough in boroughs]},
# #         "result": "Violation Issued"
# #     }
# #     violations_count = collection.count_documents(query)
# #     businesses = list(collection.find(query).limit(5))
# #     return violations_count, businesses

# # # Get violations and businesses for Queens, Manhattan, and Staten Island
# # #https://en.wikipedia.org/wiki/List_of_Queens_neighborhoods
# # count_queens, businesses_queens = get_violations_and_businesses_arrays(["REGO PARK", "SUNNYSIDE", "WOODSIDE", "ASTORIA", "LONG IS CITY", "HOWARD BEACH", "RICHMOND HILL", "OZONE PARK", "BRIARWOOD", "CORONA", "EAST ELMHURST", "ELMHURST", "FOREST HILLS", "GLENDALE", "JACKSON HEIGHTS", "KEW GARDENS", "MASPETH", "MIDDLE VILLAGE", "RIDGEWOOD", "BAYSIDE", "BELLROSE", "COLLEGE POINT", "FLUSHING", "DOUGLASTON", "LITTLE NECK", "FLORAL PARK", "KEW GARDENS", "FRESH MEADOWS", "GLEN OAKS", "WHITESTONE", "CAMBRIA HEIGHTS", "HOLLIS", "JAMAICA", "LAURELTON", "QUEENS VILLAGE", "ROSEDALE", "SPRINGFIELD GARDENS", "ARVERNE", "BELLE HARBOR", "BREEZY POINT", "BROAD CHANNEL", "FAR ROCKAWAY", "ROCKAWAY BEACH", "ROCKAWAY PARK"])
# # count_manhattan, businesses_manhattan = get_violations_and_businesses("NEW YORK")
# # count_staten_island, businesses_staten_island = get_violations_and_businesses("STATEN ISLAND")

# # # Calculate differences in counts
# # diff_queens_staten_island = abs(count_queens - count_staten_island)
# # diff_manhattan_staten_island = abs(count_manhattan - count_staten_island)

# # # Print results
# # print(f"Violations in Queens: {count_queens}")
# # print(f"Violations in count_manhattan: {count_manhattan}")
# # print(f"Violations in count_staten_island: {count_staten_island}")

# # def print_businesses(businesses, borough):
# #     print(f"First five businesses with violations in {borough}:")
# #     for business in businesses:
# #         print(f"Name: {business['business_name']}, Address: {business['address']}")

# # print_businesses(businesses_queens, "Queens")
# # print_businesses(businesses_manhattan, "Manhattan")
# # print_businesses(businesses_staten_island, "Staten Island")

# # print(f"\nViolations in Manhattan: {count_manhattan}")

# # print(f"\nViolations in Manhattan: {diff_queens_staten_island}")
# # print(f"\nViolations in Manhattan: {diff_manhattan_staten_island}")'

# # import pymongo
# # import json

# # client = pymongo.MongoClient("mongodb://localhost:27017/")
# # db = client["city_inspection"]
# # collection = db["inspections"]

# # with open("city_inspections.json") as file:
# #     for line in file:
# #         data = json.loads(line)
# #         if '_id' in data:  
# #             del data['_id']
# #         collection.insert_one(data)


# business_name = input("Enter the name of the business: ")

# # User Zip Code
# def count_businesses_by_zip(zip_code):
#     count = collection.count_documents({"address.zip": zip_code})
#     return count

# zip_code = int(input("Enter a zip code: "))
# total_businesses = count_businesses_by_zip(zip_code)
# if total_businesses:
#     print("Total businesses in zip code", zip_code, ":", total_businesses)
# else:
#     print("Zip code not found")

# # # businesses in Flushing
# # flushing_businesses = collection.find({"city": "Flushing"}).limit(5)
# # for business in flushing_businesses:
# #     print("Name:", business["business_name"])
# #     print("Address:", business["address"])
# #     print()

# # # Flushing
# # flushing_violations = collection.count_documents({"city": "Flushing", "violation": True})
# # print("Total violations in Flushing:", flushing_violations)

# Count inspections by year
inspections_2015 = collection.count_documents({"date": {"$regex": "2015"}})
inspections_2016 = collection.count_documents({"date": {"$regex": "2016"}})
print("Inspections in 2015:", inspections_2015)
print("Inspections in 2016:", inspections_2016)



def get_businesses_by_zip(zip_code):
    query = {
        "address.zip": zip_code
    }
    businesses_count = collection.count_documents(query)
    businesses = list(collection.find(query).limit(5))
    return businesses_count, businesses

def count_and_print_flushing_info():
    query = {
        "address.city": "FLUSHING"
    }
    flushing_businesses_count = collection.count_documents(query)
    flushing_businesses = list(collection.find(query).limit(5))
    flushing_violations_count = collection.count_documents({"address.city": "FLUSHING", "result": "Violation Issued"})
    
    print("Total businesses in Flushing:", flushing_businesses_count)
    print("Names and addresses of businesses in Flushing:")
    for business in flushing_businesses:
        print(f"Name: {business['business_name']}, Address: {business['address']}")
    print("Businesses in Flushing with violations:", flushing_violations_count)

# Prompt user input for zip code
def search_by_zip_code():
    zip_code = input("Enter a zip code: ")
    businesses_count, businesses = get_businesses_by_zip(zip_code)
    if businesses_count:
        print("Total businesses in zip code", zip_code, ":", businesses_count)
        print("Names and addresses of businesses:")
        for business in businesses:
            print(f"Name: {business['business_name']}, Address: {business['address']}")
    else:
        print("Zip code not found.")

# Call the functions
search_by_zip_code()
count_and_print_flushing_info()