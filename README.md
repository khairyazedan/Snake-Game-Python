# 🐍 Snake Game

A classic Snake game built with **Python** and **Pygame**. Eat the apple, grow your snake, and avoid crashing into yourself. Features background music, sound effects, and a game over screen.

---

## 🎮 Gameplay

- Control the snake using the **arrow keys**
- Eat the apple to grow longer and increase your score
- Avoid colliding with yourself — game over if you do!
- Press **Enter** to restart after game over
- Press **Escape** to quit

---

## ✨ Features

- 🎵 Background music that plays throughout the game
- 🔊 Sound effects for eating and crashing
- 📊 Live score display
- 🖼️ Custom background and sprite images
- 🔄 Restart without closing the window

---

## 🛠️ Tech Stack

- **Language:** Python 3
- **Library:** Pygame

---

## 📁 Project Structure

```
snake-game/
├── snake.py               # Main game file
├── block.jpg              # Snake body sprite
├── eyes.jpg               # Apple sprite
├── bg_picture.jpg         # Background image
├── background_music.mp3   # Background music
├── eat.mp3                # Eat sound effect
├── crash.mp3              # Crash sound effect
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.x installed
- Pygame library

### Install Pygame

```bash
pip install pygame
```

### Run the Game

```bash
python snake.py
```

---

## 🕹️ Controls

| Key | Action |
|-----|--------|
| ⬆️ Arrow Up | Move up |
| ⬇️ Arrow Down | Move down |
| ⬅️ Arrow Left | Move left |
| ➡️ Arrow Right | Move right |
| Enter | Restart after game over |
| Escape | Quit the game |

---

## 🏗️ Code Structure

| Class | Responsibility |
|-------|---------------|
| `Snake` | Handles snake movement, direction, drawing, and growth |
| `Eyes` | Handles apple rendering and random repositioning |
| `Game` | Main game loop, collision detection, score, sound, and reset |

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
