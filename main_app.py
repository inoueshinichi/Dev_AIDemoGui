
import os
import sys

sys.path.append("/".join([os.getcwd(), 'ui']))
sys.path.append("/".join([os.getcwd(), "aitoolkit"]))

from aitookkit.common import *
from startup_dialog import StartupDialog

def main() -> None:

    # App Info
    app = QApplication(sys.argv)
    app_ver = QApplication.applicationVersion()
    print("Qt App ver:", app_ver)
    app_dir = QApplication.applicationDirPath()
    print("Qt App dir:", app_dir)
    app_file = QApplication.applicationFilePath()
    print("Qt App file path:", app_file)
    app_pid = QApplication.applicationPid()
    print("Qt App process id:", app_pid)
    app_name = QApplication.applicationName()
    print("Qt App name:", app_name)
    app_display_name = QApplication.applicationDisplayName()
    print("Qt App display name:", app_display_name)
    app_org_domain = QApplication.organizationDomain()
    print("Qt App org domain:", app_org_domain)
    app_org_name = QApplication.organizationName()
    print("Qt App org name:", app_org_name)
    app_platform_name = QApplication.platformName()
    print("Qt App platform name:", app_platform_name)
    app_desktop_file_name = QApplication.desktopFileName()
    print("Qt App desktop file name:", app_desktop_file_name)
    screens = QApplication.screens()
    print("Qt App associated screens:", screens)

    startup_win = StartupDialog() #QMainWindow()
    startup_win.show()

    sys.exit(app.exec_()) 


if __name__ == "__main__":
    main()