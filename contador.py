valor = int(input("Digite o valor que deseja sacar: "));
um = 0;
dois = 0;
cinco = 0;
dez = 0;
vinte = 0;
cinquenta = 0;
cem = 0;

while(valor > 0):
  if(valor >= 100):
    cem += 1;
    valor -= 100;
  elif(valor >= 50):
    cinquenta += 1;
    valor -= 50;
  elif(valor >= 20):
    vinte += 1;
    valor -= 20;
  elif(valor >= 10):
    dez += 1;
    valor -= 10;
  elif(valor >= 5):
    cinco += 1;
    valor -= 5;
  elif(valor >= 2):
    dois +=1;
    valor -= 2;
  else:
    um += 1;
    valor -= 1;

print("As notas que serão sacadas são: ")
print("Notas de 100: ", cem)
print("Notas de 50: ", cinquenta)
print("Notas de 20: ", vinte)
print("Notas de 10: ", dez)
print("Notas de 5: ", cinco)
print("Notas de 2: ", dois)
print("Notas de 1: ", um)
              
