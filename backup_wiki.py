import os

from utils.archive import ZipArchiver
from utils.loader import SftpLoader
from utils.backup import BackupHandler

from settings import SFTP_SERVER, SFTP_USERNAME, SFTP_PASSWORD, SFTP_PORT
from settings import AES_PASSWORD


SOURCE_NAME = 'wiki'
SOURCE_PATH = 'C:\inetpub\wwwroot\dokuwiki\data'
SOURCE_TYPE = 'dir'
ARCHIVE_DIR = 'backups/wiki'
DESTINATION_DIR = 'wiki'


if __name__ == '__main__':
    archiver = ZipArchiver(
        src_name=SOURCE_NAME,
        src_path=SOURCE_PATH,
        src_type=SOURCE_TYPE,
        archive_dir=ARCHIVE_DIR,
        password=AES_PASSWORD
    )

    loader = SftpLoader(
        server=SFTP_SERVER,
        username=SFTP_USERNAME,
        password=SFTP_PASSWORD,
        port=SFTP_PORT,
        directory=DESTINATION_DIR
    )

    backup_handler = BackupHandler(
        archiver=archiver,
        loader=loader
    )

    backup_handler.backup()
