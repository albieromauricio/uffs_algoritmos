#jogo da velha
#cria a matriz
matriz_jogo = [[f"{j} {i}" for i in range(3)] for j in range(3)]
#armazena o status de vitoria
vitoria = False
#armazena os jogadores
jogadores_caratere = set()
#armazena o número de jogadas
jogadas = 0
#armazena a última jogada
ultima_jogada = 0
#mantém a execução até a vitoria
while not vitoria:
  #imprime o tabuleiro
  for i in range(3):
    for j in range(3):
      print(f"|{matriz_jogo[i][j]}|", end=" ")
    print(f'\n')
  #verifica se a jogada, posição ou caractere é válido
  try:
    i,j = map(int, input("Insira a linha e coluna correspondente: ").split())
    #verifica se a posição é válida
    if matriz_jogo[i][j] != f"{i} {j}":
      raise ValueError

    #armazena a jogada no tabuleiro
    matriz_jogo[i][j] =f' {input(f"Preencha o valor para {i} {j}: ")} '
    #armazena o jogador
    jogadores_caratere.add(matriz_jogo[i][j])
    #verifica se o numero de jogadores é valido (2), ou se a jogada é valida(feita por outro jogador)
    if len(jogadores_caratere) > 2 or ultima_jogada == matriz_jogo[i][j]:
      #remove o jogador inválido
      jogadores_caratere.remove(matriz_jogo[i][j])
      #remove a jogada inválida
      matriz_jogo[i][j] = f"{i} {j}"
      raise ValueError
    #atualiza a ultima jogada
    ultima_jogada = matriz_jogo[i][j]
  #tratamento de erros, jogadas inválidas...  
  except:
    print("Jogada, posição ou caractere inválido, tente novamente!")
    continue
  #atualiza o número de jogadas
  jogadas +=1
 
  #verifica a igualdade dos elementos da diagonal secundaria 
  if matriz_jogo[0][2] == matriz_jogo[1][1] == matriz_jogo[2][0]:
    print(f"\nJogador {matriz_jogo[1][1]} venceu!\n")
    vitoria = True
  #verifica a igualdade dos elementos da diagonal principal
  elif matriz_jogo[0][0] == matriz_jogo[1][1] == matriz_jogo[2][2]:
    print(f"\nJogador {matriz_jogo[1][1]} venceu!\n")
    vitoria = True
  #verifica a igualdade das colunas e linhas
  for i in range(3):
    if matriz_jogo[0][i] == matriz_jogo[1][i] ==  matriz_jogo[2][i]:
      print(f"\nJogador {matriz_jogo[1][i]} venceu!\n")
      vitoria = True
    elif matriz_jogo[i][0] == matriz_jogo[i][1] ==  matriz_jogo[i][2]:
      print(f"\nJogador {matriz_jogo[i][1]} venceu!\n")
      vitoria = True

  #verifica a ocorrência de empate 
  if jogadas == 9 and not vitoria:
    print("Empate!")
    break
#mostra o tabuleiro final
for i in range(3):
    for j in range(3):
      print(f"|{matriz_jogo[i][j]}|", end=" ")
    print(f'\n')