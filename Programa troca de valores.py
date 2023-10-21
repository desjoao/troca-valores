#Programa que leia dois números inteiros quaisquer A e B e troque seus valores entre si.
A = int(input('Informe um valor inteiro para a Variável A: '))
B = int(input('Informe um valor inteiro para a Variável B: '))

C = A
A = B
B = C

print(f'A variável A agora vale {A} e a variável B vale {B}.')
