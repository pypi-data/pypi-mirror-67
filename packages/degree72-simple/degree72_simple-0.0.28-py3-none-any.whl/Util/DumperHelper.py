import os
import datetime
from time import time
from uuid import uuid4
import json
import inspect
from Util.JobHelper import debug, get_stack_frame
import tarfile


class DumperHelper:
    def __init__(self, **kwargs):
        now_dt = datetime.datetime.now()
        if kwargs.get('schedule_interval') == 'hour':
            date_folder = now_dt.strftime('%Y-%m-%d-%H')
        elif kwargs.get('schedule_interval') == 'minute':
            date_folder = now_dt.strftime('%Y-%m-%d-%H-%M')
        else:
            date_folder = now_dt.strftime('%Y-%m-%d')

        self.category = kwargs.get('category', '')

        if kwargs.get('file_folder'):
            self.file_folder = kwargs.get('file_folder')
        elif debug():
            stack = inspect.stack()
            self.file_folder = os.path.join(os.path.dirname(get_stack_frame(stack)[1]), 'Dump', date_folder, self.category)
        else:
            stack = inspect.stack()
            self.file_folder = os.path.join(os.path.expanduser('~'), 'PageDump', os.path.basename(os.path.dirname(get_stack_frame(stack)[1])),
                         date_folder, self.category)

        if not os.path.exists(self.file_folder):
            os.makedirs(self.file_folder)

    def dump_page(self, page: str, file_prefix: str = '', file_name=None, **kwargs):
        if not file_name:
            file_name = self.get_file_name(file_prefix)
        file = os.path.join(self.file_folder, file_name)
        with open(file, 'w', encoding='utf-8') as fh:
            fh.write(page)

    def dump_dict(self, item, file_prefix: str = '', file_name=None, **kwargs):
        if not file_name:
            file_name = self.get_file_name(file_prefix)
        file = os.path.join(self.file_folder, file_name)
        with open(file, 'w', encoding='utf-8') as fh:
            json.dump(item, fh)

    @staticmethod
    def get_file_name(file_prefix=''):
        return '_'.join([file_prefix, str(int(time())), str(uuid4())]).strip('_')

    @staticmethod
    def tarfile(source_dir: str, output_file: str = None):
        if output_file is None:
            output_file = os.path.join(os.path.dirname(source_dir) + '.tar.gz')
        with tarfile.open(output_file, "w:gz") as tar:
            tar.add(source_dir, arcname=os.path.basename(source_dir))

    @staticmethod
    def untarfile(source_file: str, output_folder: str = None):
        if output_folder is None:
            output_folder = os.path.dirname(source_file)
        tar = tarfile.open(source_file)
        tar.extractall(output_folder)
        # tar.close()

    @staticmethod
    def unzipfile(source_file: str, output_folder: str = None):
        if output_folder is None:
            output_folder = source_file.strip('.zip')
        import zipfile
        with zipfile.ZipFile(source_file, 'r') as zip_ref:
            zip_ref.extractall(output_folder)


if __name__ == '__main__':
    t = DumperHelper()
    result = t.unzipfile(r"C:\Users\Administrator\test\2020-04-07.zip")
    print(result)

