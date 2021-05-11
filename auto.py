import pcbnew

pcb = pcbnew.GetBoard()
OFFSET = float(19.05)
XOFFSET = float(-2.5)
YOFFSET = float(14.61)
DIFFA = float(0.25)
DIFFB = float(0.5)

keys = []

class KeyD:
    def __init__(self, sw, d):
        self.sw = pcb.FindModuleByReference(sw)
        self.d = pcb.FindModuleByReference(d)

    def setswitch(self, x, y):
        self.sw.SetPosition(pcbnew.wxPointMM(x, y))
        self.d.SetPosition(pcbnew.wxPointMM(x + XOFFSET, y + YOFFSET))

    def printRef(self):
        # sw,dの名前を追加したさ
        sw_x = self.sw.GetPosition().x
        sw_y = self.sw.GetPosition().y
        d_x = self.d.GetPosition().x
        d_y = self.d.GetPosition().y
        print("(" + str(sw_x) + "," + str(sw_y) + ")" + "(" + str(d_x) + "," + str(d_y) + ")")

def Adfust():
    for i in range(keys):
        i.setswitch(i.sw.GetPosition().x, i.sw.GetPosition().y)

def Set():
    for i in range(1, 65):
        keys.append(KeyD("SW" + str(i+1), "D" + str(i)))

    # 一応ダイオードとスイッチを紐づけておく(下目に配置)
    for i, key in enumerate(keys):
        x = (i % 16)  * OFFSET
        y = (i // 16) * OFFSET
        key.setswitch(x, y + OFFSET * 3)

    # col 1 ~ 4
    for i in range(32):
        x = (i % 8) * OFFSET
        y = (i // 8) * OFFSET
        diff = 0
        if y == OFFSET:
            diff = OFFSET * DIFFB
        elif y == 2 * OFFSET:
            diff = OFFSET * (DIFFA + DIFFB)
        elif y == 3 * OFFSET:
            diff = OFFSET * (DIFFA + DIFFB*2)
        else:
            y = 0
        keys[i].setswitch(x + diff, y)

    # col  5
    init_col5 = 8 * OFFSET
    for i in range(8):
        x = (i % 2) * OFFSET
        y = (i //2) * OFFSET
        diff = 0
        if y == OFFSET:
            diff = OFFSET * DIFFB
        elif y == 2 * OFFSET:
            diff = OFFSET * (DIFFA + DIFFB)
        elif y == 3 * OFFSET:
            diff = OFFSET * (DIFFA + DIFFB*2)
        else:
            diff = 0
        keys[i + 32].setswitch(x + diff + init_col5, y)

    # col 6
    init_col6 = 10 * OFFSET
    for i in range(8):
        n = i + 42
        x = (i % 2) * OFFSET
        y = (i //2) * OFFSET
        diff = 0
        if y == OFFSET:
            diff = OFFSET * DIFFB
        elif y == 2 * OFFSET:
            diff = OFFSET * (DIFFA + DIFFB)
        else:
            diff = 0
        if n == 47:
            y = -OFFSET
            keys[n-2].setswitch(x + init_col6, y)
        elif n == 48:
            x = 2.5 * OFFSET
            y = 0
            keys[n-2].setswitch(x + init_col6, y)
        elif n == 49:
            x = 2.75 * OFFSET
            y = OFFSET
            keys[n-2].setswitch(x + init_col6, y)
        else:
            keys[i + 40].setswitch(x + diff + init_col6, y)

    # col 7 (sw50 ~ sw57)
    init_col7 = -1 * OFFSET
    for i in range(8):
        x = 0
        y = 0
        diff = 0
        if i >= 4:
            if i == 4:
                diff = 0.25
            elif i == 5:
                diff = 0.25 + 0.75 + 0.625
            elif i == 6:
                diff = 0.25 + 0.75 + 0.625 + 1.25
            elif i == 7:
                diff = 0.25 + 0.75 + 0.625 + 1.25 + 1.25
            y = 4 * OFFSET
        else:
            if i == 1:
                diff = 0.25
            elif i == 2:
                diff = 0.375
            elif i == 3:
                diff = 0.625
            y = i * OFFSET
        diff *= OFFSET
        keys[i + 48].setswitch(x + diff + init_col7, y)

    # col 8 (sw58 ~ sw65)
    init_col8 = (0.5 + 0.25 + 0.5 + 4.0) * OFFSET
    for i in range(8):
        x = 0
        y = 0
        diff = 0
        if i <= 5:
            if i == 0:
                diff = 0
            elif i == 1:
                diff = 1.5 + 0.625
            elif i <= 4:
                diff = 1.5 + 0.625 + (i - 1) * 1.25
            elif i == 5:
                diff = 1.5 + 0.625 + 3 * 1.25 + 0.625 + 0.875
            y = 4 * OFFSET
        elif i == 6:
            diff = 1 * 5 + 0.5 + 1.375
            y = 3 * OFFSET
        elif i == 7:
            diff = 1 * 5 + 0.5 + 1.375 + 0.25
            y = 2 * OFFSET
        diff *= OFFSET
        keys[i + 56].setswitch(x + diff + init_col8, y)

    for i in keys:
        i.printRef()