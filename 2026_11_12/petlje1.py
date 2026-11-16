# print("Hello")
# print("Hello")
# print("Hello") 2010, 
# print("Hello")
# print("Hello")
         # 0, 1, 2, 3, 4   
for x in range(5):
    print("Hello", x)

pocetna_godina = 2010
krajnja_godina = 2015
                #  11, 12, 13, 14, 15    2016
print("****************Allowed years*************")
for godina in range(pocetna_godina, krajnja_godina+1):
    print(godina)

print("***************************")


broj = 5
print("1\t2\t3")
print("***********************")
for x in range(1, broj+1): # 1, 2, 3, 4, 5
    print(f"{x*1}\t{x*2}\t{x*3}")

for x in range(5):
    for y in range(5):
        print("#", end=" ") # # #
    print()


for x in range(5):
    for y in range(5):
        if x == 0 or x == 4 or y == 0 or y == 4:
            print("#", end="")
        else:
            print(" ", end="")
    print()
