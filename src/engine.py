# Learning Engine and Feedback Mechanism

def start_learning_session(challenges: list):
    """
    Manages the learning session, presenting challenges and checking user input.
    (Simplified initial version)
    """
    print("\nStarting learning session...")
    for i, challenge in enumerate(challenges):
        print(f"\n--- Challenge {i+1}: {challenge['description']} ---")
        print("Context: " + challenge.get('explanation', 'No context provided.'))
        print("\nType the following code exactly as shown:")
        print("-" * 20)
        print(challenge['code_to_write'])
        print("-" * 20)

        while True:
            user_code_lines = []
            print("Enter your code line by line. Type 'DONE' on a new line when finished, or 'HINT' for a hint.")

            line_num = 0
            while True:
                line_num +=1
                line = input(f"{line_num:02d} | ")
                if line.strip().upper() == 'DONE':
                    break
                if line.strip().upper() == 'HINT':
                    print("Hint: Try to match the structure and syntax precisely. (More specific hints later!)")
                    continue
                user_code_lines.append(line)

            user_code = "\n".join(user_code_lines)

            # Simple string comparison for now
            if user_code.strip() == challenge['code_to_write'].strip():
                print("\nCorrect! Well done.")
                break
            else:
                print("\nNot quite right. Let's try that again.")
                # More detailed feedback would go here in a real version
                # e.g., diffing, syntax checking.
                # For now, show the difference for debugging this simple version.
                print("\nExpected:")
                print(challenge['code_to_write'])
                print("\nYou typed:")
                print(user_code)
                print("-" * 10)

    print("\n--- Learning session complete! ---")

if __name__ == '__main__':
    # Mock challenges for testing the engine
    mock_challenges_for_engine = [
        {
            "unit_id": "test_unit_1",
            "description": "Define a simple function.",
            "code_to_write": "def greet(name):\n    return f\"Hello, {name}!\"",
            "explanation": "Functions are defined using 'def' keyword."
        },
        {
            "unit_id": "test_unit_2",
            "description": "Call the function.",
            "code_to_write": "message = greet(\"World\")\nprint(message)",
            "explanation": "Assign the function's return value to a variable and print it."
        }
    ]
    start_learning_session(mock_challenges_for_engine)
