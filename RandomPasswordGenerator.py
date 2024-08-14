import string
import random

def generateRandomPassword(length, characterList, allow_repeats=True):
    password = []
    if allow_repeats:
        for i in range(length):
            randomchar = random.choice(characterList)
            password.append(randomchar)
    else:
        # Ensure no repeated characters
        while len(password) < length:
            randomchar = random.choice(characterList)
            if randomchar not in password:
                password.append(randomchar)
    return "".join(password)

def checkPasswordStrength(password):
    strength = "Weak"
    if len(password) >= 8:
        # Check for a mix of uppercase, lowercase, digits, and special characters
        if any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password) and any(c in string.punctuation for c in password):
            strength = "Strong"
        # Check for a mix of uppercase, lowercase, and digits
        elif any(c.isupper() for c in password) and any(c.islower() for c in password) and any(c.isdigit() for c in password):
            strength = "Moderate"
    return strength

def savePasswordsToFile(passwords):
    with open("generated_passwords.txt", "w") as file:
        for i, pw in enumerate(passwords):
            file.write(f"Password #{i + 1}: {pw}\n")

def main():
    numPasswords = int(input("How many passwords do you want to generate? "))
    print("Generating " + str(numPasswords) + " passwords")
    passwords = []
    print("Minimum length of password should be 3")

    for i in range(numPasswords):
        while True:
            length = int(input("Enter the length of Password #" + str(i + 1) + ": "))
            if length >= 3:
                break
            else:
                print("Minimum length of password should be 3.")
        
        print('''Choose character set for Password #{}:
             1. Digits
             2. Letters
             3. Special characters
             4. Exit
             '''.format(i + 1))
        characterList = ""  # Reset characterList for each password

        while True:
            choice = int(input("Pick a number: "))
            if choice == 1:
                characterList += string.digits
            elif choice == 2:
                characterList += string.ascii_letters
            elif choice == 3:
                characterList += string.punctuation
            elif choice == 4:
                print("Exiting character set selection.")
                break
            else:
                print("Please pick a valid option.")
        
        # Ask if repeating characters are allowed
        allow_repeats = input("Allow repeating characters in this password? (y/n): ").lower() == "y"
        password = generateRandomPassword(length, characterList, allow_repeats)
        passwords.append(password)
   
    print("Generated Passwords:")
    for i, pw in enumerate(passwords):
        print("Password #" + str(i + 1) + " = " + pw)
        strength = checkPasswordStrength(pw)
        print("Password Strength: " + strength)
    
    # Save passwords to a file
    savePasswordsToFile(passwords)
    print("Passwords saved to 'generated_passwords.txt'")
    print("Password generation summary:")
    print(f"Total passwords generated: {len(passwords)}")

if __name__ == "__main__":
    main()