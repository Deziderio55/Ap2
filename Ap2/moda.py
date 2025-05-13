def moda(lista):
  frequencia = {}
  for numero in lista:
    if numero in frequencia:
      frequencia[numero] += 1
    else:
      frequencia[numero] = 1

    maior_frequencia = 0
    for valor in frequencia.values():
      if valor > maior_frequencia:
        maior_frequencia = valor
  moda = 0
  for numero in frequencia:
    if frequencia[numero] == maior_frequencia:
      moda = numero

  return moda

# # Função moda(lista):
#     Crie um dicionário chamado "repetição"
#     Para cada número em lista:
#         Se número já está em repeticao:
#             Adicione o valor correspondente em 1
#         Senão:
#             Adicione o número ao dicionário com valor 1
#     Comece maior_frequencia com 0
#     Para cada valor em repeticao:
#         Se valor > maior_frequencia:
#             Atualizar maior_frequencia com esse valor
#     Comece moda com 0
#     Para cada número em repeticao:
#         Se a contagem desse número for igual à maior_frequencia:
#             Atualizar moda com esse número
#     Retorna moda
