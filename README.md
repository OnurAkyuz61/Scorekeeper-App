# Scorekeeper - A Dynamic Scoreboard Application

## Overview
Scorekeeper is a dynamic and interactive scoreboard application designed for managing scores, timers, and event information during competitive events. The project is currently under active development and aims to be a robust solution for event organizers.

## Features
- **Score Management:** Update scores for two teams in real time.
- **Timer Control:** Set and reset timers easily.
- **Audience Display:** A clean, fuşya-themed UI for spectators.
- **Cross-Platform Support:** Works seamlessly on Windows and macOS.
- **User Authentication:** Admin-based access with SQLite backend.

## Installation
1. Clone this repository:
   ```bash
   git clone https://github.com/your-username/scorekeeper.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Scoreboard
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage
1. Run the main application:
   ```bash
   python src/main.py
   ```
2. Login using the default admin credentials:
   - **Username:** `admin`
   - **Password:** `1234`

## Project Structure
```
Scoreboard/
├── .venv/  # Virtual environment for isolating project dependencies

Scoreboard/
├── src/
│   ├── audience_display.py
│   ├── login.py
│   ├── main.py
│   ├── scorekeeper.py
│   ├── settings.py
│   ├── utils.py
├── assets/
│   └── icons/
│       ├── scoreboard_icon.ico
│       └── scoreboard_icon.png
├── db/
│   └── users.db
├── requirements.txt
└── README.md
```

## Future Enhancements
- **Animated Updates:** Add animations for score updates.
- **Theming:** Support for dark and light themes.
- **Multi-Language Support:** Interface available in multiple languages.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
