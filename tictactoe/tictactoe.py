"""
Tic Tac Toe Player
"""

import math
import copy  # Necessário para fazer cópia profunda do tabuleiro

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    # Contar quantos X's e O's existem no tabuleiro
    x_count = 0
    o_count = 0
    
    # Percorrer todo o tabuleiro 3x3
    for i in range(3):
        for j in range(3):
            if board[i][j] == X:
                x_count += 1
            elif board[i][j] == O:
                o_count += 1
    
    # X joga primeiro, então:
    # - Se há o mesmo número de X's e O's (ou menos O's), é a vez do X
    # - Se há mais X's que O's, é a vez do O
    if x_count <= o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    # Criar conjunto vazio para armazenar as ações possíveis
    possible_actions = set()
    
    # Percorrer todo o tabuleiro
    for i in range(3):
        for j in range(3):
            # Se a célula está vazia, é uma ação possível
            if board[i][j] == EMPTY:
                possible_actions.add((i, j))  # Adicionar como tupla (linha, coluna)
    
    return possible_actions


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Verificar se a ação é válida (está nas ações possíveis)
    if action not in actions(board):
        raise Exception("Invalid action")
    
    # Fazer uma cópia profunda do tabuleiro para não modificar o original
    new_board = copy.deepcopy(board)
    
    # Descobrir qual jogador está fazendo a jogada
    current_player = player(board)
    
    # Desempacotar a ação para obter linha e coluna
    i, j = action
    
    # Aplicar a jogada na cópia do tabuleiro
    new_board[i][j] = current_player
    
    # Retornar o novo tabuleiro
    return new_board


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # Verificar linhas horizontais
    for row in board:
        if row[0] == row[1] == row[2] and row[0] is not EMPTY:
            return row[0]
    
    # Verificar colunas verticais
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] and board[0][j] is not EMPTY:
            return board[0][j]
    
    # Verificar diagonal principal (canto superior esquerdo ao inferior direito)
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] is not EMPTY:
        return board[0][0]
    
    # Verificar diagonal secundária (canto superior direito ao inferior esquerdo)
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] is not EMPTY:
        return board[0][2]
    
    # Nenhum vencedor encontrado
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # O jogo termina se:
    # 1. Há um vencedor OU
    # 2. Não há mais jogadas possíveis (tabuleiro cheio)
    return winner(board) is not None or len(actions(board)) == 0


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Descobrir quem ganhou o jogo
    game_winner = winner(board)
    
    # Retornar os valores de utilidade
    if game_winner == X:
        return 1    # X ganhou
    elif game_winner == O:
        return -1   # O ganhou
    else:
        return 0    # Empate ou jogo não terminado


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    # Se o jogo já terminou, não há jogada a fazer
    if terminal(board):
        return None
    
    # Descobrir qual jogador está jogando
    current_player = player(board)
    
    if current_player == X:
        # X quer maximizar o valor (buscar o maior valor possível)
        _, best_action = max_value(board)
        return best_action
    else:
        # O quer minimizar o valor (buscar o menor valor possível)
        _, best_action = min_value(board)
        return best_action


def max_value(board):
    if terminal(board):
        return utility(board), None
    
    best_value = -math.inf
    best_action = None
    
    for action in actions(board):
        new_board = result(board, action)
        min_val, _ = min_value(new_board)
        
        if min_val > best_value:
            best_value = min_val
            best_action = action
    
    return best_value, best_action


def min_value(board):
    """
    Função auxiliar para o minimax - busca o valor mínimo.
    Retorna uma tupla (valor, ação).
    """
    # Caso base: se o jogo terminou, retorna a utilidade
    if terminal(board):
        return utility(board), None
    
    # Inicializar com o pior valor possível para minimização
    best_value = math.inf
    best_action = None
    
    # Testar todas as ações possíveis
    for action in actions(board):
        # Simular a jogada
        new_board = result(board, action)
        
        # Obter o valor máximo da resposta do oponente
        max_val, _ = max_value(new_board)  # Desempacota a tupla corretamente
        
        # Se encontrou um valor melhor (menor), atualizar
        if max_val < best_value:  # Agora compara número com número
            best_value = max_val
            best_action = action
    
    return best_value, best_action