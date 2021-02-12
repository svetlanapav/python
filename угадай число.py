import random
print("\nДобро пожаловать в 'Отгадай число'.")
print("\nБыло загадано число от 1 до 20, попытайтесь его угадать.")
 
the_number = random.randint(1,20) 
guess = int(input("\nВы: Я думаю, что это ")) 
tries = 1
 
while guess != the_number: 
  if guess > the_number: 
     print( "Нет, загаданное число меньше.") 
  else: 
      print( "Нет, загаданное число больше.") 
  guess =  int ( input ("Вы: Я думаю, что это ")) 
  tries +=1
  
print("\nВы угадали!") 
print("\nНа отгадывание было потрачено", tries, "попыток.")

input("\nНажмите >Enter<, чтобы выйти.")
