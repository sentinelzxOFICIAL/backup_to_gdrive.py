# Termux Backup Automation

A script to automate backups of important files in Termux to Google Drive.

## Features

- Authenticates with Google Drive using OAuth2.
- Uploads specified files to a designated folder on Google Drive.
- Simple and customizable.

## Requirements

- Termux
- Python 3
- PyDrive

## Installation

1. Update and upgrade Termux packages:
    ```bash
    pkg update && pkg upgrade
    ```
2. Install Git and Python:
    ```bash
    pkg install git python
    ```
3. Install PyDrive:
    ```bash
    pip install pydrive
    ```
4. Clone the repository:
    ```bash
    git clone https://github.com/sentinelzxOFICIAL/backup_to_gdrive.py
    ```

## Setup

1. Follow the instructions to set up Google API credentials:
   - Go to the [Google Developer Console](https://console.developers.google.com/)
   - Create a new project
   - Enable the Google Drive API for the project
   - Create OAuth 2.0 Client IDs and download the `credentials.json` file
   - Place `credentials.json` in the `termux-backup-automation` directory

## Usage

1. Run the script:
    ```bash
    python backup_to_gdrive.py
    ```
2. Follow the prompts to authenticate with Google Drive.

## Contributing

Feel free to fork this repository and submit pull requests. Any contributions, whether they're bug fixes, enhancements, or new features, are welcome.

## License

This project is licensed under the MIT License.
