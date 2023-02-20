"""Deeplearning用プロジェクトクラス
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

class DlProject:

    def __init__(self):

        # Backend Context
        self.dl_backend_context: Optional[str] = 'cpu' # cpu, cuda0, cuda1, ..

        # Dataset
        self.dl_dataset: Optional[Any] = None

        # Dataloader
        self.dl_dataloader: Optional[Any] = None

        # Argumentation
        self.dl_argumentation: Optional[Any] = None

        # DL Model
        self.dl_model: Optional[Any] = None

        # Optimizer
        self.dl_optimizer: Optional[Any] = None



        # Training Parameters
        self.dl_training_type: Optional[str] = 'FullLearning'  # 'FineTuning', 'TransferLearning'
        self.dl_batch_size: int = 1
        self.dl_max_epochs: int = 1
        self.dl_update_interval: int = 1
        self.dl_warm_up: bool = False
        self.dl_criterion_loss: float = 0.0

        # Scheduler
        self.dl_scheduler: Optional[Any] = None

