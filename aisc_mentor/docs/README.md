# AI Source Code Mentor (aisc_mentor)

Welcome to the AI Source Code Mentor! This project aims to help users deeply learn any programming language by manually coding real production-level open-source projects.

## Vision

The AI intelligently searches GitHub to find high-quality, actively maintained, and beginner-accessible open-source repositories in the chosen language. It then:

- Breaks down complex codebases into bite-sized, logically sequenced units.
- Converts them into hands-on coding challenges that users must write out manually, reinforcing real understanding.
- Explains the context, architecture, and purpose behind each snippet.
- Tracks progress across repositories.

## Core Features (Planned)

-   **Smart Repo Scanner**: Filters repos based on stars, documentation quality, modularity, and beginner-friendliness.
-   **Code-First Learning**: Users must write every line manually—no autogeneration or copy-paste.
-   **Live Feedback**: Error detection, syntax hints, architecture notes — only when asked.
-   **Progressive Disclosure**: Only reveals the next chunk when previous is completed correctly.
-   **Tech Stack Selector**: Choose TypeScript, Rust, Go, Python, etc.
-   **Build What Matters**: Guide users through building features from real apps.

## Current Status

Project structure initialized. Basic placeholder modules created for:
- CLI (`src/main.py`)
- Repository Scanner (`src/scanner.py`)
- Code Analyzer/Challenge Generator (`src/analyzer.py`)
- Learning Engine (`src/engine.py`)
- Progress Tracker (`src/tracker.py`)

## Setup (Placeholder)

```bash
# Clone the repository (once public)
# git clone <repo_url>
cd aisc_mentor

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate # or .venv\Scripts\activate for Windows

# Install dependencies
pip install -r requirements.txt

# Run the application
python src/main.py
```

## Contributing
Details to be added. Check `AGENTS.md` for AI collaboration guidelines.
