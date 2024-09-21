idade = int(66)

if idade < 18 :
    print(f"Sua idade é : {idade} então você é menor de idade e não pode passar ")
elif idade >= 18 and idade <= 65 :
    print(f"sua idade é de : {idade} , então você é um adulto")
else :
    print(f"sua idade é de : {idade}, então você é um idoso")
    
idade_certa = int(idade)

if idade_certa == int(66) :
    idade_certa = input("qual a sua idade?") 
