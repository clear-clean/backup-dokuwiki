import os

from utils.archive import ZipArchiver
from utils.loader import SftpLoader
from utils.backup import BackupHandler

from settings import SFTP_SERVER, SFTP_USERNAME, SFTP_PASSWORD, SFTP_PORT
from settings import AES_PASSWORD


SOURCE_NAME = 'lab_data_service'
SOURCE_PATH = 'C:\inetpub\wwwroot\lab_data_service\cc_measurements\dump\db.json'
SOURCE_TYPE = 'file'
BACKUP_DIR = os.path.join('backups', 'lab_data_service')
DESTINATION_DIR = 'lab_data_service'


if __name__ == '__main__':
    archiver = ZipArchiver(
        src_name=SOURCE_NAME,
        src_path=SOURCE_PATH,
        src_type=SOURCE_TYPE,
        archive_dir=BACKUP_DIR,
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
