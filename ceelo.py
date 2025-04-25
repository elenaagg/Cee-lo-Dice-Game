# Angelopoulou Eleni,A.M. 4968
try:
            x=int(input("Number of players (between 2 and 6): "))
            if x>6 or x<2:
                  print("I expected between 2 and 6 players")
                  print("I'm setting the number of players to 3")
                  x=3
except(NameError,SyntaxError,ValueError,TypeError):
            
            print("Something wrong happened: invalid literal for int() with base 10:")
            print("I'm setting the number of players to 3")
            x=3
if x>6 or x<2:
      print("I expected between 2 and 6 players")
      print("I'm setting the number of players to 3")
      x=3


try:
            y=int(input("Number of coins per player (between 5 and 100): "))
            if y>100 or y<5:
                  print("I expected between 5 and 100 coins per player")
                  print("I'm setting the number of coins to 10")
                  y=10
except(NameError,SyntaxError,ValueError,TypeError):
            print("Something wrong happened: invalid literal for int() with base 10:")
            print("I'm setting the number of coins to 10")
            y=10
print("Game begins with",x,"players.")
print("Each player has",y,"coins.")
lst=[]
k=[]
c=0
from random import randint
a=randint(1,x)
print("Player",a,"is randomly chosen as banker")
print()
print("Current balance:")
for j in range(1,x+1):
    print("Player",j,"has",y,"coins")
print()
al=0
score=[]
scor=[]
scoreB=[]
scrb=y
scr=y
for i in range(1,x+1):
    if i!=a:
        score.append(scr)
    else:
        scoreB.append(scrb)
while (0 not in score) and (0 not in scoreB):
      print()
      scoreB=[]
      f=0
      pw=0
      lst=[]
      k=[]
      c=0
      n=0
      al=0
      z=0
      print("Player",a,": You are the banker!", end='')
      B=int(input("Please enter a valid bank amount: "))
      if B>y or B<1:
            int(input("Please enter a valid bank amount: "))
      for j in range(1,x+1):
                  if j!=a:
                        print("Player",j,": ",end= '')
                        b=int(input("Please enter a valid bet: "))
                        if b > B:
                              b=int(input("Please enter a valid bet: "))
                              lst.append(b)
                        elif B>b:
                              lst.append(b)
                              if sum(lst)>B:
                                    lst.remove(b)
                                    b=int(input("Please enter a valid bet: "))
                                    lst.append(b)
                        elif sum(lst)==B:
                              break
      print()
      print("Round starts:")
      for j in range(1,x+1):
            if j!=a:
                  print("Player",j,": has bet",lst[f])
                  f+=1
            else:
                  print("Player",a,": Banker with bank amount=",sum(lst))
      print()
      print("Banker: press ENTER to roll dice")
      d=0
      while d==0:
            for g in range(1,4):
                  b=randint(1,6)
                  k.append(b)
            print("Banker rolled:",k)
            q=k.count(1)
            p=k.count(2)
            s=k.count(3)
            o=k.count(4)
            r=k.count(5)
            l=k.count(6)
            if q==3 or p==3 or s==3 or o==3 or r==3 or l==3:
                  print("Automatic Win! Banker wins all bets! Round ends!")
                  d=1
                  n=0
                  for j in range(1,x+1):
                        if j!=a:
                              scr=score[0]
                              scr-=lst[n]
                              score.append(scr)
                              del score[0]
                              n+=1
                              
                        else:
                               scrb+=sum(lst)
                               scoreB.append(scrb)
                  break
            elif (4 in k) and (5 in k) and (6 in k):
                  print("Automatic Win! Banker wins all bets! Round ends!")
                  d=1
                  n=0
                  for j in range(1,x+1):
                         if j!=a:
                              scr=score[0]
                              scr-=lst[n]
                              score.append(scr)
                              del score[0]
                              n+=1
                              
                         else:
                               scrb+=sum(lst)
                               scoreB.append(scrb)
                  break
            elif (q==2 or p==2 or s==2 or o==2 or r==2) and (6 in k):
                  print("Automatic Win! Banker wins all bets! Round ends!")
                  d=1
                  n=0
                  for j in range(1,x+1):
                        if j!=a:
                              scr=score[0]
                              scr-=lst[n]
                              score.append(scr)
                              del score[0]
                              n+=1
                              
                        else:
                               scrb+=sum(lst)
                               scoreB.append(scrb)
                               
                         
                  break
            elif (1 in k) and (2 in k) and (3 in k):
                  al=6
                  print("Automatic loss! Banker loses all bets! Round ends!")
                  exclude=[a]
                  c=randint(1,x)
                  while c in exclude:
                      c=randint(1,x)
                  print("New banker will be Player",c)
                  n=0
                  for j in range(1,x+1):
                        if j!=a:
                              scr=score[0]
                              scr+=lst[n]
                              score.append(scr)
                              del score[0]
                              n+=1
                        
                        else:
                               scrb-=sum(lst)
                               scoreB.append(scrb)
                               if scrb<=0:
                                     scrb=0
                                     break
                              
                  d=1
                  break

            elif (p==2 or s==2 or o==2 or r==2 or l==2) and q==1:
                  al=6
                  print("Automatic loss! Banker loses all bets! Round ends!")
                  exclude=[a]
                  c=randint(1,x)
                  while c in exclude:
                      c=randint(1,x)
                  print("New banker will be Player",c)
                  n=0
                  for j in range(1,x+1):
                        if j!=a:
                              scr=score[0]
                              scr+=lst[n]
                              score.append(scr)
                              del score[0]
                              n+=1
                        
                        else:
                               scrb-=sum(lst)
                               scoreB.append(scrb)
                               if scrb<=0:
                                     scrb=0
                                     break
                              
                  d=1
                  break
            elif  (q==2 or p==2 or s==2 or o==2 or r==2 or l ==2) and (p==1 or s==1 or o==1 or r ==1):
                  if p==1:
                        g=2
                  elif s==1:
                        g=3
                  elif o==1:
                        g=4
                  elif r==1:
                        g=5
                  print("Banker scored",g,"points")
                  scoreb=g
                  d=1
                  u=0
                  for e in range(1,x+1):
                        if e!=a:
                              print()
                              print("Player",e,": press ENTER to roll dice")
                              d=0
                              while d==0:
                                    k=[]
                                    for g in range(1,4):
                                          b=randint(1,6)
                                          k.append(b)
                                    print("Player rolled:",k)
                                    q=k.count(1)
                                    p=k.count(2)
                                    s=k.count(3)
                                    o=k.count(4)
                                    r=k.count(5)
                                    l=k.count(6)
            
                                    if q==3 or p==3 or s==3 or o==3 or r==3 or l==3:
                                          scr=score[0]
                                          print("Player wins!")
                                          d=1
                                          scrb-= lst[u]
                                          scr+=lst[u]
                                          scoreB.append(scrb)
                                          score.append(scr)
                                          del score[0]
                                          u+=1
                                          
                                          pw+=1
                                    elif (4 in k) and (5 in k) and (6 in k):
                                          scr=score[0]
                                          print("Player wins!")
                                          d=1
                                          scrb-= lst[u]
                                          scr+=lst[u]
                                          scoreB.append(scrb)
                                          score.append(scr)
                                          del score[0]
                                          u+=1
                                          
                                          pw+=1
                                    elif (q==2 or p==2 or s==2 or o==2 or r==2) and (6 in k):
                                           scr=score[0]
                                           print("Player wins!")
                                           d=1
                                           scrb-= lst[u]
                                           scr+=lst[u]
                                           scoreB.append(scrb)
                                           score.append(scr)
                                           del score[0]
                                           u+=1
                                           
                                           pw+=1
                                    elif (1 in k) and (2 in k) and (3 in k):
                                           scr=score[0]
                                           print("Banker wins!")
                                           d=1
                                           scrb+= lst[u]
                                           scr-=lst[u]
                                           scoreB.append(scrb)
                                           score.append(scr)
                                           del score[0]
                                           u+=1
                                           
                                    elif (p==2 or s==2 or o==2 or r==2 or l==2) and q==1:
                                          scr=score[0]
                                          print("Banker wins!")
                                          d=1
                                          scrb+= lst[u]
                                          scr-=lst[u]
                                          scoreB.append(scrb)
                                          score.append(scr)
                                          del score[0]
                                          u+=1
                                          
                                    elif  (q==2 or p==2 or s==2 or o==2 or r==2 or l ==2) and (p==1 or s==1 or o==1 or r ==1):
                                          if p==1:
                                                g=2
                                          elif s==1:
                                                g=3
                                          elif o==1:
                                                g=4
                                          elif r==1:
                                                g=5
                                          print("Player scored",g,"points")
                                          scoreP=g
                                          d=1
                                          if scoreb==scoreP:
                                                scr=score[0]
                                                print("It's a tie between the banker and the player")
                                                score.append(scr)
                                                scoreB.append(scrb)
                                                del score[0]
                                                u+=1
                                                
                                          elif scoreb>scoreP:
                                                scr=score[0]
                                                print("Banker wins!")
                                                scrb+= lst[u]
                                                scr-=lst[u]
                                                scoreB.append(scrb)
                                                score.append(scr)
                                                del score[0]
                                                u+=1
                                                
                                          elif scoreb<scoreP:
                                                scr=score[0]
                                                print("Player wins!")
                                                scrb-= lst[u]
                                                scr+=lst[u]
                                                scoreB.append(scrb)
                                                score.append(scr)
                                                del score[0]
                                                u+=1
                                                
                                                pw+=1
                                    else:
                                          k=[]
                                          print("Player rolls again")
                        else:
                              continue
                  
            else:
                  k=[]
                  print("Banker rolls again")
      print()
      print("Current balance:")
      i=0
      if al==6:
                  i=0
                  for j in range(1,x+1):
                        if j!=a:
                              if j==c:
                                    z=i
                              print("Player",j,"has",score[i],"coins")
                              i+=1
                        
                                      
                        else:
                              print("Player",j,"has",scoreB[-1],"coins")
                  for j in range(1,x+1):
                        if j==a:
                              score.insert(j-1,scrb)
                              
                              v=score.index(score[z])
                              scrb=score[z]
                  
                  del score[v]
                  a=c
                  
      else:
            i=0
            for j in range(1,x+1):
                  if j!=a:
                        if j==c:
                               z=i
                        print("Player",j,"has",score[i],"coins")
                        i+=1
                        
                  else:
                        print("Player",j,"has",scoreB[-1],"coins")
            if pw==2:
                  for j in range(1,x+1):
                        if j==a:
                              score.insert(j-1,scrb)
                              v=score.index(score[z])
                              scrb=score[z]
                  
                  del score[v]
                  exclude=[a]
                  a=randint(1,x)
                  while a in exclude:
                        a=randint(1,x)
                  print("New banker will be Player",a)
                 
                            
print()
if 0 in scoreB:
      s=a
elif 0 in score:
      s=score.index(0)
      i=0
      for j in range(1,x+1):
            if j!=a and score[i]==0:
                  i+=1
                  s=j
      
print("Player",s,"is bankrupt.Game ends.")           
      
            


      
      

              
    


                             
