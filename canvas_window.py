"""画像表示用ウィンドウ
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

from canvas_scene import CanvasScene

from ui.ui_canvas_window import Ui_CanvasWindow


class CanvasWindow(QMainWindow):

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

    def __init__(self, parent : Optional[QWidget] = None):
        super().__init__(parent)

        # UI
        self.ui : Optional[Any] = Ui_CanvasWindow()
        self.ui.setupUi(self)

        # ウィンドウ属性の設定
        self.setAttribute(Qt.WA_DeleteOnClose)

        # シーンの設定
        self.scene : Optional[CanvasScene] = CanvasScene(self)
        self.ui.graphicsView_canvas.setScene(self.scene)


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






