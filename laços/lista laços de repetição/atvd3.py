while True:
    usuario = str(input("Digite o usuário: "))
    senha = input("Digite a senha: ")

    if usuario in senha:
        print("Senha inválida: não pode conter o nome de usuário.")
    else:
        print("Cadastro aceito!")
