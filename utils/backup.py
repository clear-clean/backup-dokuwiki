# from interfaces.loader import LoaderInterface


class BackupHandler:
    def __init__(self, archiver, loader):
        self.archiver = archiver
        self.loader = loader

    def backup(self):
        self.archiver.compress()
        self.loader.put(
            self.archiver.current_archive_path,
            self.archiver.current_archive_file
        )

    # def restore(self, dst='', remote_archive_file=None):
    #     if not remote_archive_file:
    #         remote_archive_file = self.loader.get_last_backup_file()
    #
    #     self.loader.get(
    #         remote_archive_file,
    #         dst
    #     )
    #     self.archiver.uncompress(dst, )
