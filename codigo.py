valor = int(input("valor: "))

ultimos2 = valor%100
esto = valor//10
penultimo = esto%10
ultimo = ultimos2%10

if(penultimo!=ultimo):
    print("los dos ultimos numeros son diferentes")
else:
    print("los dos ultimos numeros son iguales")