
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), 'ui'))
sys.path.append(os.path.join(os.path.dirname(__file__), 'aitoolkit'))

from aitoolkit.type_def import *
from aitoolkit.qt_pyside2 import *

from startup_dialog import StartupDialog


def main() -> None:
    
    """Pythonインタープリター上のQObjectの扱い
    概要 : QtオブジェクトのPython参照オブジェクト(Python上の変数)を破棄しても, そのタイミングで破棄されない.

    Qtオブジェクトが破棄対象になるタイミングは, 自身のオブジェクトが破棄された際に，
    設定していた親オブジェクトも破棄される場合に限る.

    Pythonの参照オブジェクトを破棄しても内部でオブジェクトが保持されているため,
    QObject系列のオブジェクトの生成と破棄を繰り返すと莫大なメモリを消費してしまう.

    QWidget系にself.setAttribute(Qt.WA_DeleteOnClose)を設定すると, closeEvent()実行後に自動でメモリ破棄される.
    しかし, Python参照オブジェクトは破棄されておらずPython参照オブジェクトから内部的に空になったメモリオブジェクトを
    参照できてしまう. (ダングリング状態)
    """

    # App Info
    app : QApplication = QApplication(sys.argv)
    app_ver : str = QApplication.applicationVersion()
    print("Qt App ver:", app_ver)
    app_dir : str = QApplication.applicationDirPath()
    print("Qt App dir:", app_dir)
    app_file : str = QApplication.applicationFilePath()
    print("Qt App file path:", app_file)
    app_pid : int = QApplication.applicationPid()
    print("Qt App process id:", app_pid)
    app_name : str = QApplication.applicationName()
    print("Qt App name:", app_name)
    app_display_name : str = QApplication.applicationDisplayName()
    print("Qt App display name:", app_display_name)
    app_org_domain : str = QApplication.organizationDomain()
    print("Qt App org domain:", app_org_domain)
    app_org_name : str = QApplication.organizationName()
    print("Qt App org name:", app_org_name)
    app_platform_name : str = QApplication.platformName()
    print("Qt App platform name:", app_platform_name)
    app_desktop_file_name : str = QApplication.desktopFileName()
    print("Qt App desktop file name:", app_desktop_file_name)
    screens : List[Any] = QApplication.screens()
    print("Qt App associated screens:", screens)

    startup_win : Any = StartupDialog()
    startup_win.show()


    sys.exit(app.exec_()) 

if __name__ == "__main__":
    main()