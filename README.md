# 2048 Game

A simple implementation of the 2048 game in Python. The game is played on a 4x4 grid, with numbered tiles that can be moved using the arrow keys. When two tiles with the same number touch, they merge into one. The goal is to create a tile with the number 2048.

## How to Play

- Use `W`, `A`, `S`, and `D` keys to move the tiles up, left, down, and right, respectively.
- After each move, a new tile with a value of 2 or 4 will randomly appear on an empty spot on the board.
- When two tiles with the same value collide while moving, they merge into a tile with the sum of their values.
- The game is won when a tile with the value of 2048 is created.
- The game is over when there are no empty spots on the board and no adjacent tiles can be merged.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/yourusername/2048-game.git
    cd 2048-game
    ```

2. Run the game:
    ```sh
    python 2048.py
    ```

## Code Overview

### Main Functions

- `start_game()`: Initializes the game board.
- `random_one_addition(mat)`: Adds a random tile (2 or 4) to an empty spot on the board.
- `add_two_random_start(mat)`: Adds two random tiles at the start of the game.
- `check_game(mat)`: Checks if the player has won by reaching the 2048 tile.
- `merge_tiles_move_left(mat)`, `merge_tiles_move_right(mat)`, `merge_tiles_move_up(mat)`, `merge_tiles_move_down(mat)`: Handle the merging and shifting of tiles for each move direction.
- `move_tiles(move, mat)`: Executes the move based on the player's input.
- `operation(mat)`: Main game loop handling player input and game state.
- `print_board(mat)`: Prints the current state of the board.

### Game Logic

- The game board is represented as a 4x4 matrix.
- Tiles are moved and merged according to the rules of the 2048 game.
- The game checks for win and game over conditions after each move.

### Game Over Condition

The game is over if there are no zeros in the matrix and no adjacent tiles with the same value.


