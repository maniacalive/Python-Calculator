no1 = input('What should be your First Number: ')
opt = input('What should be your operator(+, -, *, /): ')
no2 = input('What should be your Second Number: ')
if opt == '+' :
  sum = int(no1) + int(no2);
  print('Result ' + str(sum))

if opt == '-' :
  sum = int(no1) - int(no2);
  print('Result ' + str(sum))

if opt == '*' :
  sum = int(no1) * int(no2);
  print('Result ' + str(sum))

if opt == '/' :
  sum = int(no1) / int(no2);
  print('Result ' + str(sum))

else :
  print('Error. Check your number or mode of operator!')