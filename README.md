This project is a Python-based password generator designed to create random, secure passwords. It offers customization options for users to specify password length, character sets, and whether characters can be repeated within a password. Here’s a breakdown of the key functionalities:

Key Features:

Password Generation:
The program can generate multiple passwords based on user input.
Users can specify the desired length of each password (with a minimum length of 3 characters).
The character set for each password can be customized to include:
Digits (0-9)
Letters (both uppercase and lowercase)
Special Characters (e.g., @, #, $, etc.)
Users can choose whether to allow repeating characters within the password.

Password Strength Check:
After generating a password, the program evaluates its strength.
Weak: Passwords shorter than 8 characters or lacking variety in character types.
Moderate: Passwords that include a mix of uppercase letters, lowercase letters, and digits but lack special characters.
Strong: Passwords that include a mix of uppercase letters, lowercase letters, digits, and special characters.

Save Passwords to File:
The generated passwords are saved to a file named generated_passwords.txt, with each password labeled sequentially.
The file allows users to securely store and retrieve the generated passwords.

User Interaction:
The program is interactive, prompting users to input their preferences for each password.
Users are guided through the selection process for the password length, character set, and repetition rules.

Use Cases:
Personal Use: Individuals who need to generate secure passwords for online accounts or personal security.
IT Professionals: A quick tool for generating secure passwords for systems and applications.
Educational Purposes: Demonstrates concepts like randomization, user input handling, file operations, and conditional logic in Python.
How It Works:
The user is prompted to input the number of passwords they wish to generate.
For each password, the user specifies the length and selects the character types they want to include.
The program generates a random password based on the selected options and evaluates its strength.
The generated passwords are displayed, along with their strength ratings, and saved to a text file for future reference.
