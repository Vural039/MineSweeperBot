# Minesweeper Bot

This project is a **Minesweeper bot** that automatically clicks on tiles and reads their colors to make decisions.  
It uses **PyAutoGUI** and **time** libraries to control mouse movements and handle delays.

## Features
- Automatically clicks on tiles.
- Reads pixel colors to determine safe tiles.
- Works on different board sizes (Beginner, Intermediate, Expert).
- Uses coordinates and tile positions defined in the code.

## How to Run
1. Open your Minesweeper game.
2. Make sure the `Base_X`, `Base_Y`, and `Tile_Size` values in the code match your screen resolution.
3. Install required libraries:
   ```bash
   pip install pyautogui

## Important Settings

`Base_X` & `Base_Y`: Starting position of the first tile.

`Tile_Size`: Size of each tile.

`NumOfTilesX` & `NumOfTilesY`: Number of tiles in the game.

`mouthX`, `mouthY`, `glassesX`, `glassesY`: Pixels used to check win or lose state.

## Warning

This bot relies on *pixel colors* and *fixed coordinates*.
If your Minesweeper version, theme, or screen resolution is different, the bot may not work correctly.
You may need to update coordinates and color values in the code.

## Requirements

Python 3.x

PyAutoGUI library

Compatible screen resolution