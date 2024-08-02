import random
names=input("Enter everybody's name here:")
names_list=names.split(" ")
#length=len(names_list)
#random_choice=random.randint(0,length-1)
#print(f'{random_choice} will pay the bill')
#or
random_choice=random.randint(names_list)
print(f'{random_choice} will pay the bill')