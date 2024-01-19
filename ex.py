d = {
    "Ivan": "is bad student",
    "Nolan": "is good student"
}

print(d['Ivan'])

print(list(d.keys()))

for n in list(d.keys()):
    print("Name: " + n)
    print("He: " + d[n])