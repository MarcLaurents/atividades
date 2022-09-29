perguntas = [
  'Telefonou para a vitima?',
  'Esteve no local do crime?',
  'Mora perto da vitima?',
  'Devia para a vitima?',
  'Ja trabalhou com a vitima?'
]

avaliacao = [
  'Inocente!',
  'Suspeita!',
  'Cumplice!',
  'Assassino'  
]

contador = 0

print('Interrogatório: \n' + 'Responda SIM ou NAO: \n')

for i in perguntas:
  resposta = str(input(i)).upper()
  if resposta == 'SIM':
    contador += 1
    print('Certo!')
  else:
    contador = contador
    print('Tudo bem!')
if contador == 0:
  print(avaliacao[0])
elif contador < 3:
  print(avaliacao[1])
elif contador < 5:
  print(avaliacao[2])
else:
  print(avaliacao[3])