# Dev_AIToolKit

Cyclic System for AI with Gui. 

1. Learning style (Supervised, Unspervised, Reinforcement)
2. Annotation (Image, 3D, Table(Vector), TimeSeries, Video, Audio, Text)
3. Making dataset (Training, Validation, Test ; option uniform label)
4. Select pretrained model or coding model
5. Select optimizer
6. Tuning pyper parameters
7. Train dataset and check loss of these training and validation
8. Test
9. Demo (Checking model performance in sumulated environment)

Requirements
+ Python 3.9
+ Numpy 1.23.5
+ Matplotlib 3.6.2
+ Pandas 1.5.2
+ PySide2(Qt) 5.15.2
+ qimage2ndarray 1.10.0
+ Opencv 4.7.0
+ Opencv-contrib-python 4.7.0
+ Pytorch 1.13.1
+ CUDA 11.7
+ TorchVision
+ TorchAudio
+ Scikit-learn 1.2.0
+ tqdm 4.46.1

### PythonインタープリターにおけるQtオブジェクトの生成破棄サイクル
概要 : QtオブジェクトのPython参照オブジェクト(Python上の変数)を破棄しても, そのタイミングで破棄されない.  
+ Qtオブジェクトが破棄対象になるタイミングは, 自身のオブジェクトが破棄された際に，設定していた親オブジェクトも破棄される場合に限る.
+ Pythonの参照オブジェクトを破棄しても内部でオブジェクトが保持されているため, QObject系列のオブジェクトの生成と破棄を繰り返すと莫大なメモリを消費してしまう.
+ QWidget系にself.setAttribute(Qt.WA_DeleteOnClose)を設定すると, closeEvent()実行後に自動でメモリ破棄される. しかし, Python参照オブジェクトは破棄されておらずPython参照オブジェクトから内部的に空になったメモリオブジェクトを参照できてしまう. (ダングリング状態)

