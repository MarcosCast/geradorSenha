import random
import string

def generate_password(length):
    """Esta função gera uma senha aleatória com o comprimento especificado pelo usuário"""
    
    caracteres = string.ascii_letters + string.digits + string.punctuation
    
    password = ""
    
    for i in range(length):
        password += random.choice(caracteres)

    return password

length = int(input("Qual o comprimento da senha que você deseja? "))

password = generate_password(length)

print("Senha gerada:", password)
