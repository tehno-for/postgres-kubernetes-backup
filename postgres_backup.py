import subprocess
import datetime
import os

def manage_backup_files(backup_dir, db_name, max_files):
    files = sorted(
        [f for f in os.listdir(backup_dir) if f.startswith(db_name) and f.endswith(".sql")],
        key=lambda x: os.path.getmtime(os.path.join(backup_dir, x))
    )
    while len(files) > max_files:
        os.remove(os.path.join(backup_dir, files.pop(0)))

def backup_postgres(backup_dir='./'):
    if not os.path.exists(backup_dir):
        os.makedirs(backup_dir)
    
    db_name = os.getenv('POSTGRES_NAME')
    user = os.getenv('POSTGRES_USER')
    password = os.getenv('POSTGRES_PASSWORD')
    host = os.getenv('POSTGRES_HOST')
    port = int(os.getenv('POSTGRES_PORT', 5432))
    max_files = os.getenv('MAX_FILES')
    
    timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
    backup_file = f"{backup_dir}{db_name}_backup_{timestamp}.sql"
    
    env = {"PGPASSWORD": password}
    command = [
        "pg_dump", "-h", host, "-p", str(port), "-U", user, "-F", "c", "-b", "-v", "-f", backup_file, db_name
    ]    

    try:
        subprocess.run(command, check=True, env=env)
        print(f"Backup successful for database {db_name}: {backup_file}")
        manage_backup_files(backup_dir, db_name)
    except subprocess.CalledProcessError as e:
        print(f"Error during backup: {e}")

# Run functions for both databases
backup_postgres(backup_dir="/backup/")
