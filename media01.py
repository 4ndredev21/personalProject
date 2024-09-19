nota_2 = int(input("Qual a sua média?"))
nota_1 = int(input("Qual a sua média?"))
nota_3 = int(input("Qual a sua média?"))
nota_4 = int(input("Qual a sua média?"))

media = (nota_1 + nota_2 + nota_3 + nota_4) / 4

print(f"suas notas foram - {nota_1}, - {nota_2},- {nota_3} e - 7{nota_4} então sua média foi {media}")

if media >= int(6): 
    print(f" A sua média foi de {media}, então você passou de ano")
else:
    print(f"A sua média foi de {media} então você foi reprobvado , tente novamente")
