"""Deeplearning用Processタスク(子プロセスと1対1)
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

from dl_project import DlProject


class DlProcessTask(QProcess):
    @staticmethod
    def overrides(klass):
        def check_super(method) -> Any:
            method_name = method.__name__
            msg = f"`{method_name}()` is not defined in `{klass.__name__}`."
            assert method_name in dir(klass), msg
        def wrapper(method) -> Any:
            check_super(method)
            return method
        return wrapper

    def __getstate__(self) -> DlProject:
        """
        親プロセス側でPickle化するオブジェクトを指定する
        https://qiita.com/fumitoh/items/6ae34b7c63cb419a7b48
        https://qiita.com/s-wakaba/items/f15b4aa579c018880758
        :return:
        """
        return self.dl_project

    def __setstate__(self, memory_object) -> None:
        """
        子プロセス側でPickleデータからメモリオブジェクトに解凍
        https://qiita.com/fumitoh/items/6ae34b7c63cb419a7b48
        https://qiita.com/s-wakaba/items/f15b4aa579c018880758
        :param memory_object: Pickleデータ
        :return:
        """
        self.dl_project = memory_object

    def __init__(self, parent: Optional[QObject], dl_project: Optional[DlProject]):
        super().__init__(parent)

        # プロジェクトファイルのインスタンス
        self.dl_project = dl_project
