"""画像表示用ビュー
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *

class CanvasView(QGraphicsView):

    zoom_scale_factor : float = 1.0
    zoom_current_level = 0
    zoom_max_level : int = 12
    zoom_min_level : int = -12

    # ズームレベル (参考: ImageJ)
    zoom_scale : Dict[str, float] = dict()
    zoom_scale['1/72'] = (float)(1. / 72)
    zoom_scale['1/48'] = (float)(1. / 48)
    zoom_scale['1/32'] = (float)(1. / 32)
    zoom_scale['1/24'] = (float)(1. / 24)
    zoom_scale['1/16'] = (float)(1. / 16)
    zoom_scale['1/12'] = (float)(1. / 12)
    zoom_scale['1/8']  = (float)(1. / 8)
    zoom_scale['1/6']  = (float)(1. / 6)
    zoom_scale['1/4']  = (float)(1. / 4)
    zoom_scale['1/3']  = (float)(1. / 3)
    zoom_scale['1/2']  = (float)(1. / 2)
    zoom_scale['3/4']  = (float)(3. / 4)
    zoom_scale['1']    = (float)(1.)
    zoom_scale['4/3']  = (float)(4. / 3)
    zoom_scale['2']  = (float)(2.)
    zoom_scale['3']  = (float)(3.)
    zoom_scale['4']  = (float)(4.)
    zoom_scale['6']  = (float)(6.)
    zoom_scale['8']  = (float)(8.)
    zoom_scale['12'] = (float)(12.)
    zoom_scale['16'] = (float)(16.)
    zoom_scale['24'] = (float)(24.)
    zoom_scale['32'] = (float)(32.)
    zoom_scale['48'] = (float)(48.)
    zoom_scale['72'] = (float)(72.)

    zoom_level : Dict[int, str] = dict()
    zoom_level[-12] = '1/72'
    zoom_level[-11] = '1/48'
    zoom_level[-10] = '1/32'
    zoom_level[-9]  = '1/24'
    zoom_level[-8]  = '1/16'
    zoom_level[-7]  = '1/12'
    zoom_level[-6]  = '1/8'
    zoom_level[-5]  = '1/6'
    zoom_level[-4]  = '1/4'
    zoom_level[-3]  = '1/3'
    zoom_level[-2]  = '1/2'
    zoom_level[-1]  = '3/4'
    zoom_level[0]   = '1'
    zoom_level[1]   = '4/3'
    zoom_level[2]   = '2'
    zoom_level[3]   = '3'
    zoom_level[4]   = '4'
    zoom_level[5]   = '6'
    zoom_level[6]   = '8'
    zoom_level[7]   = '12'
    zoom_level[8]   = '16'
    zoom_level[9]   = '24'
    zoom_level[10]  = '32'
    zoom_level[11]  = '48'
    zoom_level[12]  = '72'
    
    def __init__(self, parent : Optional[QWidget] = None):
        super().__init__(parent)
        
        # 親ウィンドウの設定(QMainWindow系統のCentralWidget対策)
        self.parent_widget : Optional[QWidget] = self.parentWidget()

        if self.parent_widget is None:
            raise ValueError("Parent widget of CanvasView is None. Please set parent.")

        count : int = 0
        while self.parent_widget.metaObject().className() != "CanvasWindow":
            self.parent_widget = self.parent_widget.parentWidget()
            count = count + 1
            if count > 3:
                raise ValueError("CanvasWindow do not exist.")

        # ビュー属性の設定
        self.setAcceptDrops(True) # ドロップイベント有効化
        # self.setAlignment(Qt.AlignLeft | Qt.AlignTop) # 原点を左上にする
        self.setViewportUpdateMode(QGraphicsView.MinimalViewportUpdate) # FullViewportUpdate, SmartViewportUpdate, BoundingRectViewportUpdate
        self.setRenderHint(QPainter.Antialiasing, enabled=False)        # シーンオブジェクトのアンチエイリアスをOFF
        self.setRenderHint(QPainter.TextAntialiasing, enabled=True)     # シーンの文字のアンチエイリアスをON
        self.setTransformationAnchor(QGraphicsView.AnchorUnderMouse)    # アフィン変換の原点をマウス直下にする
        self.setBackgroundBrush(QColor(64, 64, 64, 255))                # 背景を灰色に設定

        """@warning シーンとビューの間のTransformの行列は行優先表現
             [m11, m12, m13],
             [m21, m22, m23],
             [m31, m32, m33]
             1. ゼロ要素 m13 = m23 = 0
             2. 並進要素 m31 = trans_x, m32 = trans_y
             3. 回転要素 m11, m12, m21, m22
             4. 拡縮要素 m11, m22
             5. 1要素 m33
        """
        # self.transform()


    @staticmethod
    def zoom_level(level : int) -> None:
        if level <= CanvasView.zoom_max_level and level >= CanvasView.zoom_min_level:
            scale_id : str = CanvasView.zoom_level[level]
            CanvasView.zoom_scale_factor = CanvasView.zoom_scale[scale_id]
    
    @staticmethod
    def zoom_out() -> None:
        if CanvasView.zoom_current_level > CanvasView.zoom_max_level:
           CanvasView.zoom_current_level = CanvasView.zoom_max_level
        CanvasView.zoom_current_level = CanvasView.zoom_current_level - 1

    @staticmethod
    def zoom_in() -> None:
        if CanvasView.zoom_current_level < CanvasView.zoom_min_level:
            CanvasView.zoom_current_level = CanvasView.zoom_min_level
        CanvasView.zoom_current_level = CanvasView.zoom_current_level + 1

    @staticmethod
    def reset_zoom_level() -> None:
        CanvasView.zoom_scale_factor = CanvasView.zoom_scale[CanvasView.zoom_level[0]] # 1.0

    def scale_scene(self) -> None:
        self.resetMatrix() # View-Scene間の座標変換をリセット
        self.scale(CanvasView.zoom_scale_factor, CanvasView.zoom_scale_factor)


    # @override
    def wheelEvent(self, event: PySide2.QtGui.QWheelEvent):
        # マウスホイールは15度進む度に120単位で進むので，実際の角度は8で割った値
        degree = event.angleDelta().y() / 8

        if event.modifiers() == Qt.ControlModifier:
            """ズーム処理
            """
            # ズーム中心をマウス位置に指定
            self.setTransformationAnchor(self.ViewportAnchor.AnchorUnderMouse)

            sign : bool = degree > 0
            if sign:
                CanvasView.zoom_in()
            else:
                CanvasView.zoom_out()
            
            self.scale_scene() # ズーム

        elif event.modifiers() == Qt.ShiftModifier:
            """水平方向シフト
            """
        else:
            """垂直方向シフト
            """

        super().wheelEvent(event)



    








    