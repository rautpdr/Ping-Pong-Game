# PING PONG GAME

A classic Pong-style game built using Python and the Turtle graphics module. This project demonstrates Object-Oriented Programming (OOP) concepts to manage game elements like paddles, ball movement, collision detection, and scorekeeping.

## Table of Contents

- [Overview](#overview)
- [How it Works](#how-it-works)
- [Technologies Used](#technologies-used)
- [Lessons Learned](#lessons-learned)

## Overview

The Ping Pong Game is a two-player arcade game where each player controls a paddle to bounce a ball back and forth. The goal is to prevent the ball from passing your paddle while trying to score against the opponent. This project puts a strong emphasis on modular, object-oriented design.

## How it Works

1. **Start the Game**: Run the `main.py` file to begin playing.
2. **Player Controls**:
   - **Left Paddle**:
     - `W`: Move up
     - `S`: Move down
   - **Right Paddle**:
     - `O`: Move up
     - `L`: Move down
3. **Gameplay Mechanics**:
   - The ball automatically moves and bounces off the top and bottom walls.
   - If the ball hits a paddle, it bounces back.
   - If a player misses the ball, the opponent scores a point.
4. **Winning**: First player to reach 5 points wins.

## Technologies Used

- **Python**: Language used to implement the game logic
- **Turtle**: For drawing game elements and creating animations
- **Object-Oriented Programming (OOP)**: To encapsulate behavior in classes like `Paddle`, `Ball`, and `Scoreboard`

## Lessons Learned

Project helped reinforce my understanding of:

- **Class Inheritance & Object Interaction**: Creating multiple classes that interact cleanly
- **Real-Time Game Loops**: Handling continuous updates and smooth movement using `screen.update()` and `time.sleep()`
- **Event Listeners**: Managing user inputs for paddle control
- **Boundary Detection**: Ensuring paddles and the ball behave correctly within the game space
- **Code Cleanup**: Keeping logic readable and maintainable with separation of concerns


