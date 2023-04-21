import time, d, w

font = d.font
row0 = (w.ROWS - len(font['0'])) // 2
step = len(font['0'][0]) + 1
col0 = (w.COLS - 3 * step) // 2

t0 = time.time()

while True:
    frame = w.get_clear_frame()

    delta = time.time() - t0
    delta_sec = int(delta)
    t = f'{delta_sec:03d}'
    m1 = font[t[-1]]
    m2 = font[str((int(t[-1])+1)%10)]
    for si in range(len(t)-1):
        for ri in range(len(font[t[si]])):
            for ci in range(len(font[t[si]][ri])):
                frame[row0 + ri][col0 + si*step + ci] = font[t[si]][ri][ci]
    sec_part = delta - delta_sec
    m1_part = round((1 - sec_part) * len(m1))
    m2_part = len(m2) - m1_part
    mm = [m1[i] for i in range(m2_part, len(m1))]
    mm += [m2[i] for i in range(m2_part)]
    for ri in range(len(mm)):
        for ci in range(len(mm[ri])):
            frame[row0 + ri][col0 + 2*step + ci] = mm[ri][ci]
    
    
    w.output_frame(frame)

