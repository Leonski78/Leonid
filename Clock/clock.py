import math, w

X0, Y0 = w.COLS/2, w.ROWS/2

def draw(degree, distance, text):
    x = X0 + math.cos(math.radians(degree)) * distance * 2
    y = Y0 + math.sin(math.radians(degree)) * distance
    for i in range(len(text)):
        frame[int(y)][int(x)+i] = text[i]

def draw_clock(hour, minute, second):
    for h in range(1, 12+1):
        draw(360/12*(h-3), w.ROWS/2 - 1, str(h))
    for d in range(1, int(w.ROWS/5)+2):
        draw(360/12 * (hour + minute/60 - 3), d, 'H')
    for d in range(1, int(w.ROWS/3)+1):
        draw(360/60 * (minute + second/60 - 15), d, '*')
    for d in range(1, int(w.ROWS/2)-2):
        draw(360/60 * (second - 15), d, '.')
    frame[int(Y0)][int(X0)] = '@'
    
H, M, S = 0, 5, 0

while True:
    frame = w.get_clear_frame()
    
    S += 1
    if S >= 60:
        S = 0
        M += 1
        if M >= 60:
            M = 0
            H += 1
            if H >= 12:
                H = 0
    
    draw_clock(H,M,S)

    for i, ch in enumerate(f'{H:02d}:{M:02d}:{S:02d}'):
        frame[0][i] = ch

    w.output_frame(frame)
