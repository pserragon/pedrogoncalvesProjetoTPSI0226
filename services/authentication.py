import re


# LOGIN
def login():

    utilizador_correto = "admin"
    password_correta = "ByteTech123"

    print("\n=== LOGIN BYTE TECH ===")

    username = input("Username: ")
    password = input("Password: ")

    # REGEX USERNAME
    padrao_username = r"^[A-Za-z0-9_]{3,20}$"

    resultado_username = re.match(
        padrao_username,
        username
    )

    if resultado_username is None:

        print("\nUsername inválido.")
        return False

    else:

        print("\nUsername válido.")
        print("Grupo encontrado:", resultado_username.group())
        print("Posição:", resultado_username.span())

    # REGEX PASSWORD
    padrao_password = r"^[A-Za-z0-9@#\$%\!\?]{6,20}$"

    resultado_password = re.match(
        padrao_password,
        password
    )

    if resultado_password is None:

        print("\nPassword inválida.")
        return False

    else:

        print("\nPassword válida.")
        print("Grupo encontrado:", resultado_password.group())
        print("Posição:", resultado_password.span())

    # VERIFICAÇÃO LOGIN
    if (
        username == utilizador_correto
        and
        password == password_correta
    ):

        print("\nLogin realizado com sucesso!")
        return True

    else:

        print("\nCredenciais incorretas.")
        return False