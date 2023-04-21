import time, sys

FPS = 25 # FPS - Frames Per Second (число кадров в секунду)

windows = sys.platform.startswith('win')

ROWS, COLS = 20, 80
if windows:
    ROWS, COLS = 29, 120
else:
    print('\x1b[2J')

def get_clear_frame():
    frame = [[' '] * COLS for _ in range(ROWS)]
    return frame

def output_frame(frame):
    esc = s = ''
    if not windows:
        esc, s = '\x1b[H', '|\n'
    s = s.join([''.join(row) for row in frame])
    if not windows:
        s += '|\n' + '-' * COLS + '+\n'
    print(esc + s, end='')
    time.sleep(1 / FPS)
