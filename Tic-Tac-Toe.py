import random

positions = [" " for i in range(9)]

occupied = []
def gameBoard():
    print("""
{} | {} | {}
---------
{} | {} | {}
---------
{} | {} | {}""".format(positions[0],positions[1],positions[2],
                       positions[3],positions[4],positions[5],
                       positions[6],positions[7],positions[8],))

def user_fun(ch):
    pos = int(input("Enter the position to move.."))
    if pos in occupied:
        print("You can't move here..")
        user_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)
def cpu_fun(ch):
    pos = random.randint(1,9)
    if pos in occupied:
        cpu_fun(ch)
    else:
        positions[pos-1] = ch
        occupied.append(pos)
def check_winner():
    winning_combinations = [(0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6)]
    for combo in winning_combinations:
        if (positions[combo[0]]) == (positions[combo[1]])== (positions[combo[2]]) != " ":
            return positions[combo[0]]

def main():
    gameBoard()

    user_ch = input("Enter your Choice..X or 0").upper()
    while user_ch not in ['X','0']:
        print("Please Enter valid choice..")
        user_ch = input("Enter your Choice..X or 0").upper()
    if user_ch == 'X':
        cpu_ch = '0'
    else:
        cpu_ch = 'X'
    count  = 0
    winner = None
    while count < 5 and not winner:
        count += 1
        user_fun(user_ch)
        gameBoard()
        winner = check_winner()
        if winner:
            print("hey user, you win the match! Congratulations.")
            break
        if count == 5:
            print("It's Draw..")
        cpu_fun(cpu_ch)
        gameBoard()
        winner = check_winner()
        if winner:
            print("Cpu win, you lost!")
            break
        
            
main()
