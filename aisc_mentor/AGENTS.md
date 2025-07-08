# AI Agent Instructions for `aisc_mentor`

This document provides guidelines for AI agents contributing to the `aisc_mentor` project.

## Project Overview

The `aisc_mentor` project is an AI-powered coding mentor. Its goal is to help users learn programming languages by working through real open-source projects. Key components include a repository scanner, a code analyzer, a challenge generator, a learning engine, and progress tracking.

## Coding Conventions

-   **Language**: The primary language for the core application is Python 3.8+.
-   **Style**: Follow PEP 8 guidelines. Use a formatter like Black and a linter like Flake8 if possible. (Setup for these tools will be part of the development process).
-   **Docstrings**: Use Google-style docstrings for all modules, classes, and functions.
-   **Type Hinting**: Use type hints for all function signatures and variable declarations where appropriate.
-   **Modularity**: Strive for small, focused functions and classes. Each module should have a clear responsibility.
-   **Error Handling**: Implement robust error handling. Use specific exception types where possible.
-   **Simplicity**: Prefer clear and straightforward code over overly complex solutions, especially in early development stages. The current stubs are intentionally simple.

## Development Process

1.  **Understand the Plan**: Ensure you understand the current step in the project plan.
2.  **Incremental Implementation**: Implement features incrementally. Focus on getting a basic version working first, then iterate and add complexity.
3.  **Placeholders**: It's acceptable to use placeholders (e.g., mock data, simplified logic) in initial versions, but clearly comment them and plan for their replacement. The current stubs use this approach.
4.  **Testing**:
    *   Write unit tests for new functionality.
    *   Aim for good test coverage.
    *   Tests should be placed in the `tests/` directory, mirroring the `src/` structure.
5.  **Documentation**:
    *   Keep the `README.md` updated with project status and setup instructions.
    *   Add comments to explain complex or non-obvious code sections.
6.  **Commits**:
    *   Make small, atomic commits with clear messages.
    *   Reference the relevant plan step or issue if applicable.

## Specific Module Guidelines

-   **`scanner.py`**: This module will interact with external APIs (e.g., GitHub). Ensure that API keys or sensitive credentials are not hardcoded. Plan for configurability.
-   **`analyzer.py`**: This module will involve complex logic like code parsing (e.g., AST). Start with simplified versions and gradually increase sophistication.
-   **`engine.py`**: The user interaction logic should be clear and user-friendly. Feedback mechanisms will evolve from simple string comparison to more intelligent analysis.
-   **`tracker.py`**: User progress data should be handled carefully. Consider data privacy and integrity.

## Communication

-   If instructions are unclear, ask for clarification.
-   Report any significant deviations from the plan.
-   Provide updates on progress.

By following these guidelines, we can build a robust and effective AI Coding Mentor.
