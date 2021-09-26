import datetime as dt
import os
import pyzipper


class ZipArchiver:
    def __init__(self, src_name, src_path, archive_dir, password):
        self.source = {
            'name': src_name,
            'path': src_path
        }
        self.archive_dir = archive_dir
        self.password = password
        self.current_archive_file = None

    @property
    def current_archive_path(self):
        return os.path.join(self.archive_dir, self.current_archive_file)

    def generate_file_name(self):
        now = dt.datetime.now()
        timestamp = now.strftime('%Y%m%d_%H%M%S')
        return '{ts}_{src}.zip'.format(ts=timestamp, src=self.source['name'])

    def zip_directory(self, zip_file):
        path = self.source['path']
        for root, dirs, files in os.walk(path):
            for file in files:
                zip_file.write(
                    os.path.join(root, file),
                    os.path.relpath(
                        os.path.join(root, file),
                        os.path.join(path, '..')
                    )
                )

    def compress(self):
        self.current_archive_file = self.generate_file_name()
        current_archive_path = os.path.join(
            self.archive_dir,
            self.current_archive_file
        )
        with pyzipper.AESZipFile(
                current_archive_path,
                'w',
                compression=pyzipper.ZIP_DEFLATED,
                encryption=pyzipper.WZ_AES
        ) as zip_file:
            zip_file.pwd = self.password
            self.zip_directory(zip_file)

    def uncompress(self, filename, destination):
        zip_path = os.path.join(self.archive_dir, filename)
        with pyzipper.AESZipFile(zip_path) as zip_file:
            zip_file.pwd = self.password
            zip_file.extractall(destination)
