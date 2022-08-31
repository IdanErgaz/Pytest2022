class footbalPlayer:
    def __init__(self,first, last, height, weight, num, team):
        self.first=first
        self.last=last
        self.height=height
        self.weight=weight
        self.num=num
        self.team=team

    def playerDetail(self):
        print('Name:{}, LastName:{}, Height:{}. Weight:{}, Num:{}, Team:{}'.format(self.first, self.last, self.height, self.weight, self.num, self.team))


#Main:
player1=footbalPlayer('Idan', 'Ergaz', 183, 77, 10, 'Macabi Haif')
player2=footbalPlayer('Naty', 'Ergaz', 173, 60, 11, 'Macabi TelAviv')

player1.playerDetail()
player2.playerDetail()
#decrease the weight of player 1 and print it
player1.weight=player1.weight-3
print('Player1 new weight is: '+ str(player1.weight))

#Update player2 team and print it
player2.team='Hapoel TelAviv'
print('Player2 new team is:'+ player2.team)