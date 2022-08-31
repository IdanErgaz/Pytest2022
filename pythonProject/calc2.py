import re
pre=0
run =True
def calculator():
    global pre
    global run
    equation=""

    if pre==0:
        equation=input("Please type your query:")
    else:
        equation=input(str(pre))

    if equation=="quit":
        run =False
    else:
        equation=re.sub('[a-zA-Z,:()""]', '', equation)
        if pre==0:
            pre=eval(equation)
        else:
            pre =eval(str(pre)+equation)

    print("You typed :",pre)
while run:
    calculator()