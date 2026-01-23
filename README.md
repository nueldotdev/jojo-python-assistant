# Jojo Assistant

Jojo Assistant is an early prototype of a personal assistant written in Python. This project started as an experiment to explore building a small, extensible assistant; the current prototype can open YouTube videos and will be expanded with more features over time.

Status: Experimental / prototype

## Features
- Opens YouTube videos (current prototype capability)
- Designed to be extended with new commands and integrations
- Lightweight and Python-based so it's easy to modify

## Goals / Roadmap
- Improve command parsing and natural language handling
- Add integrations (media control, messaging, web search, etc.)
- Add tests, CI, and packaging
- Improve documentation and onboarding for contributors

## Requirements
- Python 3.8+ recommended
- (Optional) A virtual environment tool such as venv or virtualenv

## Installation (local development)
1. Clone the repository:
   ```
   git clone https://github.com/nueldotdev/jojo-python-assistant.git
   cd jojo-python-assistant
   ```

2. Create and activate a virtual environment:
   ```
   python -m venv .venv
   source .venv/bin/activate   # macOS / Linux
   .venv\Scripts\activate      # Windows (PowerShell/CMD)
   ```

3. Install dependencies (if a `requirements.txt` exists):
   ```
   pip install -r requirements.txt
   ```

If there is no `requirements.txt`, inspect the repository for the main script and any imports to determine required packages.

## Running the assistant
The repository currently contains a small prototype, run it with:

```
python jojo.py
```

The current prototype mainly supports opening YouTube videos and searching for info on Wikipedia through the wiki-api.

## Contributing
Contributions are welcome.

- File an issue to propose features or report bugs.
- Open PRs for improvements. Keep changes small and focused.
- If you add dependencies, include or update `requirements.txt`.
- Add tests for new features when possible.

Suggested labels: enhancement, bug, docs, help wanted.

