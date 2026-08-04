shopping = ["milk","Bread","Rice","dal"]
print("orginal list:",shopping)

shopping.append("fruits")
shopping[1] = ("Butter")
shopping[3] = ("Daal")

shopping.remove("Rice")

print("final list:",shopping)

print("\n")

number = [10,20,30,40,50,60]

print("First 3:",number[:3])
print("Last 3:",number[-3:])
print("Reverse:",number[::-1])
