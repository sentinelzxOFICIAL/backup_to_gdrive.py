import os
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

def authenticate():
    gauth = GoogleAuth()
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def upload_files(drive, folder_id, files):
    for file_name in files:
        file = drive.CreateFile({'parents': [{'id': folder_id}]})
        file.SetContentFile(file_name)
        file.Upload()
        print(f"Uploaded {file_name}")

def main():
    backup_folder_id = 'your_google_drive_folder_id'  # Substitua pelo ID da sua pasta no Google Drive
    files_to_backup = ['file1.txt', 'file2.txt']  # Substitua com os arquivos que deseja fazer backup

    drive = authenticate()
    upload_files(drive, backup_folder_id, files_to_backup)

if __name__ == "__main__":
    main()
