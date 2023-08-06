# -*- coding: utf-8 -*-
"""
module for merging video files
"""

from pathlib import Path

from lockfile import LockFile
from simpleutils.time import unix2dt
from ffmpy import FFmpeg

from sail_utils import LOGGER
from sail_utils.oss.utilities import OSSUtility


class Merger:
    """
    class for merger
    """

    def __init__(self, company_id: int,
                 shop_id: int,
                 ipc_id: int,
                 oss_utils: OSSUtility):
        self._root = Path(f"data/{company_id}/{shop_id}/{ipc_id}")
        self._company_id = company_id
        self._shop_id = shop_id
        self._ipc_id = ipc_id
        self._oss_utils = oss_utils

    @property
    def company_id(self) -> int:
        """
        get company id
        :return:
        """
        return self._company_id

    @property
    def shop_id(self) -> int:
        """
        get shop id
        :return:
        """
        return self._shop_id

    @property
    def ipc_id(self) -> int:
        """
        get ipc id
        :return:
        """
        return self._ipc_id

    @property
    def oss_utils(self) -> OSSUtility:
        """
        get internal oss state
        :return:
        """
        return self._oss_utils

    def download_files(self, start_epoch, end_epoch) -> list:
        """
        download files between start epoch and end epoch
        :param start_epoch:
        :param end_epoch:
        :return:
        """
        # TODO: should include 2 dates in case
        target_date = unix2dt(start_epoch)[:10].replace('-', '')
        file_folder = self._root / target_date
        download_folder = Path('tmp/')
        download_folder.mkdir(exist_ok=True)
        used_files = []
        for file in self.oss_utils.list(file_folder.as_posix()):
            if file.endswith('flv'):
                file_name = Path(file).name
                file_start_epoch, file_end_epoch = file_name[:-4].split('_')
                file_start_epoch = int(file_start_epoch)
                file_end_epoch = int(file_end_epoch)
                if start_epoch <= file_start_epoch <= end_epoch \
                        or start_epoch <= file_end_epoch <= end_epoch:
                    download_file = download_folder / file_name
                    self.oss_utils.download(file, download_file)
                    used_files.append(download_file)
        return used_files

    def merge(self,
              start_epoch: int,
              end_epoch: int,
              merged_file: str,
              used_files: list = None) -> str:
        """
        merge video files between start epoch and end epoch
        :param start_epoch:
        :param end_epoch:
        :param merged_file:
        :param used_files:
        :return:
        """
        if not used_files:
            used_files = self.download_files(start_epoch, end_epoch)

        if used_files:
            # merge
            file_list_name = Path(f"tmp/{start_epoch}_{end_epoch}.txt")
            with LockFile(file_list_name.as_posix() + '.lock'):
                if not file_list_name.exists():
                    with open(file_list_name, 'w') as f_handle:
                        for file in used_files:
                            f_handle.write(f"file '{file.name}'\n")
                else:
                    LOGGER.info(f'<{file_list_name}> already exists.')

            ff_cmd = FFmpeg(global_options=['-f', 'concat'],
                            inputs={file_list_name.as_posix(): ['-safe', '0']},
                            outputs={merged_file: ['-c', 'copy']})
            LOGGER.info(ff_cmd.cmd)
            ff_cmd.run()
        return merged_file
