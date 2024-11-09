# **Math Quiz**

This project is a **Python package** for a basic math quiz. The quiz presents five randomly generated questions involving addition, subtraction, or multiplication. Players receive **immediate feedback** after each answer, with a final score out of five provided at the end.

## **Files**

- **math_quiz.py**: Contains the main logic for generating and running the math quiz, including random question generation, user input handling, and scoring.
- **test_math_quiz.py**: Contains unit tests to validate the functionality of `math_quiz.py`, ensuring correct question generation, scoring, and feedback.
- **setup.py**: Configuration file for installing the package, supporting easy installation via `pip`.

## **Features**

- **Question Types**: Addition, subtraction, and multiplication questions with:
  - **int1**: Random integer between 0 and 5.
  - **int2**: Random integer between 0 and 10.
- **Difficulty**: Single difficulty level, suitable for quick practice.
- **Feedback**: Provides immediate feedback after each answer.
- **Scoring**: Each correct answer is worth one point; the quiz has five questions, so the maximum score is five.

## **Installation**

To install the Math Quiz package, navigate to the project directory and run:

```bash
pip install git+https://github.com/Josie-fau/dsss_homework_2.git
```

## **Usage**

To start the quiz, run the following command:

```bash
python -m math_quiz
```

### **Example Question**

```plaintext
Question: What is 3 + 4?
Your answer: 7
Correct! You earned a point.
```

## **Testing**

To run the tests in `test_math_quiz.py`, use the following command:

```bash
python -m unittest test_math_quiz.py
```
## **Dependencies**
random: For generating random integers.

unittest: For running the test cases.
