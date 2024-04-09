
contacts = {
    "Ola" : "ola@example.com",
    "Daniel" : 30,
    "Ania" : "ania@example.com"
}

contacts["Rafał"] = "rafal@example.com"

print(contacts["Ola"])
print(contacts["Daniel"])
print(type(contacts))
print(len(contacts))

print( contacts.keys() )
print( contacts.values() )
contacts["Lukasz"]=12345
for key in contacts:
    print( key + " " + str(contacts[key]) )

print(" ")

for key, value in contacts.items():
    print( key, " ", value)

