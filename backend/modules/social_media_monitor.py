import random

class SocialMediaMonitor:
    def analyze_activity(self, account_name):
        simulated_risks = ["Login suspeito", "Alteração de senha", "Postagem imprópria"]
        return {
            "account": account_name,
            "risks": random.choices(simulated_risks, k=2),
            "message": "Atividade monitorada com sucesso."
        }
