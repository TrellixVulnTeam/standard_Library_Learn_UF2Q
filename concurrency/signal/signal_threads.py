import os
import signal
import threading
import time


def signal_handler(num, stack):
    print('Received signal {} in {}'.format(
        num, threading.current_thread().name
    ))


signal.signal(signal.SIGUSR1, signal_handler)


def wait_for_signal():
    print('Waiting for signal in', threading.current_thread().name)
    signal.pause()
    print('Done waiting')


receiver = threading.Thread(
    target=wait_for_signal,
    name='reveiver',
)

receiver.start()
time.sleep(0.1)


def send_signal():
    print('Sending signal in', threading.current_thread().name)
    os.kill(os.getpid(), signal.SIGUSR1)


sender = threading.Thread(target=send_signal, name='sender')
sender.start()
sender.join()

print('waiting for', receiver.name)
signal.alarm(2)
receiver.join()
