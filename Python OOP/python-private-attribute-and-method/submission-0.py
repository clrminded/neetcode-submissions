class PasswordManager:
    def __init__(self, stored_password):
        self.__stored_password = stored_password
    
    # TODO: Implement the verify_password method
    def verify_password(self, password: str) -> bool:
        return password == self.__stored_password



# Don't modify the code below this line
my_password = PasswordManager("secret123")
print(my_password.verify_password("secret123"))  # Should print: True
print(my_password.verify_password("wrong"))      # Should print: False
