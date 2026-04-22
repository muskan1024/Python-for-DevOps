import os
import datetime
import shutil

def backup(source, destination):
    today = datetime.date.today()
    backup_file = os.path.join(destination, f"backup_{today}")
    # .path.join(destination, f"backup_{today}.tar.gz")
    shutil.make_archive(backup_file, 'gztar', source )
    # shutil.make_archive(backup_file.replace(".tar.gz", ""), 'gztar', source )
    
source = "/mnt/d/DevOps/Python/practice"
destination = "/mnt/d/DevOps/Python/project/backups"
backup(source, destination)