m1 = float(input("Enter the first mass in Kgs: "))
m2 = float(input("Enter the second mass in Kgs: "))
r = float(input("Enter the distance between the centres of the masses in Kms: ")) 
G = 6.673*(10**-11) 
f = (G*m1*m2)/(r**2) 
print("Hence, the gravitational force is: ",round(f,2),"N")