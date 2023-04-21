import datetime, d, w

font = d.font
row0 = (w.ROWS - len(font['0'])) // 2
step = len(font['0'][0]) + 1
col0 = (w.COLS - 8 * step) // 2

while True:
    frame = w.get_clear_frame()

    t = str(datetime.datetime.now())

    for i, ch in enumerate(t):
        frame[0][i] = ch

    t = t[11:19]
    for si in range(len(t)):
        for ri in range(len(font[t[si]])):
            for ci in range(len(font[t[si]][ri])):
                frame[row0 + ri][col0 + si*step + ci] = font[t[si]][ri][ci]
    
    w.output_frame(frame)

