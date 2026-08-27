from hashlib import sha256


def hash_password(password: str) -> str:
    return sha256(password.encode('utf-8')).hexdigest()


def check_password(password: str, hashed_password: str) -> bool:
    return hash_password(password) == hashed_password


password = input("Registre uma senha: ")

password_hash = hash_password(password)
print(password_hash)

while True:
    password = input("Digite sua senha: ")
    if check_password(password, password_hash):
        print("Senha correta")
        break
    else:
        print("Senha incorreta, tente novamente")
