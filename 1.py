str = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."
print("Символов :", len(str))
c = 0
for char in str:
    if char.isalpha():
        c+=1
print(c)

str_2 = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua." [::-1]
print(str_2)


str_3 = str.replace(" ", "")
print(str_3)

str_4 = str.replace(".", "")
str_5 = str_4.replace("ipsum", "")
str_6 = str_5 + " ipsum."
print(str_6)

spaces = str.count(" ")
print(spaces)