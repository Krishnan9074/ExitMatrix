# Codebase Analyzer and Challenge Generator

def analyze_codebase(repo_url: str):
    """
    Analyzes a codebase to identify learning units.
    (Simplified initial version)
    """
    print(f"Analyzing codebase at {repo_url}...")
    # Placeholder for actual analysis (AST parsing, etc.)
    # This would involve cloning the repo, parsing files.
    # For now, returns mock challenges.
    mock_challenges = [
        {
            "unit_id": "unit_1",
            "description": "Understand the basic structure of a Flask route.",
            "code_to_write": """\
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'
""",
            "explanation": "This is a simple Flask application. The `@app.route('/')` decorator defines an endpoint for the root URL. When accessed, the `hello_world` function is called."
        },
        {
            "unit_id": "unit_2",
            "description": "Add a new route that accepts a parameter.",
            "code_to_write": """\
@app.route('/user/<username>')
def show_user_profile(username):
    return f'User {username}'
""",
            "explanation": "This route demonstrates how to capture URL parameters. The `<username>` part in the route is passed as an argument to the `show_user_profile` function."
        }
    ]
    return mock_challenges

if __name__ == '__main__':
    challenges = analyze_codebase("https://github.com/pallets/flask")
    for challenge in challenges:
        print(f"\nChallenge: {challenge['description']}")
        print("Code to write manually:")
        print(challenge['code_to_write'])
