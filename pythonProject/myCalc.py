import re
print("### Idan's Calculator: ###")
print("+++++++++++++++++++++++++++++")

run =True
pre=0

def calculator():
    global run
    global pre
    query = ""

    if pre==0:
        query = input("Please type your query:")
    else:
        query = input(str(pre))

    if query=="quit" or query=="QUIT":
        print("****************************************")
        print("** You chose to close the calculator!!**")
        print("****************************************")
        run = False
    else:
        query=re.sub('[a-zA-Z,: " "]', ' ', query)
        if pre==0:
            pre=eval(query)
        else:
            pre= eval(str(pre)+ query)
    print("You typed:", pre)
while run:
    calculator()

