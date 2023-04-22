import random



def choose_opcion ():
  opcions = ('piedra','papel','tijera')
  user_opcion = input('piedra,papel o tijera => ').lower()
  computer_opcion = random.choice(opcions)
  
  if not user_opcion in opcions:
    print('esta no es una opcion valida')
    return None,None
    #continue

  print('user opcion => ',user_opcion)
  print('computer opcion => ',computer_opcion)
  return user_opcion,computer_opcion

def rules_game(user_opcion,computer_opcion,users_win,computers_win):
  if user_opcion == computer_opcion :
    print ('ESTO ES UN EMPATE')
  elif user_opcion == 'piedra':
    if computer_opcion == 'tijera':
      print ('Piedra le gana a la tijera ')
      print ('USER A GANADO')
      users_win += 1
    else :
      print ('papel le gana a la piedra')
      print ('COMPUTER A GANADO')
      computers_win += 1
  elif user_opcion == 'papel':
    if computer_opcion == 'piedra':
      print ('el papel le gana a la piedra')
      print ('USER A GANADO ')
      users_win += 1
    else:
      print ('la tijera le ganan al papel')
      print ('COMPUTER A GANADO')
      computers_win += 1
  elif user_opcion == 'tijera':
    if computer_opcion == 'papel':
      print('la tijera le gana al papel')
      print('USER GANA ')
      users_win +=1
    else:
      print('la piedra le gana al papel')
      print('COMPUTER GANA ')
      computers_win +=1
  return users_win,computers_win
def check_winner(users_win,computers_win):
    
  if computers_win == 3 :
    print('La computadora es la victoriosa por',computers_win,'a',users_win )
    exit()
  if users_win == 3 :
    print('el user es el victorioso por',users_win,'a',computers_win )
    exit()

def run_game():
  round = 1
  computers_win = 0
  users_win = 0
  while True :
    print('#'*10)
    print ('ROUND',round)
    print ('#'*10)
  
    print ('el usuario lleva ==> ',users_win,'VICTORIAS')
    print ('la computadora lleva ==> ',computers_win,'VICTORIAS')
    round += 1
    user_opcion,computer_opcion = choose_opcion()
    users_win,computers_win = rules_game(user_opcion,computer_opcion,users_win,computers_win)
    check_winner(users_win,computers_win)
run_game()