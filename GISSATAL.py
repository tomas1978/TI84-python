import random 
gissningar=0
slumptal=random.randint(0,101)
tal=-1
while tal!=slumptal:
  gissningar+=1
  tal=int(input("Gissa tal 0-100: "))
  if tal<slumptal:
    print("for lagt")
  elif tal>slumptal:
    print("for hogt")
  else:
    print("bra! Ratt gissning")
    print("Antal gissningar",gissningar)
    break
    

