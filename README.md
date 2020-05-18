# 2048 in a shell

![Gameplay](https://i.github-camo.com/252baa5513f36a05b6566c1bb509b6afc6ef58b1/68747470733a2f2f7261772e6769746875622e636f6d2f766f69642d6d61696e2f61746f6d2d323034382f6d61737465722f706f7765722d6d6f64652d64656d6f2e676966)

## What is 2048?


2048 is a single-player sliding block puzzle game designed by an Italian web developer. The game's objective is to slide numbered tiles on a grid to combine them to create a tile with the number 2048. 

*On our version of 2048, player can decide the winning score.*

## About Game

2048 is played on a (n x n) grid, with numbered tiles that slide smoothly when a player moves them using the four arrow keys( or W,A,S,D keys in our case). 

#### Some rules

* Every turn, a new tile will randomly appear in an empty spot on the board with a value of 2 .

* Tiles slide as far as possible in the chosen direction until they are stopped by either another tile or the edge of the grid. 

* If two tiles of the same number collide while moving, they will merge into a tile with the total value of the two tiles that collided. The resulting tile cannot merge with another tile again in the same move.

* If a move causes three consecutive tiles of the same value to slide together, only the two tiles farthest along the direction of motion will combine.

* The game is won when a tile with a value of winning score appears on the board

## About _CODE_

**This code provides terminal based 2048 game with movement keys (W,A,S,D)**

 The code mainly includes 3 modules.
 
 1. [msvcrt module](https://docs.python.org/2/library/msvcrt.html)
 2. [os module](https://docs.python.org/3/library/os.html)
 3. [random module](https://docs.python.org/3/library/random.html)

### How to run
1. Running the code in terminal will first ask the grid size which the player can enter. If no size is entered, a default size of 5 is chosen. A winning score is asked to the player which is to be entered as a power of 2(*eg. For 32 score, 5 should be entered*). A default 2048 score is chosen if nothing is chosen.

![Size and Score](https://drive.google.com/file/d/1aeQ-VvZWhfesTkvP2YFtxogSCBH1uQwS/view?usp=sharing)

2. Random 2 will appear at any tile on the grid. The user needs W,A,S,D keys to move these tiles while colliding with other tiles to make a greater number.

![Grid display](https://drive.google.com/file/d/1eQ2uHlKPjeVyw5Ah5S9wzYGobKsUfRjA/view?usp=sharing)

3. Player can press p instead of W,A,S,D keys to end the game in the middle without winning or losing.
4. If winning score is reached the player wins the game else if the grid is full with no movement left, the player lose.
![Win Display](https://drive.google.com/file/d/1zLQqrfkmlBNDP_O9OuTBhiiEnmwMp_kr/view?usp=sharing)


## Built with

* Python (programming language)
* Jupyter notebook 
