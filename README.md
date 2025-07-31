<div align="center">
    
# Escaping-BRACU

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![PyOpenGL](https://img.shields.io/badge/PyOpenGL-FF6F00?style=flat-square&logo=OpenGL&logoColor=white)

This is the visual version of the game BRACU is playing with our lives. This game is part of the CSE423 course project and is developed using OpenGL. For this game, we were only allowed to use GL_POINTS, Midpoint Line, and Midpoint Circle algorithms. The game is developed using Python and PyOpenGL.

https://github.com/user-attachments/assets/9e27d917-c3b1-4d0a-8cdf-5f77e4bb060b

</div>

## Features
- [x] Restricts the movement area randomly, level by level, using the midpoint line algorithm.
- [x] Generates a movable box using the midpoint line algorithm. The box represents the player.
- [x] Creates randomly generated bubbles using the midpoint circle algorithm. These bubbles will contain deduction values.
- [x] If the box collides with a bubble, the score will decrease randomly between 0.1 - 0.5.
- [x] The goal is to move the box to a designated person without touching any bubbles.
- [x] The score will be updated based on BRACU's grading system.
- [x] The box will not be able to cross the restricted movement area.
- [x] The game will have 11 levels.
- [x] The difficulty will increase as the levels progress.
- [x] Includes pause, play, and restart options.
- [x] Has an intro screen.
- [x] Has an outro screen with credits and a score-based message.
- [x] In levels 3, 8, and 11, an extra "Special-object" will follow the box to reduce the score.

## How to Run
1. Clone the repository or download the zip file:
    ```bash
    git clone https://github.com/badhon495/Escaping-BRACU.git
    ```
2. Navigate to the project directory:
    ```bash
    cd Escaping-BRACU
    ```
3. Run the game:
    ```bash
    python -u game.py
    ```

If the game does not run properly, install PyOpenGL using the following command:
```bash 
pip install PyOpenGL
```

## How to Play
1. Use the arrow keys to move the box.
2. Avoid the bubbles.
3. Reach the designated person.
4. Enjoy the game.

## How to Contribute
1. Fork the repository.
2. Make changes
3. Create a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

<div align="center">
  <p>⭐ Star this repo if you found it helpful!</p>
</div>

