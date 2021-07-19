import os

from utils.archive import ZipArchiver
from utils.loader import SftpLoader
from utils.backup import BackupHandler

from settings import SFTP_SERVER, SFTP_USERNAME, SFTP_PASSWORD, SFTP_PORT
from settings import AES_PASSWORD


SOURCE = 'my-directory'
BACKUP_DIR = 'backups'


def get_last_backup():
    backup_files = [
        file
        for file in os.listdir(BACKUP_DIR)
        if os.path.isfile(os.path.join(BACKUP_DIR, file))
    ]
    return backup_files[-1]

#
# def main():
#     print('Archiving my-directory.')
#     archiver = ZipArchiver('my-directory', 'my-directory', BACKUP_DIR)
#     archiver.compress()
#
#     print('Unarchiving my-directory in tmp')
#     last_backup = get_last_backup()
#     archiver.uncompress(last_backup, 'tmp')

if __name__ == '__main__':
    archiver = ZipArchiver(
        src_name=SOURCE,
        src_path=SOURCE,
        archive_dir=BACKUP_DIR,
        password=AES_PASSWORD
    )

    loader = SftpLoader(
        server=SFTP_SERVER,
        username=SFTP_USERNAME,
        password=SFTP_PASSWORD,
        port=SFTP_PORT
    )

    backup_handler = BackupHandler(
        archiver=archiver,
        loader=loader
    )

    # backup_handler.backup()
    backup_handler.restore(dst='20210712_132522_my-directory.zip', remote_archive_file='20210712_132522_my-directory.zip')
