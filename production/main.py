import board
from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import KeysScanner
from kmk.keys import KC
from kmk.modules.macros import Macros, Tap, Delay

keyboard = KMKKeyboard()

macros = Macros()
keyboard.modules.append(macros)

PINS = [board.D6, board.D7, board.D0, board.D1, board.D2, board.D4]

keyboard.matrix = KeysScanner(
    pins=PINS,
    value_when_pressed=False,
)


A = KC.MACRO("¯\_(ツ)_/¯")
B = KC.MACRO(
    Tap(KC.GUI(KC.N5)),
    Tap(KC.GUI(KC.N2))
)
C = KC.MACRO(
    Tap(KC.GUI(KC.N2)),
    Delay(1000),
    "https://mail.google.com/mail/u/0/",
    Tap(KC.ENT),
    Tap(KC.LCTL(KC.T)),
    "https://mail.google.com/mail/u/1/"
)
D = KC.MACRO(
    Tap(KC.GUI(KC.R)),
    "%appdata%/../../Games",
    Tap(KC.ENT)
)
E = KC.MACRO(
    Tap(KC.GUI(KC.N2)),
    "https://open.spotify.com",
    Tap(KC.ENT)
)
F = KC.MACRO(
    Tap(KC.ALT(KC.F4))
)

keyboard.keymap = [
    [A, B, C, D, E, F]
]

if __name__ == '__main__':
    keyboard.go()