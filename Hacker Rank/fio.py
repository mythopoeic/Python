my_list = [i**2 for i in range(1,11)]

my_file = open("output.txt", "r+")

# Add your code below!
for x in my_list:
    temp = str(x) + "\n"
    my_file.write(temp)

my_file.close()