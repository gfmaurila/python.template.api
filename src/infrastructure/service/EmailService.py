class EmailService:
    def SendResetPasswordEmail(self, email: str, code: str):
        link = f"https://meusite.com/reset-password?code={code}"
        print(f"[EMAIL] Link enviado para {email}: {link}")