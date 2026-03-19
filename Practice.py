import csv
import json
# ------------TXT-------------TXT----------TXT-------------
#1 reading from a text file
with open("employees.txt","r") as file:

    for employee in file:
        print(employee.strip())

#2 writing into text file:
with open("employees.txt","w") as f:
    f.write("Hello World\n")
    f.write("I'm Akash, learning Data Engineering\n")

#3 Appending into text file:
with open("employees.txt","a") as file:
    file.write("Now I'm trying append mode\n")
    file.write("With backslash n we move & write next line\n")

#------------CSV------------CSV----------CSV----------------------

#4 Writing into CSV file:

data=[
    ["order_id","customer","amount"],
    [101,"Alice",500],
    [102,"Bob",300],
    [103,"Charlie",700]
]

with open("sales.csv","w",newline="")as file:
    writer = csv.writer(file)

    writer.writerows(data)

#5 Reading from CSV file:

with open("sales.csv","r") as file:
    reader = csv.reader(file)

    next(reader) # skips column names --> Like Header of table
    for row in reader:
        print(row)

#####   using DictReader --> list converts into dictionary

with open("sales.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        print(row)   # prints all the dictionary
        print(row["customer"],row["amount"])        # prints only selected col values


#-----------JSON----------JSON-----------JSON----------
#6 Reading JSON files :

with open("customer.json","r") as file:
    reader = json.load(file)

    for customer in reader:
        print(customer)
        print(customer["id"], customer["name"])

#7 Writing into JSON Files :

data = [
 {"id":1,"name":"Alice","city":"Delhi"},
 {"id":2,"name":"Bob","city":"Mumbai"}
]
with open("customer.json","w") as file:
    json.dump(data,file)

#--------Examples-------Examples--------Examples

# 8 Read a sales CSV file, calculate total sales, and write summary
total_sales = 0
with open("sales.csv","r") as file:
    reader = csv.DictReader(file)

    for row in reader:
        total_sales += int(row["amount"])

print("Total Sales :", total_sales)

#9 Remove rows with missing values and insert into another file
cleaned_data = []
with open("sales.csv") as file:
    reader = csv.DictReader(file)

    for row in reader:
        if row["amount"]!="":
            cleaned_data.append(row)

with open("cleaned_data.csv", "w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["order_id","customer","amount"])
    writer.writeheader()
    writer.writerows(cleaned_data)

print(cleaned_data)

#Real Data Engineering Example
#10 Suppose we download API data as JSON.
with open("customer.json","r") as file:
    reader = json.load(file)

with open("customer.csv","w",newline="") as file:
    writer = csv.DictWriter(file,fieldnames=["id","name","city"])
    writer.writeheader()

    for customer in reader:
        writer.writerow(customer)

#11 Processing Logs (Very Real Data Engineering Task)
# -- Extract ERROR logs.
with open("Log_file.txt","r") as file:
    for i in file:
        if "ERROR" in i:
            print(i.strip())
