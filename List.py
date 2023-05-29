lista = [2,3,4,5]
lista.append(7)
print(lista)

print("Esta es una prueba pa lana")

print("Segunda prueba")

newlist = [2 for x in lista if 2 == x]
print(newlist)

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
newHello = ['hello' for x in fruits]
print(newHello)

newlist = [x if x != "banana" else "orange" for x in fruits]
newlist = [x for x in range(10) if x < 5]
print(newlist)

thislist = ["orange", "mango", "kiwi", "pineapple", "banana"]
thislist.sort(reverse=True)
print(thislist)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(thisdict["brand"])
print(thisdict.keys())
print(thisdict.items())