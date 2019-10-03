print('Hello, welcome to tech quiz!')

ans=input('Are you ready to play (yes/no):')
score = 0
total_q = 5

if ans.lower() == 'yes':

  ans = input('1) what is the best programming language?')
  if ans.lower()=='python':
    score=score+1
    print('correct')
  else:
    print('incorrect')
    

  ans = input('2) what is 2+8+9-1?')

  if ans.lower() == '18':
   score=score+1
   print('correct')
  else:
   print('incorrect')

  ans=input('3)how python is saved in file?')

  if ans.lower() == 'py':
   score=score+1
   print('correct')
  else:
   print('incorrect')

  ans=input('4) Is python a case sensitive language?')

  if ans.lower() == 'right':
   score=score+1
   print('correct')
  

   ans=input('5)How to remove values to a python array?' )

  if ans.lower() == 'pop()' or ans.lower=='remove()':
   score=score+1
   print('correct')
  else:
   print('incorrect')

print('Thank you for playing the tech quiz','you got score',score,"",'out of 5')
marks= (score/total_q)*100

print('marks',marks)
