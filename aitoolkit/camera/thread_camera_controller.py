
import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from type_def import *
from common import *

from threading import Thread

from thread_camera_frame_reader import ThreadCameraFrameReader
from usb_thread_camera_frame_reader import UsbThreadCameraFrameReader

# UsbThreadCameraFrameReader = NewType("UsbThreadCameraFrameReader", ThreadCameraFrameReader)

class ThreadCameraController:

    def __init__(self):
        self.registries: Dict[str, Tuple[Optional[Thread], Optional[ThreadCameraFrameReader]]]
    
    def remove_device(self, uni_name: str) -> None:
        self.stop_worker(uni_name)
        del self.registries[uni_name]

    def set_device(self, uni_name: str, io_type: str, device_id: Union[int, bytearray, str]) -> bool:
        if uni_name in self.registries.keys():
            return False

        camera_frame_reader = None
        if 'usb' == io_type.lower():
            camera_frame_reader = UsbThreadCameraFrameReader()
        elif 'ip' == io_type.lower():
            raise NotImplementedError("No implement ip camera interface yet.")
        elif 'ids' == io_type.lower():
            raise NotImplementedError("No implement ids camera interface yet.")
        else:
            raise NotImplementedError("So far, this controller is adapted to \
            `usb`, `ip` and `ids`. Given is " % io_type) 
        
        # @Note daemonスレッド: 残っているスレッドがデーモンスレッドだけになった時に Python プログラム全体を終了させる
        worker_thread = Thread(target=camera_frame_reader.start, 
                               args=(),
                               name=f"Worker thread of camera Id: `{device_id}`, Type: `{io_type}`",
                               daemon=True)
            
        camera_frame_reader.set_device_id(device_id)

        # 追加
        self.registries[uni_name] = (worker_thread, camera_frame_reader)

    def get_device_id(self, uni_name: str) -> Union[int, bytearray, str, None]:
        if uni_name in self.registries.keys():
            return self.registries[uni_name][1].get_device_id()
        else:
            return None

    def set_target_fps(self, uni_name: str, fps: float) -> None:
        if uni_name in self.registries.keys():
            self.registries[uni_name][1].set_target_fps(fps)
        
    def get_target_fps(self, uni_name: str) -> float:
        if uni_name in self.registries.keys():
            return self.registries[uni_name][1].get_target_fps()

    def get_thread_id(self, uni_name: str) -> Optional[int]:
        if uni_name in self.registries.keys():
            worker_thread = self.registries[uni_name][0]
            if worker_thread.is_alive():
                return worker_thread.getident()
        return None

    def get_thread_native_id(self, uni_name: str) -> Optional[int]:        
        if uni_name in self.registries.keys():
            worker_thread = self.registries[uni_name][0]
            if worker_thread.is_alive():
                return worker_thread.get_native_id() # Windows, Linux, macOS
        return None

    def state_of_thread(self, uni_name: str) -> bool:
        return self.registries[uni_name][0].is_alive()

    def get_managed_active_threads(self) -> int:
        count = 0
        for key in self.registries.keys():
            if self.state_of_thread(key):
                count += 1
        return count

    def get_managed_threads(self) -> int:
        return len(self.registries)
    
    def initialize(self, uni_name: str) -> bool:
        if uni_name in self.registries.keys():
            return self.registries[uni_name][1].initialize()
        else:
            return False
    
    def shutdown(self, uni_name: str) -> None:
        if uni_name in self.registries.keys():
            self.registries[uni_name][1].shutdown()

    def fetch_frame(self, uni_name: str) -> Union[Optional[np.ndarray], float, float, str]:
        # 短時間で複数回コールされるのでifチェックなし
        timestamp = dt.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        return self.registries[uni_name][1].retrieve_frame(), timestamp

    def stop_worker(self, uni_name: str) -> None:
        print(f"##### stop_worker({uni_name}) #####")
        if uni_name in self.registries.keys():
            worker_thread = self.registries[uni_name][0]
            if worker_thread.is_alive():
                frame_reader = self.registries[uni_name][1]
                frame_reader.stop()
                worker_thread.join() # worker_thread終了までメインスレッドを待機させる
                print("Stop worker thread: " % self.get_thread_id(uni_name))
            else:
                print("Dead worker thread: " % self.get_thread_id(uni_name))
        else:
            print("No device. Given is " % uni_name)

    def start_worker(self, uni_name: str) -> None:
        print(f"##### start_worker({uni_name}) #####")

        if uni_name is not self.registries.keys():
            print("No uni_name. Given is " % uni_name)
            return

        worker_thread = self.registries[uni_name][0]
        frame_reader = self.registries[uni_name][1]

        if worker_thread.is_alive():
            print("Already worker thread running. Id: " % worker_thread.get_ident())
            return
        
        if not frame_reader.initialized:
            print(f"Not initialize {uni_name} yet. Please initialize")
            return
        
        # 実行
        worker_thread.start()
        print("Worker thread start.")
        print("Status of starting worker thread {0} : {1}".format(worker_thread.get_ident(), worker_thread.is_alive()))
