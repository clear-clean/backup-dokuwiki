import paramiko


class SftpLoader:
    def __init__(self, server, username, password, port):
        self.client = paramiko.SSHClient()
        self.client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.client.connect(
            server,
            username=username,
            password=password,
            port=port
        )

    def list_files(self):
        pass

    def put(self, src, dst):
        with self.client.open_sftp() as sftp:
            sftp.put(src, dst)

    def get(self, src, dst):
        with self.client.open_sftp() as sftp:
            sftp.get(src, dst)

    def get_last_backup_file(self):
        files = self.client.listdir()
        return files[-1]
