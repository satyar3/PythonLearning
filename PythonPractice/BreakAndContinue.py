name = "Alexander"
for i in name:
    print(i)
    if(i == "x"):
        break

print("----------------------------")
for i in name:
    if(i == "x"):
        continue
    else:
        print(i)