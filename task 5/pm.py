def num_char(password):
    # This function checks if the password contains both uppercase and lowercase characters
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    return has_upper and has_lower

def capital_small(password):
    # This function checks if the password does not start with a digit or special character
    return not (password[0].isdigit() or not password[0].isalnum())

def special(password):
    # This function checks if the password is in the list of not allowed passwords
    special_characters = set("!@#$%^&*()-_+=[]{};:,.?/<>|\\~`")
    return any(char in special_characters for char in password)

def not_allowed(password):
    # This function checks the length of the password
    return len(password) == 8

def length(password):
    # This function checks if the password is not in the list of disallowed passwords
    not_allowed_passwords = {"A1b#cD3e", "Xy4$Zz7!", "P@ssw0rd", "M!n3r4L^", "T7r$eN8f"}
    return password not in not_allowed_passwords

def validity(password):
    # This function checks the validity of the password based on multiple criteria
    if (length(password) and not_allowed(password) and special(password) and 
            capital_small(password) and num_char(password)):
        print("Password is accepted")
    else:
        print("Sorry, your password is not accepted")

# MAIN PROGRAM
while True:
    password = input("Enter your password: ")
    validity(password)
    retry = input("Do you want to retry (yes/no): ").strip().lower()
    if retry == "no":
        break
