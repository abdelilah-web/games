
class Game:
    ## Constractor for the main game
    def __init__(self):
        print('Welcome to our Games')
        print('choose a game : ')
        print('press [1] to play the Even-odd game')
        print('Press [2] to play the Average game')
        print('Press [3] to play the Multiplication')
        self.choose()
        
    ##################################################
    ##Availabale choises
    def choose(self):
        while True:
            select = input('your choise : ')
            try:
                select = int(select)
                if select == 1:
                    print()
                    print()
                    self.Even_odd()
                elif select == 2 :
                    print()
                    print()
                    self.Average()            
                elif select == 3 :
                    print()
                    print()
                    self.Multiplication()
                else :
                    print('Please choose between 1, 2 or 3 ')
            except ValueError:
                print('Please Enter a valid number')

    ##################################################
    ##Even Odd code
    def Even_odd(self) :   
        print('Welcome to the Even Odd game')
        while True:
            number = input('Enter your number : ')
            if number == 'x':
                print('End Of the game')
                print('...')
                break
            try :
                number = int(number)   
                if number % 2 == 0:
                    print('Even number')
                else:
                    print('Odd number')
            except ValueError :
                print('Please enter a valid number')

    ##################################################
    ##Average Code
    def Average(self) :
        print('Welcome to the Average game')
        how_number = int(input('how many number do you want to summ : '))
        zero = 0
        summ = 0
        while how_number > zero :
            numbers = int(input('your number : '))
            zero += 1
            summ += numbers
        print(summ/how_number)
        
    ###################################################
    ##Multiplication Table game code
    def Multiplication(self) :
        print('Welcome to the Multiplication')
        start = int(input('Enter the first number : '))
        end = int(input('Enter the final number : '))

        for x in range(start,end+1):
            for y in range(1,13):
                print(x,' X ',y ,' = ' ,x*y)
            print('__________________________________')





## Create Object from the Class
play = Game()
























    
