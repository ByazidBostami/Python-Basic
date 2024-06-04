runing_total=0
while True:
    user=input("Please input a number or type (exit) to quit: ")
    if user=="exit":
        break

    else:
        convertToIntegrt=int(user)
        runing_total+=convertToIntegrt
        print(runing_total)



