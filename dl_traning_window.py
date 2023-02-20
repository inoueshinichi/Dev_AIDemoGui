"""ディープラーニング学習画面
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

from ui.ui_dl_training_window import Ui_DlTrainingWindow

from dl_project import DlProject
from dl_process_controller import DlProcessController





class DlTrainingWindow(QMainWindow):

    def __init__(self, parent: Optional[QWidget] = None):
        super().__init__(parent)

        # UI
        self.ui: Any = Ui_DlTrainingWindow()
        self.ui.setupUi(self)

        # Workspace
        self.workspace_path: Optional[str] = None

        # Managed Projects
        self.managed_projects: Optional[Dict[str, Optional[DlProject]]] = None

        # Learning Child-Process Controller
        self.dl_process_controller: Optional[DlProcessController] = None

        # Learning Curve Chart
        self.dl_learning_charts: Optional[Dict[str, DlTrainingWindow]] = None



        # Signal/Slot
        # self._toolbar_connection()
        # self._menubar_connection()
        # self._ui_connection()
        # self._custom_connection()

    def _toolbar_connection(self) -> None:
        """
        ToolBarに関するSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("ToolBarに関するSignal/Slotの接続")

    def _menubar_connection(self) -> None:
        """
        MenuBarに関するSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("MenuBarに関するSignal/Slotの接続")

    def _ui_connection(self) -> None:
        """
        UIに関するSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("UIに関するSignal/Slotの接続")

    def _custom_connection(self) -> None:
        """
        ユーザー定義のカスタムSignal/Slotの接続
        :return:
        """
        raise NotImplementedError("ユーザー定義のカスタムSignal/Slotの接続")

    def _init_training_curve_chart(self):
        """
        学習曲線用QChartの初期化
        """
        training_curve_chart: QtCharts.QChart = QtCharts.QChart()

        training_curve_chart.setAnimationOptions(QtCharts.QChart.AllAnimations)
