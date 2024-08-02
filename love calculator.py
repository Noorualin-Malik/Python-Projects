name_1=input('enter your name=')
name_2=input('enter your partner name=')
combine=name_1+name_2
lower=combine.lower()

t=lower.count('t')
r=lower.count('r')
u=lower.count('u')
e=lower.count('e')
true_1=t+r+u+e

l=lower.count('l')
o=lower.count('o')
v=lower.count('v')
e=lower.count('e')
true_2=l+o+v+e

love_score = str(true_1)+str(true_2)
print(love_score)