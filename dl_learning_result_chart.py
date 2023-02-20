"""ディープラーニング学習結果グラフ
"""
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.common import *
from aitoolkit.qt_pyside2 import *


class DlTrainingResultChart:
    def __init__(self, parent: Optional[QWidget], max_epoch: int,
                 tick_count_epoch: int = 10, tick_count_loss: int = 10, tick_count_acc: int = 10):

        if not isinstance(parent, QWidget):
            raise ValueError("Parent is not QWidget. Please set QWidget parent.")

        # 親
        self.parent = parent

        # Config
        self.dl_axis_y_loss_tick_count: int = tick_count_loss
        self.dl_axis_y_acc_tick_count: int = tick_count_acc
        self.dl_axis_x_epoch_tick_count: int = tick_count_epoch
        self.dl_axis_x_max_epoch: int = max_epoch
        self.dl_axis_x_epoch_current_range_max: int = self.dl_axis_x_epoch_tick_count
        self.dl_axis_x_epoch_current_range_min: int = 0
        self.dl_axis_y_loss_current_range_max: float = self.dl_axis_y_loss_tick_count
        self.dl_axis_y_loss_current_range_min: float = 0.0
        self.dl_axis_y_acc_current_range_max: float = 1.0
        self.dl_axis_y_acc_current_range_min: float = 0.0

        # Chart
        self.dl_chart_learning_curve: QtCharts.QChart = QtCharts.QChart(self.parent)
        self.dl_chart_learning_curve.setAnimationOptions(QtCharts.QChart.AllAnimations)

        # View
        self.dl_view_chart: QtCharts.QChartView = QtCharts.QChartView(self.dl_chart_learning_curve)
        self.dl_view_chart.setRenderHint(QPainter.Antialiasing)

        # Layout
        self.dl_layout_view_chart: QHBoxLayout = QHBoxLayout(self.parent)
        self.dl_layout_view_chart.addWidget(self.dl_view_chart)
        self.parent.parentWidget().setLayout(self.dl_layout_view_chart) # 親Widgetに配置

        # Series
        self.dl_series_loss_train: QtCharts.QLineSeries = QtCharts.QLineSeries(self.parent)
        self.dl_series_loss_val: QtCharts.QLineSeries = QtCharts.QLineSeries(self.parent)
        self.dl_series_acc_train: QtCharts.QLineSeries = QtCharts.QLineSeries(self.parent)
        self.dl_series_acc_val: QtCharts.QLineSeries = QtCharts.QLineSeries(self.parent)
        self.dl_series_axis_x_epoch: QtCharts.QLineSeries = QtCharts.QLineSeries(self.parent)

        # Axis
        self.dl_axis_y_loss: QtCharts.QValueAxis = QtCharts.QValueAxis(self.parent)
        self.dl_axis_y_acc: QtCharts.QValueAxis = QtCharts.QValueAxis(self.parent)
        self.dl_axis_x_epoch: QtCharts.QValueAxis = QtCharts.QValueAxis(self.parent)

        self._initialize()

    def _initialize(self) -> None:
        """グラフの初期化
        """
        # Set series name
        self.dl_series_loss_train.setName("Loss train")
        self.dl_series_loss_val.setName("Loss val")
        self.dl_series_acc_train.setName("Acc train")
        self.dl_series_acc_val.setName("Acc val")
        self.dl_series_axis_x_epoch.setName("Epoch")

        # Set series color
        self.dl_series_loss_train.setColor(QColor(Qt.red))
        self.dl_series_loss_val.setColor(QColor(Qt.blue))
        self.dl_series_acc_train.setColor(QColor(Qt.magenta))
        self.dl_series_acc_val.setColor(QColor(Qt.cyan))
        self.dl_series_axis_x_epoch.setColor(QColor(Qt.black))

        # Set series to chart
        self.dl_chart_learning_curve.addSeries(self.dl_series_loss_train)
        self.dl_chart_learning_curve.addSeries(self.dl_series_loss_val)
        self.dl_chart_learning_curve.addSeries(self.dl_series_acc_train)
        self.dl_chart_learning_curve.addSeries(self.dl_series_acc_val)

        # Set axis_x_epoch to chart
        self.dl_axis_x_epoch.setTickCount(self.dl_axis_x_epoch_tick_count)
        self.dl_axis_x_epoch.setRange(0, self.dl_axis_x_max_epoch)
        self.dl_axis_x_epoch.setLabelFormat("%d")
        self.dl_axis_x_epoch.setTitleText("Epoch")
        self.dl_chart_learning_curve.addAxis(self.dl_axis_x_epoch, Qt.AlignBottom)
        self.dl_series_loss_train.attachAxis(self.dl_axis_x_epoch)
        self.dl_series_loss_val.attachAxis(self.dl_axis_x_epoch)
        self.dl_series_acc_train.attachAxis(self.dl_axis_x_epoch)
        self.dl_series_acc_val.attachAxis(self.dl_axis_x_epoch)

        # Set axis_y_loss to chart
        self.dl_axis_y_loss.setTickCount(self.dl_axis_y_loss_tick_count)
        self.dl_axis_y_loss.setLabelFormat("%.2f")
        self.dl_axis_y_loss.setTitleText("Loss")
        self.dl_chart_learning_curve.addAxis(self.dl_axis_y_loss, Qt.AlignLeft)
        self.dl_series_loss_train.attachAxis(self.dl_axis_y_loss)
        self.dl_series_loss_val.attachAxis(self.dl_axis_y_loss)

        # Set axis_y_acc to chart
        self.dl_axis_y_acc.setTickCount(self.dl_axis_y_acc_tick_count)
        self.dl_axis_y_acc.setLabelFormat("%.2f")
        self.dl_axis_y_acc.setTitleText("Accuracy")
        self.dl_chart_learning_curve.addAxis(self.dl_axis_y_acc, Qt.AlignRight)
        self.dl_series_acc_train.attachAxis(self.dl_axis_y_acc)
        self.dl_series_acc_val.attachAxis(self.dl_axis_y_acc)

    def _set_range_axis_x_epoch(self, epoch: int):
        if (epoch % self.dl_axis_x_epoch_tick_count) == 0:
            self.dl_axis_x_epoch_current_range_max = epoch + self.dl_axis_x_epoch_tick_count
            self.dl_axis_x_epoch.setRange(0, self.dl_axis_x_epoch_current_range_max)
            self.dl_axis_x_epoch.setMin(0)
            self.dl_axis_x_epoch.setMax(self.dl_axis_x_max_epoch)

    def _set_range_axis_y_loss(self, loss_train: float, loss_val: float):
        large_loss = loss_val if loss_val > loss_train else loss_train
        if large_loss > self.dl_axis_y_loss_current_range_max:
            loss_chunk = large_loss / self.dl_axis_y_loss_tick_count
            self.dl_axis_y_loss_current_range_max = loss_chunk * (self.dl_axis_y_loss_tick_count + 1)
            self.dl_axis_y_loss.setRange(0, self.dl_axis_y_loss_current_range_max)
            self.dl_axis_y_loss.setMin(0)
            self.dl_axis_y_loss.setMax(self.dl_axis_y_loss_current_range_max)

    def _set_range_axis_y_acc(self, acc_train: float, acc_val: float):
        large_acc = acc_val if acc_val > acc_train else acc_train
        if large_acc > self.dl_axis_y_acc_current_range_max:
            acc_chunk = large_acc / self.dl_axis_y_acc_tick_count
            self.dl_axis_y_acc_current_range_max = acc_chunk * (self.dl_axis_y_acc_tick_count + 1)
            self.dl_axis_y_acc.setRange(0, self.dl_axis_y_acc_current_range_max)
            self.dl_axis_y_acc.setMin(0)
            self.dl_axis_y_acc.setMax(self.dl_axis_y_acc_current_range_max)
    def update_learning_curve(self, epoch: int,
                              loss_train: float, loss_val: float,
                              acc_train: float, acc_val: float) -> None:
        """学習曲線の更新
        """
        self.dl_series_loss_train.append(epoch, loss_train)
        self.dl_series_loss_val.append(epoch, loss_val)
        self.dl_series_acc_train.append(epoch, acc_train)
        self.dl_series_acc_val.append(epoch, acc_val)

        self._set_range_axis_x_epoch(epoch)
        self._set_range_axis_y_loss(loss_train, loss_val)
        self._set_range_axis_y_acc(acc_train, acc_val)






