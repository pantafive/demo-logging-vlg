import json
import signal
import sys
import time
import uuid
from dataclasses import asdict, dataclass


class GracefulKiller:
    kill_now = False

    def __init__(self):
        signal.signal(signal.SIGINT, self.exit_gracefully)
        signal.signal(signal.SIGTERM, self.exit_gracefully)

    def exit_gracefully(self, *args):
        self.kill_now = True


@dataclass
class Message:
    log_level: str
    request_id: str
    message: str
    additional_info: dict


def main(killer: GracefulKiller) -> None:
    while True:
        for level in ["DEBUG", "INFO", "WARNING", "ERROR", "CRITICAL"]:
            if killer.kill_now:
                return
            message = Message(level, str(uuid.uuid4()), "Hello World", {"key": "value"})
            sys.stderr.write(json.dumps(asdict(message)) + "\n")
            time.sleep(5)


if __name__ == "__main__":
    time.sleep(1)
    main(GracefulKiller())
