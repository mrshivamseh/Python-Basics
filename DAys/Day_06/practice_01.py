fruits = {""}
fruits.add("Orange")
# fruits.remove("Banana")
fruits.discard("Banana")

set1 = {"Apple","Banana"}
set2 = {"Mango","Orange"}

result = set1.union(set2)
print(result)


set1 = {"Apple","Banana","Mango"}
set2 = {"Mango","Orange","Apple"}

result = set1.intersection(set2)
print(result)

print("\n")



set1 = {"Apple","Banana","Mango"}
set2 = {"Mango","Orange","Apple"}

result = set1.difference(set2)
print("Difference:",result)

#symmetric Difference
result = set1.symmetric_difference(set2)
print("Symmetric Difference:",result)


