class AccessControl:
    def __init__(self):
        self.access_logs = []

    def log_access(self, user, resource, action):
        self.access_logs.append({"user": user, "resource": resource, "action": action})
        return {"message": f"Ação registrada: {action} em {resource} por {user}."}

    def get_logs(self):
        return self.access_logs
