

from common import *

class ProcessCameraFrameReader(metaclass=abc.ABCMeta):

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

    def __init__(self):
        self.device_id: Optional[int] = None
        self.target_fps: float = 0.0
        self.initialized: bool = False
        self.shutdowned: bool = True
        self.running: bool = False
        self.frame_queue: deque[Tuple[np.ndarray, float, float]] = deque(maxlen=queue_size)
        self.channels: int = 0
        self.height: int = 0
        self.width: int = 0
        self.tick_count_ns: float = 0.0

