import os

import paramiko


class SftpLoader:
    def __init__(self, server, username, password, port, directory):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            server,
            username=username,
            password=password,
            port=port
        )
        self.directory = directory

    def list_files(self):
        pass

    def put(self, src_file, dst_file):
        with self.client.open_sftp() as sftp:
            sftp.put(src_file, self.directory + '/' + dst_file)

    def get(self, src_file, dst_file):
        with self.client.open_sftp() as sftp:
            sftp.get(src_file, self.directory + '/' + dst_file)

    def get_last_backup_file(self):
        files = self.client.listdir()
        return files[-1]
