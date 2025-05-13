def busca_largura(grafo, comeco):
  visitados = [False] * len(grafo)
  distancia = [0] * len(grafo)
  fila = [comeco]
  visitados[comeco] = True
  contador = 0 

  while contador < len(fila):
    atual = fila[contador]
    contador += 1
    for vizinho, conectado in enumerate(grafo[atual]):
      if conectado and not visitados[vizinho]:
        visitados[vizinho] = True
        distancia[vizinho] = distancia[atual] + 1
        fila.append(vizinho)

  max_distancia = 0
  for resultado in distancia:
    if resultado > max_distancia:
      max_distancia = resultado
  return max_distancia

def maior_distancia(grafo):
  max_distancia = 0 
  for i in range(len(grafo)):
    distancia = busca_largura(grafo,i)
    if distancia > max_distancia:
      max_distancia = distancia
  return max_distancia

# Função BUSCA_LARGURA(grafo, início):
#     Cria uma lista "Visitados" com "False" para cada vértice
#     Cria uma lista "Distancia" com 0 para cada vértice
#     Cria uma lista "Fila" com o vértice de início
#     Marque o vértice de início como visitado
#     Criar a variavel "Contador" = 0

#     Enquanto a variavel "Contador" for < que o tamanho da "Fila":
#         "Atual" = Fila[Contador]
#         Incrementar Contador

#         Para cada "Vizinho" do vértice "Atual":
#             Se houver conexão entre "Atual" e "Vizinho" e "Vizinho" não foi visitado:
#                 Marcar "Vizinho" como visitado
#                 Distancia[Vizinho] = "Distancia"[Atual] + 1
#                 Adicionar "Vizinho" à "Fila"

#     Retornar o maior valor da lista "Distancia"


# Função MAIOR_DISTANCIA(grafo):
#     Criar Max_distancia = 0

#     Para cada vértice i no grafo:
#         "Distancia" = BUSCA_LARGURA(grafo, i)
#         Se "Distancia" > Max_distancia:
#             Atualizar Max_distancia com "Distancia"

#     Retornar Max_distancia
