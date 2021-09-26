@echo off
cd C:\inetpub\wwwroot\lab_data_service\cc_measurements
CALL venv\scripts\activate.bat
python manage.py dumpdata > dump/db.json

cd C:\Users\Malte\Desktop\backup-dokuwiki
CALL venv\scripts\activate.bat
python backup_lab_data_service.py
