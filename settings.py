import os
from dotenv import load_dotenv

load_dotenv()

AES_PASSWORD = os.environ.get('AES_PASSWORD', 'password').encode('utf-8')

SFTP_SERVER = os.getenv('SFTP_SERVER')
SFTP_PORT = int(os.environ.get('SFTP_PORT', '22'))
SFTP_USERNAME = os.environ.get('SFTP_USERNAME')
SFTP_PASSWORD = os.environ.get('SFTP_PASSWORD')
