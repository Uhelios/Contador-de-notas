valor = int(input("Digite o valor que deseja sacar: "));
cem = int(valor / 100)
valor %= 100
cinquenta = int(valor / 50)
valor %= 50
vinte = int(valor / 20)
valor %= 20
dez = int(valor / 10)
valor %= 10
cinco = int(valor / 5)
valor %= 5
dois = int(valor / 2)
valor %= 2
um = int(valor / 1)

print("As notas que serão sacadas são:")
print("Notas de 100 reais: ", cem)
print("Notas de 50 reais: ", cinquenta)
print("Notas de 20 reais: ", vinte)
print("Notas de 10 reais: ", dez)
print("Notas de 5 reais: ", cinco)
print("Notas de 2 reais: ", dois)
print("Notas de 1 real: ", um)
