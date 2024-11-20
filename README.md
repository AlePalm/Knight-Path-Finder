# Knight Problem

## Description
Knight Path Finder is a Python program that calculates all the shortest paths a chess knight can take to move from a starting position to an ending position on a chessboard. It also generates a DOT file that graphically represents the paths and converts it into a PNG image.

## Requirements
- Docker Desktop installed.
- Graphviz installed. 
- Python 3.13

## How to Run the Project
1. Start Docker Desktop from the application menu.
2. Open a terminal and navigate to the directory where you extracted the project zip file. 
   - On Windows, you can open the terminal directly in the folder by typing `cmd` in the File Explorer address bar and pressing Enter.
3. In the terminal, run the following command:
   docker-compose run --service-ports knight-path-finder
4. Follow the instructions in the terminal to input the knight's starting and ending positions