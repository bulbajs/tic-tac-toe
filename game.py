field = [
   ['-', '-', '-'],
   ['-', '-', '-'],
   ['-', '-', '-'],
     ]

def playing_field(f):

     print ('  0 1 2')
     for i in range(len(field)):
          print(i,' '.join(field[i]))

def users_input(f,user):
    while True:
        k = input(f'Ходит -{user}-, введите координаты: ').split()
        if len(k) != 2:
            print('Введите 2 координаты')
            continue
        x, y = map(int, k)
        if not ((x >= 0 and x < 3) and (y >= 0 and y < 3)):
            print('Вы вышли из диапазона')
            continue
        if f[x][y] != '-':
            print('Клетка занята')
            continue
        break
    return x,y

def win(f, user):
    def check_line(a,b,c,user):
        if a == user and b == user and c == user:
            return True
    for i in range(3):
        if check_line(f[i][0],f[i][1],f[i][2], user) or \
        check_line(f[0][i], f[1][i], f[2][i], user) or \
        check_line(f[0][0], f[1][1], f[2][2], user) or \
        check_line(f[2][0], f[1][0], f[0][2], user):
            return True

def start(field):
    count=0
    while True:
        playing_field(field)
        if count%2==0:
            user='x'
        else:
            user = 'o'
        if count<9:
            x, y = users_input(field,user)
            field[x][y] = user
        elif count==9:
            print ('Ничья')
            break
        if win(field,user):
            print(f"ПОБЕДА!!! Выиграл {user}!")
            break
        count+=1
    playing_field(field)

start(field)
