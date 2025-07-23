import hashlib

class Password:
    @staticmethod
    def ComputeSha256Hash(password: str) -> str:
        # Codifica a senha em UTF-8 e calcula o hash SHA256
        sha256Hash = hashlib.sha256()
        sha256Hash.update(password.encode('utf-8'))
        bytesHash = sha256Hash.digest()

        # Converte o array de bytes em uma string hexadecimal
        builder = []
        for byte in bytesHash:
            builder.append(f"{byte:02x}")
        
        return ''.join(builder)
