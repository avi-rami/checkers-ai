# Checkers AI

A Python implementation of the classic Checkers game with an AI opponent using the Minimax algorithm.

## Features

- Classic Checkers gameplay with standard rules
- AI opponent using Minimax algorithm with alpha-beta pruning
- Graphical user interface using Pygame
- Game state tracking and move validation
- Support for piece promotion to kings

## Requirements

- Python 3.x
- Pygame

## Installation

1. Clone the repository:
```bash
git clone https://github.com/avi-rami/checkers-ai.git
cd checkers-ai
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## How to Play

Run the game using:
```bash
python main.py
```

### Game Rules
- Players take turns moving their pieces diagonally
- Regular pieces can only move forward
- Kings can move both forward and backward
- Pieces can capture opponent's pieces by jumping over them
- When a piece reaches the opposite end of the board, it becomes a king
- The game ends when one player captures all opponent's pieces or blocks all possible moves

## Project Structure

- `main.py` - Entry point of the game
- `checkers/` - Core game logic
  - `board.py` - Board representation and management
  - `piece.py` - Piece class and movement logic
  - `game.py` - Game state and rules
  - `menu.py` - Game menu interface
  - `constants.py` - Game constants and configurations
- `minimax/` - AI implementation
  - `algorithm.py` - Minimax algorithm with alpha-beta pruning

## Contributing

Feel free to submit issues and enhancement requests!