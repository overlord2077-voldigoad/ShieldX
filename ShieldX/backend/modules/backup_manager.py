import os
import shutil

class BackupManager:
    def perform_backup(self, directory):
        try:
            backup_dir = f"{directory}_backup"
            shutil.copytree(directory, backup_dir)
            return {"status": "success", "message": f"Backup realizado em {backup_dir}"}
        except Exception as e:
            return {"status": "error", "message": str(e)}