"""_Qtライブラリ
"""

import os

import PySide2
os.environ['QT_QPA_PLATFORM_PLUGIN_PATH'] = \
    os.path.join(os.path.dirname(PySide2.__file__), 'plugins', 'platforms')

from PySide2.QtCore import (
    Qt,
    Signal,
    Slot,
    QObject,
    QThread,
    QMutex,
    QMutexLocker,
    QCoreApplication,
    QEvent,
    QTimer,
    QPoint,
    QPointF,
    QRect,
    QRectF,
    qDebug,
    QLine,
    QLineF,
    QModelIndex,
    QSortFilterProxyModel,
    QRegExp,
    QBuffer,
    QIODevice,
    QProcess,
)

from PySide2.QtCharts import QtCharts

from PySide2.QtMultimedia import (
    QCameraInfo,
)

from PySide2.QtGui import (
    QIcon,
    QImage,
    QPixmap,
    QBitmap,
    QPen,
    QBrush,
    QFont,
    qGray,
    QTextCursor,
    QPainter,
    QPainterPath,
    QColor,
    QDrag,
    QStandardItem,
    QStandardItemModel,
)

from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QFileDialog,
    QDialog,
    QMessageBox,
    QLabel,
    QHeaderView,
    QTableWidget,
    QTableWidgetItem,
    QTableView,
    QStyledItemDelegate,
    QHBoxLayout,
    QGraphicsScene,
    QGraphicsView,
    QGraphicsPixmapItem,
    QGraphicsPathItem,
    QGraphicsRectItem,
    QGraphicsTextItem,
    QGraphicsSimpleTextItem,
    QGraphicsEllipseItem,
    QGraphicsItem,
    QGraphicsScene, 
    QGraphicsLineItem,
    QInputDialog,
    QColorDialog,
)