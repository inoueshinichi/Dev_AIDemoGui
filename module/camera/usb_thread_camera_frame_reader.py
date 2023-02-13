
from common import *
from thread_camera_frame_reader import ThreadCameraFrameReader


class UsbThreadCameraFrameReader(ThreadCameraFrameReader):
    """USB接続カメラ用の実装クラス

    Args:
        ThreadCameraFrameReader (_type_): _description_
    """

    def __init__(self, queue_size: int = 1):
        super().__init__(queue_size)
        self.capture: Any = None

    @ThreadCameraFrameReader.overrides(ThreadCameraFrameReader)
    def initialize(self) -> bool:
        print("Initialize UsbThreadCameraFrameReader...")

        if self.initialized:
            print("Already initialized.")
            return False
        
        if self.device_id is None:
            print("self.device_id is None. Please set device_id.")
            return False

        self.capture = cv2.VideoCapture(self.device_id)
        if not self.capture.isOpened():
            print(f"Failed to open cv2.VideoCapture({self.device_id}).")
            self.shutdown()
            return False
        
        self.capture = cv2.VideoCapture(self.device_id)
        status, frame = self._capture()
        if frame is None:
            print("Failed to capture image buffer. Error status is " % status)
            self.shutdown()
            return False
        
        # 成功
        if frame.ndim == 2:
            # Mono
            self.channels = 1
            self.height, self.width = frame.shape()
            self.initialized = True
        elif frame.ndim == 3:
            # Color
            self.height, self.width, self.channels = frame.shape()
            self.initialized = True
        else:
            print("Shape of frame is not (H,W,C=1or3). Given is ", frame.shape())
            self.shutdown()
            return False
        
        print("Success to initialize video capture. (H,W,C)=({0:d},{1:d},{2:d})"\
            .format(self.height, self.width, self.channels))
        return True

    @ThreadCameraFrameReader.overrides(ThreadCameraFrameReader)
    def shutdown(self) -> None:
        print("Shutdown UsbThreadCameraFrameReader...")
        self.initialized = False
        if self.capture is not None:
            self.capture.release()
            print("Released self.capture.")

    @ThreadCameraFrameReader.overrides(ThreadCameraFrameReader)
    def _capture(self) -> Tuple[int, Optional[np.ndarray]]:
        return self.capture.read()
    