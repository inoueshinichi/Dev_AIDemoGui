"""Deeplearning学習用子プロセスコントローラ
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

from dl_process_task import DlProcessTask

import platform

# Pythonによるプロセス間通信の方法
# https://qiita.com/kaitolucifer/items/e4ace07bd8e112388c75
from multiprocessing import (
    Manager,
    Process,
    Queue,
    Pipe,
    Lock,
    Value,
    # Array,
    freeze_support
)

import queue # queue.Empty()例外, queue.Full()例外


class DlProcessController:
    def __init__(self):
        # 子プロセスタスク (id_str,[id_int, Task])
        self.managed_process_tasks: Optional[Dict[str, Tuple[DlProcessTask, int]]] = None
        # 子プロセス制御
        self.managed_process_running: Optional[Dict[str, Value]] = None

    def _initialize(self):
        self.managed_process_tasks = dict()
        self.managed_process_running = dict()
    def add_task(self, process_id: str, project: DlProcessTask) -> bool:
        if process_id in self.managed_process_tasks.keys():
            return False
        # 追加
        self.managed_process_tasks[str][0] = project
        # 共有メモリ作成
        self.managed_process_running[str] = Value(ctypes.c_bool, False)

        return True


    def start_task(self, process_id: str) -> bool:
        if process_id in self.managed_process_tasks.keys():
            print("No exist {0} in DlProcessController. Please add_task.".format(process_id))
            return False
        if self.managed_process_running[process_id] is True:
            print("{0} has already been running.".format(process_id))
            return False

        if platform.system() == "Windows":
            freeze_support()  # 作成する子プロセスがpythonモジュールのimportを完了させることを保証する for Windows OS









