import random

class Tateti:

    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append("-")
            self.board.append(row)

    def jugador_1(self):
        return random.randint(0, 1)

    def agrego(self, row, col, player):
        self.board[row][col] = player

    def ganador(self, player):
        win = None

        n = len(self.board)

        # checking rows
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[i][j] != player:
                    win = False
                    break
            if win:
                return win

        # checking columns
        for i in range(n):
            win = True
            for j in range(n):
                if self.board[j][i] != player:
                    win = False
                    break
            if win:
                return win

        # checking diagonals
        win = True
        for i in range(n):
            if self.board[i][i] != player:
                win = False
                break
        if win:
            return win

        win = True
        for i in range(n):
            if self.board[i][n - 1 - i] != player:
                win = False
                break
        if win:
            return win
        return False

        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def empate(self):
        for row in self.board:
            for item in row:
                if item == '-':
                    return False
        return True

    def turno(self, player):
        return 'X' if player == 'O' else 'O'


    def show_board(self):
        for row in self.board:
            for item in row:
                print(item, end=" ")
            print()

    def start(self):
        
        self.create_board()

        player = 'X' if self.jugador_1() == 1 else 'O'

        while True:

            print(f"Turno jugador {player}")

            self.show_board()

            # ingreso coordenadas
            row, col = list(map(int, input("Ingrese coordenadas del tablero separado por coma: (Ej: Fila,Columna) --> ").split(",")))

            print()

            # agrego el lugar
            self.agrego(row - 1, col - 1, player)

            # comprobar si el jugador gana
            if self.ganador(player):
                print(f"Jugador {player} ganó el juego!")
                break

            # comprobar empate
            if self.empate():
                print("Juego empatado!")
                break

            # cambio turno
            player = self.turno(player)

        # showing the final view of board
        print()
        self.show_board()

Ta_te_ti = Tateti()
Ta_te_ti.start()