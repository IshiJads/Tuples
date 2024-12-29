Address=("1","Stansard","London","4d5j394","England")
door_no,streetname,city,zipcode,country=Address
print (Address[4])
print (Address[1:3])
#Address[1]="Picadilly" DATA IS UNCHANGABLE
if "London" in Address:
    print ("Data is present")

elif "Picadilly" in Address:
    print ("Data is not present.")
    
for item in Address:
    print (item)