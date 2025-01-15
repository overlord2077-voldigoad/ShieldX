import requests

class CredentialMonitor:
    def __init__(self, api_key):
        self.api_key = api_key
        self.headers = {
            "hibp-api-key": self.api_key,
            "User-Agent": "ShieldX-Monitor"
        }

    def check_email(self, email):
        url = f"https://haveibeenpwned.com/api/v3/breachedaccount/{email}"
        response = requests.get(url, headers=self.headers)
        if response.status_code == 200:
            return {
                "status": "compromised",
                "breaches": response.json(),
                "message": "Credenciais vazadas encontradas."
            }
        elif response.status_code == 404:
            return {"status": "safe", "message": "Nenhum vazamento encontrado."}
        else:
            return {"status": "error", "message": f"Erro: {response.status_code}"}