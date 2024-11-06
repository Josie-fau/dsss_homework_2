import random


def random_int(smallest, largest):
    """
    Generates a random integer between two specified bounds.

    Parameters:
        smallest (int): The lower bound (inclusive) for the random integer.
        largest (int): The upper bound (inclusive) for the random integer.

    Returns:
        int: A random integer between 'smallest' and 'largest' (inclusive).
    """
    return random.randint(smallest, largest)


def random_op():
    """
    Selects a random arithmetic operation from addition, subtraction, and multiplication.

    Returns:
        str: A randomly chosen operation, one of the following: '+', '-', or '*'.
    """
    return random.choice(['+', '-', '*'])


def calculate(n1, n2, o):
    """
    Calculates the result of a specified arithmetic operation between two numbers.

    Parameters:
        n1 (int): The first integer in the operation.
        n2 (int): The second integer in the operation.
        o (str): The operation to perform, which can be '+', '-', or '*'.

    Returns:
        tuple: A tuple containing:
            - str: A string representation of the math problem in the form "n1 o n2".
            - int: The result of the arithmetic operation.
    """
    p = f"{n1} {o} {n2}"
    if o == '+':
        a = n1 + n2
    elif o == '-':
        a = n1 - n2
    else:
        a = n1 * n2
    return p, a


def math_quiz():
    """
    Plays a math quiz game where the user answers a series of randomly generated math problems.

    Game Flow:
        - The quiz consists of 5 math questions generated randomly.
        - Each question involves two integers and a random arithmetic operation (addition, subtraction, or multiplication).
        - The user is prompted to input their answer to each question.
        - If the user provides the correct answer, they earn a point.
        - If the answer is incorrect, or the user does not provide a valid integer, no points are awarded for that question.
        - The game displays a final score out of 5 at the end.

    How It Works:
        1. The function initializes the score to zero.
        2. For each question:
            - Two random integers and an operation are generated.
            - The question is displayed, and the user inputs their answer.
            - The function checks if the answer is correctly formatted as a single integer without spaces.
            - If the answer is correct, a point is added to the score.
            - If the answer is incorrect or invalid (e.g., not an integer), an error message is displayed, and the user earns no points for that question.
        3. After all questions, the function prints the final score.

    """
    s = 0  # points
    num_questions = 5

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(num_questions):
        int1 = random_int(1, 10)  # first integer between 1 and 10
        int2 = random_int(1, 5)  # second integer between 1 and 5
        operation = random_op()  # random operation +,-,*

        PROBLEM, ANSWER = calculate(int1, int2, operation)  # creates string of the problem and the answer(int)
        print(f"\nQuestion: {PROBLEM}")
        useranswer = input("Your answer: ")

        if " " in useranswer:
            print("You provided an answer with an empty space. This is not the right format. The answer should only "
                  "be given in one integer. No point for you. Try again with the next question\n")
            continue

        try:
            useranswer = int(useranswer)  # attempt to convert to int
            if useranswer == ANSWER:
                print("Correct! You earned a point.\n")
                s += 1  # add a point
            else:
                print(f"Wrong answer. The correct answer is {ANSWER}. No point for you!\n")
        except ValueError:
            print("You did not provide an integer answer. No point for you. Try again with the next question\n")

    print(f"\nGame over! Your score is: {s}/{num_questions}")

if __name__ == "__main__":
    math_quiz()
