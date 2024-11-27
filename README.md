# TheGameOfLife
A Python simulation of John Conway's Game of Life

## Project Description
The Game of Life, created by mathematician John Conway, is a cellular automaton where simple rules determine the evolution of a grid of cells. Each cell can be alive or dead, and its state evolves over discrete time steps based on the states of its neighbors. This project provides an interactive Python implementation of the Game of Life, offering features such as adjustable grid sizes, simulation speed, and the ability to pause and resume the game.

## Features
- **Adjustable Grid Sizes**: Choose between small, medium, and large grids to customize your simulation experience.
- **Simulation Control**: Pause and resume the game at any time.
- **Speed Adjustment**: Modify the evolution speed to observe patterns at your own pace.
- **Toroidal Grid**: Edges wrap around to simulate an infinite grid.

## Requirements
This project requires Python 3.8 or higher. Additionally, the following libraries are needed:
- **NumPy**
- **Pygame**

### Installing the Libraries
#### On Windows
1. Open Command Prompt or PowerShell.
2. Use the following command to install the required libraries:
   ```bash
   python -m pip install numpy pygame

#### On Linux/Mac
1. Open Terminal.
2. Use the following command to install the required libraries:
   ```bash
   pip install numpy pygame

## How to Run
1. Clone this repository.
   ```bash
   git clone https://github.com/LuigiRuotolo00/TheGameOfLife.git
   cd TheGameOfLife
2. Run the main script.
   ```bash
   python TheGameOfLife.py
