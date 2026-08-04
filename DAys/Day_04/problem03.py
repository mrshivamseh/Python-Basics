fruits = ["Apple","Banana","Mango","Orange","Grapes"]

print("Full list:",fruits)
fruits[1] = "kiwi"
print("Replace list:",fruits)

fruits[-1] = "watermelon"
print("New replace list:",fruits)

print("remove item list:",fruits.remove("Mango"))

print("Final list:",fruits)

print("final reverse list:",fruits[::-1])