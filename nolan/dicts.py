house = {
    "kitchen":"Tony", 
    "garage":"Lucas", 
    "basement":"Tim"
}
rooms = list(house.keys())
people = list(house.values())
def CIAhitlist(name):
    return name + "needs to die for the security of our nation!"
print(CIAhitlist("John F. Kennedy"))

def arithmetic(x): 
    return (x * 2) + 8
print(arithmetic(5)) 