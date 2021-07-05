import os
import datetime as dt
import pyzipper

from settings import AES_PASSWORD


class Archiver:
    def __init__(self, src_name, src_path, zip_dir):
        self.source = {
            'name': src_name,
            'path': src_path
        }
        self.zip_dir = zip_dir

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
        zip_path = os.path.join(self.zip_dir, self.generate_file_name())
        with pyzipper.AESZipFile(
                zip_path,
                'w',
                compression=pyzipper.ZIP_DEFLATED,
                encryption=pyzipper.WZ_AES
        ) as zip_file:
            zip_file.pwd = AES_PASSWORD
            self.zip_directory(zip_file)

    def uncompress(self, file_name, destination):
        zip_path = os.path.join(self.zip_dir, file_name)
        with pyzipper.AESZipFile(zip_path) as zip_file:
            zip_file.pwd = AES_PASSWORD
            zip_file.extractall(destination)
