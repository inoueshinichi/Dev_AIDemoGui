"""画像表示用シーン
"""
import os
import sys

sys.path.append("/".join([os.getcwd(), 'ui']))
sys.path.append("/".join([os.getcwd(), "aitoolkit"]))

from aitookkit.common import *

class CanvasScene(QGraphicsScene):

    def __init__(self, parent: Optional[QObject] = None):
        super().__init__(parent)

        # 画像データ
        self.ori_dib_img : Optional[QImage] = None
        self.dib_img : Optional[QImage] = None
        self.ddb_img : Optional[QPixmap] = None
        self.item_ddb_img : Optional[QGraphicsPixmapItem] = None
        self.item_ddb_img_pos : QPointF = None
        self.dib_img_pos : QPoint = None

    def set_dib_img(self, img : QImage, is_ori : bool = False) -> bool:
        if (is_ori):
            self.ori_dib_img = img.copy()
        self.dib_img = img
        self.draw_ddb_img(self.dib_img)
        self.update() # シーンの更新

    def get_dib_img(self) -> Optional[QImage]:
        return self.dib_img

    def get_ori_dib_img(self) -> Optional[QImage]:
        return self.ori_dib_img

    def draw_ddb_img(self, img : QImage) -> None:
        # QPixmap生成
        self.ddb_img = QPixmap.fromImage(img)

        # QGraphicsPixmapItem生成
        if self.item_ddb_img in self.items():
            self.item_ddb_img = QGraphicsPixmapItem(self.ddb_img)
            self.addItems(self.item_ddb_img)
        else:
            self.item_ddb_img.setPixmap(self.ddb_img)

        # シーンサイズの設定
        self.setSceneRect(self.item_ddb_img.pixmap().rect())


    def reset_dib_img(self) -> None:
        if ((self.ori_dib_img is not None) and (not self.ori_dib_img.isNumm())):
            self.dib_img = self.ori_dib_img.copy()
            self.draw_ddb_img(self.dib_img)