This repository provides a simple 2D physics simulation in Python and Pygame.

Below is a complete documentation structure you can use for your repository.
2D Collision Simulation

This project is a simple 2D collision simulation (work in progress). It was built for fun and to learn how physics and collision detection work in a digital space.
Features

Circle Collisions: Circles detect when they hit each other and bounce back realistically.

Wall Bouncing: Circles stay inside the window by bouncing off the screen edges.

### Project Structure

main.py: entry point.

App.py: This file manages the game loop. it handles events, updates the logic, and draws everything on the screen.

Circle.py: This file contains the Circle class. Definition of movement and collision checks.

Colors.py: A simple file to store RGB color values.

GameConfigs.py: Contains settings like screen size and physics constants.

### Requirements

Python 3.x

Pygame library

### Steps

Clone this repository to your local machine.

Install the Pygame library by running:
pip install pygame

Start the project by running the main file:
python main.py
