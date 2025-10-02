# FPL Assistant ⚽

[![Python](https://img.shields.io/badge/python-3.11-blue?logo=python&logoColor=white)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

FPL Assistant is a terminal-based tool to help Fantasy Premier League (FPL) managers make smarter squad decisions, including player lookup, captain recommendations, and comparisons.

---

## Features

- 🔍 **Player Lookup** – Search for any player and view stats, availability, and captaincy recommendations.  
- ⚖️ **Compare Players** – Compare stats and form between two players.  
- 👑 **Squad Captain Optimiser** – Get the best captain choice for your team for the upcoming gameweek.  
- 🔄 **Refresh Data** – Fetch the latest FPL data from the official API.

---

## Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/fpl_assistant.git
cd fpl_assistant
```

2. Create and activate a virtual environment

python -m venv venv
source venv/bin/activate  # Mac/Linux
venv\Scripts\activate     # Windows

3. Install dependencies

pip install -r requirements.txt

---

## Usage

Run the application

python main.py

---

## Project Structure

fpl-assistant/
├── main.py              # Main entry point
├── config.py            # Configuration and constants
├── core/                # Pure business logic functions
├── features/            # Feature orchestration and data handling
├── ui/                  # Terminal UI functions
└── data/                # API fetching and data loading

---

## Contributing

Contributions are welcome! Please submit a pull request or open an issue.
