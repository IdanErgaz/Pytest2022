from classes.game import bcolors, person

magic=[{"name":"Fire", "cost":10, "dmg":60},
       {"name":"Thunder", "cost":10, "dmg":60},
       {"name":"Blizard", "cost":10, "dmg":60}]

player = person(460,65, 60, 34, magic)
enemy = person(1200, 65, 45, 25, magic)


running =True
i=0

print(bcolors.FAIL + bcolors.BOLD+ "An Ennemy Attacks!!!"+ bcolors.ENDC)
# while running:
#        print("Let's overflow this stuck!", i )
#        i+=1
