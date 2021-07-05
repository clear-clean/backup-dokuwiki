import os

AES_PASSWORD = os.environ.get('AES_PASSWORD', 'password').encode('utf-8')

SFTP_SERVER = os.environ.get('SFTP_SERVER', 'localhost')
SFTP_PORT = os.environ.get('SFTP_PORT', 22)
SFTP_USER = os.environ.get('SFTP_USER')
SFTP_PASSWORD = os.environ.get('SFTP_PASSWORD')
