# Command Line Maze

This is a personal project for my Introduction to Programming I class where 3x3, 4x4, or 5x5 mazes are created using the command line.

## How to Run

1. Download [maze.py](https://github.com/angelo-dlcrz/CSCI-21-Midterm-Project-Maze/blob/main/maze.py).
2. Make sure that you have [Python](https://www.python.org/downloads/) installed in your machine. It is recommended to use Python 3.
3. Run the command line. Change your working directory into the directory where you downloaded [maze.py](https://github.com/angelo-dlcrz/CSCI-21-Midterm-Project-Maze/blob/main/maze.py). Once there, run this.

```console
$ py maze.py
```

## How to Play

1. Once the game has run, you will be prompted to select a level. Select the level that you like.

### Level 1: 3x3 Maze
<pre>
W W W W W W W 
W O W X     W 
W   W   W W W
W           W
W   W   W W W
W   W       W
W W W W W W W
</pre>
### Level 2: 4x4 Maze
<pre>
W W W W W W W W W
W O   X         W
W   W W W W W   W
W           W   W
W   W W W   W W W
W   W   W       W
W   W   W   W   W
W       W   W   W
W W W W W W W W W
</pre>
### Level 3: 5x5 Maze
<pre>
W W W W W W W W W W W
W O   X         W   W
W   W W W   W   W   W
W       W   W       W
W W W   W   W   W W W
W           W       W
W   W   W W W W W   W
W   W       W   W   W
W   W W W   W   W   W
W       W   W       W
W W W W W W W W W W W
</pre>

2. You will then be asked for a start point and end point. The possible points will depend on the maze size. Don't put the same start and end point.

> Note: Current Player Position is denoted by

```console
$ O
```

> Note: End Position is denoted by

```console
$ X
```

### Level 1: 3x3 Maze | Choose a point from 0-8
<pre>
00 01 02
03 04 05
06 07 08
</pre>
### Level 2: 4x4 Maze | Choose a point from 0-15
<pre>
00 01 02 03
04 05 06 07
08 09 10 11
12 13 14 15
</pre>
### Level 3: 5x5 Maze | Choose a point from 0-24
<pre>
00 01 02 03 04
05 06 07 08 09
10 11 12 13 14
15 16 17 18 19
20 21 22 23 24
</pre>

> Note: If you put the same start and end point, the game will still be playable. However, you won't be able to see where the end point is.

3. After giving your start and end points. The game starts. You will be told what available directions you can go to. The only valid directions are North, South, East, and West. You will be told to choose a valid and available direction if the direction you typed is not in the choices.

Enjoy!