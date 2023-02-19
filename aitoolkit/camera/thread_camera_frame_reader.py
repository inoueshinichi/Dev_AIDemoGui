import os
import sys
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from type_def import *
from common import *


class ThreadCameraFrameReader(metaclass=abc.ABCMeta):
    """カメラ画像取り込み用インターフェースクラス(スレッド版)

    Args:
        metaclass (_type_, optional): _description_. Defaults to abc.ABCMeta.

    Raises:
        ValueError: 目標FPSがゼロの場合
        NotImplementedError: initialize()実装は派生クラスに移譲
        NotImplementedError: shutdown()の実装は派生クラスに移譲

    Returns:
        _type_: _description_
    """
    
    # 派生クラスへのインターフェースAPIの強制
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

    def __init__(self, queue_size: int = 1):
        self.device_id: Optional[int] = None
        self.target_fps: float = 0.0
        self.initialized: bool = False
        self.running: bool = False
        self.frame_queue: deque[Tuple[np.ndarray, float, float]] = deque(maxlen=queue_size)
        self.channels: int = 0
        self.height: int = 0
        self.width: int = 0
        self.tick_count_ns: float = 0.0

    def set_device_id(self, id: int) -> None:
        self.device_id = id

    def get_device_id(self) -> Optional[int]:
        return self.device_id
    
    def set_target_fps(self, fps: float) -> None:
        if fps <= 0.0:
            raise ValueError("Must fps > 0")
        self.target_fps = fps
    
    def get_target_fps(self) -> float:
        return self.target_fps

    def _spin(self) -> None:
        until_time = self.tick_count_ns + 1000.0 / self.target_fps
        while time.perf_counter_ns() < until_time:
            pass

    @abc.abstractmethod
    def initialize(self) -> bool:
        func_name = inspect.currentframe().f_code.co_name
        class_name = self.__class__.__name__
        raise NotImplementedError(f"No implement {func_name} on {class_name}")

    @abc.abstractmethod
    def shutdown(self) -> None:
        func_name = inspect.currentframe().f_code.co_name
        class_name = self.__class__.__name__
        raise NotImplementedError(f"No implement {func_name} on {class_name}")

    @abc.abstractmethod
    def _capture(self) -> Tuple[int, Optional[np.ndarray]]:
        func_name = inspect.currentframe().f_code.co_name
        class_name = self.__class__.__name__
        raise NotImplementedError(f"No implement {func_name} on {class_name}")

    def start(self) -> None:
        print(">>> Enter capture loop.")
        self.running = True

        while self.running:
            # 目標FPSで周期させる
            self._spin()
            tp_start: int = time.perf_counter_ns()

            try:
                status, frame = self._capture() # 実装は派生クラスに任せる
                    
                if frame is None:
                    print("Missing frame! Error statsu is " % status)

                tp_end: int = time.perf_counter_ns()
                elapsed_time = (tp_end - tp_start) / 1000.0 # [ms]
                real_fps: float = 1000.0 / elapsed_time
                self.frame_queue.append((frame, real_fps, elapsed_time)) # スレッドセーフなキューにプッシュ
            except:
                print("Exception throw at capture loop in worker thread!")
                break
        print("<<< Exit capture loop.")

        if self.running:
            self.shutdown() # 異常終了
        
                
    def stop(self) -> None:
        self.running = False

    def retrieve_frame(self) -> Tuple[Optional[np.ndarray], float, float]:
        if len(self.frame_queue) > 0:
            return self.frame_queue[0]
        else:
            return (None, 0.0, 0.0)
    

