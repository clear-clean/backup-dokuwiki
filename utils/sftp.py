import paramiko

from settings import SFTP_SERVER, SFTP_USER, SFTP_PASSWORD, SFTP_PORT


class Sftp:
    def __init__(self):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            SFTP_SERVER,
            username=SFTP_USER,
            password=SFTP_PASSWORD,
            port=SFTP_PORT
        )

    def list_files(self):
        pass

    def put(self, filepath):
        pass

    def get(self, filename):
        pass
