'''A short demo of the threading builtin package,
and an example of how NOT to work with multiple threads.'''
from threading import Thread
import time

JOKE_PARTS = [
    'Because always getting',
    'woken up at',
    'random times',
    'makes them cranky.'
]

def add_joke_part(part, joke_parts):
    time.sleep(0.2)
    # threads take around 20 ms to start up, so wait much longer than the
    # startup time 
    joke_parts.append(part)

def main():
    '''reassemble the joke using multiple threads'''
    threads = []
    print("Q: Why are threads bad at sharing resources?")
    new_joke_parts = []
    for part in JOKE_PARTS:
        thread = Thread(None, 
            target=lambda: add_joke_part(part, new_joke_parts))
        threads.append(thread)
        thread.start()
    for thread in threads:
        thread.join()
    print('\n'.join(new_joke_parts))


if __name__ == '__main__':
    main()