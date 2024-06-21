
def verifica_vitoria(matriz):
  #verifica a igualdade dos elementos da diagonal secundaria
  if matriz[0][2] == matriz[1][1] == matriz[2][0]:
    return True
  #verifica a igualdade dos elementos da diagonal principal
  elif matriz[0][0] == matriz[1][1] == matriz[2][2]:
    return True
  #verifica a igualdade das colunas e linhas
  for i in range(3):
    if matriz[0][i] == matriz[1][i] ==  matriz[2][i]:
      return True
    elif matriz[i][0] == matriz[i][1] ==  matriz[i][2]:
      return True
  return False

def imprime_tabuleiro(matriz):
  for i in range(3):
    for j in range(3):
      print(f"|{matriz[i][j]}|", end=" ")
    print(f'\n')
def inpute_jogada():
  i,j = map(int, input("Insira a linha e coluna correspondente: ").split())
  
  return i,j
def valida_jogada(matriz_jogo,i,j):
  if matriz_jogo[i][j] != f"{i} {j}":
    raise ValueError
def valida_jogador(jogadores_caratere,ultima_jogada,i,j,matriz_jogo):
  if len(jogadores_caratere) > 2 or ultima_jogada == matriz_jogo[i][j]:
    jogadores_caratere.remove(matriz_jogo[i][j])
    matriz_jogo[i][j] = f"{i} {j}"
    raise ValueError
def rodar_jogo():
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
  while not vitoria and jogadas < 9:
    #imprime o tabuleiro
    imprime_tabuleiro(matriz_jogo)
    #verifica se a jogada, posição ou caractere é válido
    try:
      i,j = inpute_jogada()
      #verifica se a posição é válida
      valida_jogada(matriz_jogo,i,j)
      #armazena a jogada no tabuleiro
      matriz_jogo[i][j] =f' {input(f"Preencha o valor para {i} {j}: ")} '
      print('')
      #armazena o jogador
      jogadores_caratere.add(matriz_jogo[i][j])
      #verifica se o numero de jogadores é valido (2), ou se a jogada é valida(feita por outro jogador)
      valida_jogador(jogadores_caratere,ultima_jogada,i,j,matriz_jogo)
      #atualiza a ultima jogada
      ultima_jogada = matriz_jogo[i][j]
    #tratamento de erros, jogadas inválidas...
    except:
      print(f"Jogada, posição ou caractere inválido, tente novamente!\n")
      continue
    #atualiza o número de jogadas
    jogadas +=1
    #verifica a vitoria
    vitoria = verifica_vitoria(matriz_jogo)
  print(f"Jogador {matriz_jogo[i][j]} venceu!\n" if vitoria else f"Empate!\n")
  #mostra o tabuleiro final
  imprime_tabuleiro(matriz_jogo)
  print(f'Fim do jogo!\n')
status = 1
while status == 1:
  rodar_jogo()
  status = int(input("Deseja jogar novamente? 1 - Sim / 0 - Não: "))
  print('')
