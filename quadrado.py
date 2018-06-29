import operator
X = []
Y = []
XY = []
X2 = []
i = 1
o = 1
xy = 1
p = 0
l = 0
print("Vamos fazer a resolução por meio de Mínimos Quadrados!\n\nInstruções de uso:\n- Para números em notação científica deve-se escrevê-los como decimais comuns, para não haver erros no programa;\n- O programa utiliza sistema americano, então para casas decimais deve-se digitar PONTO. e não VÍRGULA, ;\n- Após digitar um valor aperte ENTER para que seja salvo.\n\n")
opcao = int(input("Selecione uma opção:\n1 - Achar uma equação de reta;\n2 - Você já tem os dados e quer somente calcular uma concentração\nDigite a opção que você quer: "))

while (opcao<1) or (opcao>2):
  opcao = int(input("Opção digitada não faz parte das opções disponíveis.\nSelecione uma opção:\n1 - Achar uma equação de reta;\n2 - Você já tem os dados e quer somente calcular uma concentração\nDigite a opção que você quer: "))

if (opcao == 1):

  #primeira seção, introduzindo os dados

  qtdeX = int(input("\nQuantas amostras você tem?\nNúmero de amostras: "))
  while (i <= qtdeX):
	  X.append(float(input("\nVamos ver agora quais os seus valores de X.\nDigite o {}º numero de volume que você tem: ".format(i))))
	  i = i + 1
  print("Ok, valores das concentrações salvos!\n")
  while (o <= qtdeX):
	  Y.append(float(input( "\nVamos ver os seus valores de Y.\nDigite o {}º valor de absorbância que você tem: ".format(o))))
	  o = o + 1
  print("Ok, valores das absorbâncias salvos!")

  #segunda seção, fazendo as contas de XY e X2
  XY = list(map(operator.mul, X, Y))
  print("\nA lista de XY é: {}".format(XY))
  X2 = list(map(operator.mul, X, X))
  print("\nA lista de X^2 é: {}".format(X2))

  #terceira seção, soma das listas
  somaX = sum(X)
  print("\nA somatória de X é: {}".format(somaX))
  somaY = sum(Y)
  print("\nA somatória de Y é: {}".format(somaY))
  somaXY = sum(XY)
  print("\nA somatória de XY é: {}".format(somaXY))
  somaX2 = sum(X2)
  print("\nA somatória de X^2 é: {}".format(somaX2))

  #calculando m
  m = ((somaXY*qtdeX)-(somaX*somaY))/((somaX2*qtdeX)-(somaX*somaX))
  print("\nO valor de m é {}".format(m))

  #calculando b
  b = ((somaX2*somaY)-(somaXY*somaX))/((somaX2*qtdeX)-(somaX*somaX))
  print("\nO valor de b é {}".format(b))

  #Finale, apresentando a equação da reta
  print("\n\nTendo em vista os dados inseridos a equação da reta deve ser;\nA = {:.5f}C + {:.5f}".format(m, b))
  sair = input("\n\nPressione uma tecla para sair...")

if (opcao==2):
  numM = float(input("\nDigite o valor de m da sua reta: "))
  numB = float(input("\nDigite o valor de b da sua reta: "))
  numA = float(input("\nDigite o valor de absorbância da sua reta: "))
  print("\nA sua equação é: {} = {}*C + {}".format(numA, numM, numB))
  numC = (numA - (numB))/numM
  print("\nA concentração do composto é igual a {}".format(numC))
  sair2 = input("Pressione uma tecla para sair...")