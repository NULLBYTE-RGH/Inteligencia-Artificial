import math
import numpy as np
from copy import deepcopy

'''
 Função de Avaliação
'''
def funcaoAvaliacao(mat, jogador):
  def pontuar(matString, jogador):
    if jogador == 'X':
      pontos = 0
      if 'XXX' in matString:
        pontos += 1000
      if 'OOO' in matString:
        pontos -= 1000
    else:
      pontos = 0
      if 'OOO' in matString:
        pontos += 1000
      if 'XXX' in matString:
        pontos -= 1000
    return pontos

  matString = ''
  for x in range(3):
    for y in range(3):
      matString += mat[x][y]
    matString += '\n'

  for y in range(3):
    for x in range(3):
      matString += mat[x][y]
    matString += '\n'

  for x in range(3):
    l = x
    c = 0
    while l < 3 and c < 3:
      matString += mat[l][c]
      l += 1
      c += 1
    matString += '\n'

  for x in range(3):
    l = 0
    c = x
    while l < 3 and c < 3:
      matString += mat[l][c]
      l += 1
      c += 1
    matString += '\n'

  for x in range(3):
    l = x
    c = 0
    while l >= 0 and c < 3:
      matString += mat[l][c]
      l -= 1
      c += 1
    matString += '\n'

  for x in range(3):
    l = 2
    c = x
    while l >= 0 and c < 3:
      matString += mat[l][c]
      l -= 1
      c += 1
    matString += '\n'
  return pontuar(matString, jogador)

'''
 Funções úteis
'''
def primeiraLinhaLivre(coluna, mat):
  return livre(2, coluna, mat)

def livre(linha, coluna, mat):
  if linha < 0:
    return -1
  if mat[linha][coluna] == ' ':
    return linha
  return livre(linha - 1, coluna, mat)

def outro(jogador):
  if jogador == 'X':
    return 'O'
  else:
    return 'X'

def gereSucessores(inicio, vez):
  suc = []
  for i in range(3):
    linha = primeiraLinhaLivre(i, inicio)
    if linha >= 0:
      novaMat = deepcopy(inicio)
      novaMat[linha][i] = vez
      suc.append(novaMat)
    else:
      suc.append(None)
  return suc

def imprimirMatriz(mat):
  print('😡 = Computador     😎 = Humano\n')
  for i in range(3):
    print(f'{i:2} ', end=' ')
    for j in range(3):
      if mat[i][j] == 'X':
        print('😡', end=' ')
      elif mat[i][j] == 'O':
        print('😎', end=' ')
      else:
        print(' ', end=' ')
    print()
  print('   0  1  2 ')
  print()

def quantasJogadasRestam(mat):
  cont = 0
  for i in range(3):
    for j in range(3):
      if mat[i][j] == ' ':
        cont += 1
  return cont

def minimax(mat, profundidade, jogador):
  if profundidade == 0 or quantasJogadasRestam(mat) == 0:
    return funcaoAvaliacao(mat, jogador)
  if jogador == 'X':
    maxEval = -math.inf
    for suc in gereSucessores(mat, 'X'):
      if suc is not None:
        eval = minimax(suc, profundidade - 1, 'O')
        maxEval = max(maxEval, eval)
    return maxEval
  else:
    minEval = math.inf
    for suc in gereSucessores(mat, 'O'):
      if suc is not None:
        eval = minimax(suc, profundidade - 1, 'X')
        minEval = min(minEval, eval)
    return minEval

def main():
  mat = [[' ', ' ', ' '],
         [' ', ' ', ' '],
         [' ', ' ', ' ']]

  imprimirMatriz(mat)
  while True:
    jogadasRestantes = quantasJogadasRestam(mat)
    print('Restam', jogadasRestantes, 'jogadas no máximo.')
    if jogadasRestantes == 0:
      print('Empate!!')
      break
    while True:
      colunaString = input('Entre com a coluna em que deseja jogar: ')
      coluna = int(colunaString)
      linha = primeiraLinhaLivre(coluna, mat)
      if linha >= 0:
        break
      else:
        print('Essa coluna está lotada. Tente outra.')
    mat[linha][coluna] = 'O'
    placar = funcaoAvaliacao(mat, 'O')
    imprimirMatriz(mat)
    if placar > 0:
      print('Vantagem do COMPUTADOR')
    else:
      print('Vantagem do HUMANO')
    if placar <= -1000:
      print('Parabéns, você ganhou!!')
      break
    coluna = minimax(mat, 2, 'X')
    linha = primeiraLinhaLivre(coluna, mat)
    if linha == -1:
      print('Empate!!!!')
      break
    print('\nMinha jogada: COLUNA =', coluna, ', LINHA =', linha)
    mat[linha][coluna] = 'X'
    imprimirMatriz(mat)
    placar = funcaoAvaliacao(mat, 'X')
    if placar > 0:
      print('Vantagem do COMPUTADOR')
    else:
      print('Vantagem do HUMANO')
    if placar >= 1000:
      print('Patinho! Eu ganhei!!!!')
      break

main()
