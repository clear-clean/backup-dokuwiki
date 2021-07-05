import os

from utils.archive import Archiver


SOURCE = 'my-directory'
BACKUP_DIR = 'backups'


def get_last_backup():
    backup_files = [
        file
        for file in os.listdir(BACKUP_DIR)
        if os.path.isfile(os.path.join(BACKUP_DIR, file))
    ]
    return backup_files[-1]


if __name__ == '__main__':
    print('Archiving my-directory.')
    archiver = Archiver('my-directory', 'my-directory', BACKUP_DIR)
    archiver.compress()

    print('Unarchiving my-directory in tmp')
    last_backup = get_last_backup()
    archiver.uncompress(last_backup, 'tmp')
