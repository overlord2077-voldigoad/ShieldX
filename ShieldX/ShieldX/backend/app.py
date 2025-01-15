from flask import Flask, request, jsonify
from modules.threat_prediction import ThreatPredictor
from modules.credential_monitor import CredentialMonitor
from modules.access_control import AccessControl
from modules.social_media_monitor import SocialMediaMonitor
from modules.backup_manager import BackupManager

app = Flask(__name__)

# Inicializar módulos
threat_predictor = ThreatPredictor()
credential_monitor = CredentialMonitor(api_key="SUA_API_KEY")
access_control = AccessControl()
social_media_monitor = SocialMediaMonitor()
backup_manager = BackupManager()

# Rotas de API
@app.route("/predict-threats", methods=["GET"])
def predict_threats():
    threats = threat_predictor.predict_threats()
    return jsonify({"status": "success", "predicted_threats": threats})

@app.route("/check-credentials", methods=["GET"])
def check_credentials():
    email = request.args.get("email")
    if not email:
        return jsonify({"message": "E-mail não fornecido."}), 400
    result = credential_monitor.check_email(email)
    return jsonify(result)

@app.route("/log-access", methods=["POST"])
def log_access():
    data = request.json
    if not data:
        return jsonify({"message": "Dados não fornecidos."}), 400
    result = access_control.log_access(data["user"], data["resource"], data["action"])
    return jsonify(result)

@app.route("/analyze-social", methods=["GET"])
def analyze_social():
    account_name = request.args.get("account_name")
    if not account_name:
        return jsonify({"message": "Nome da conta não fornecido."}), 400
    result = social_media_monitor.analyze_activity(account_name)
    return jsonify(result)

@app.route("/manage-backup", methods=["POST"])
def manage_backup():
    data = request.json
    if not data:
        return jsonify({"message": "Dados de backup não fornecidos."}), 400
    result = backup_manager.perform_backup(data["directory"])
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)