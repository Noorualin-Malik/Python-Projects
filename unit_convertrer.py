print("Unit Converter")

num1=input("Enter the value:")
unit1= input("Enter the unit 1: ")
unit2=input("Enter the unit 1: ")

if unit1 =="cm" and unit2 =="m":
    ans=float(num1)/100
    print(ans)

elif unit1=="m" and unit2=="cm":
    ans=float(num1)*100
    print(ans)

elif unit1=="mm" and unit2=="cm":
    ans=float(num1)/10
    print(ans)

elif unit1=="mm" and unit2=="m":
    ans=float(num1)/1000
    print(ans)

if unit1=="cm" and unit2=="mm":
    ans=float(num1)*10
    print(ans)

elif unit1=="m" and unit2=="mm":
    ans=float(num1)/1000
    print(ans)

elif unit1=="km" and unit2=="m":
    ans=float(num1)*1000
    print(ans)

elif unit1=="km" and unit2=="mm":
    ans=float(num1)*100000
    print(ans)

elif unit1=="mm" and unit2=="km":
    ans=float(num1)/100000
    print(ans)

elif unit1=="ft" and unit2=="cm":
    ans=float(num1)*30.48
    print(ans)

elif unit1=="ft" and unit2=="mm":
    ans=float(num1)*304.8
    print(ans)

elif unit1=="ft" and unit2=="inch":
    ans=float(num1)*12
    print(ans)

elif unit1=="inch" and unit2=="cm":
    ans=float(num1)*2.54
    print(ans)

elif unit1=="inch" and unit2=="mm":
    ans=float(num1)*25.4
    print(ans)

elif unit1=="cm" and unit2=="inch":
    ans=float(num1)/2.54
    print(ans)

elif unit1=="m" and unit2=="cm":
    ans=float(num1)*100
    print(ans)