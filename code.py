print("Starting")

import board
import supervisor
import board
import digitalio
import storage
import usb_cdc
import usb_hid

from kmk.kmk_keyboard import KMKKeyboard
from kmk.keys import KC
from kmk.scanners import DiodeOrientation
from kmk.modules.layers import Layers
keyboard = KMKKeyboard()
layers = Layers()

keyboard.row_pins = (board.GP14, board.GP15, board.GP16, board.GP17, board.GP18) # Cols
keyboard.col_pins = (board.GP0, board.GP1, board.GP2, board.GP3, board.GP4, board.GP5, board.GP6, board.GP7, board.GP8, board.GP9, board.GP10, board.GP11, board.GP12, board.GP13)             # Rows
keyboard.diode_orientation = DiodeOrientation.COL2ROW

# Keymap
keyboard.keymap = [
    #Layer 0 - base layer
    [KC.ESC   ,KC.N1    ,KC.N2    ,KC.N3    ,KC.N4    ,KC.N5    ,KC.N6    ,KC.N7    ,KC.N8    ,KC.N9    ,KC.N0    ,KC.MINUS ,KC.EQUAL ,KC.BKSP  ,
     KC.TAB   ,KC.Q     ,KC.W     ,KC.E     ,KC.R     ,KC.T     ,KC.Y     ,KC.U     ,KC.I     ,KC.O     ,KC.P     ,KC.LBRC  ,KC.RBRC  ,KC.BSLASH,
     KC.CAPS  ,KC.A     ,KC.S     ,KC.D     ,KC.F     ,KC.G     ,KC.H     ,KC.J     ,KC.K     ,KC.L     ,KC.SCLN  ,KC.QUOT  ,KC.NO    ,KC.ENTER ,
     KC.LSHIFT,KC.NO    ,KC.Z     ,KC.X     ,KC.C     ,KC.V     ,KC.B     ,KC.N     ,KC.M     ,KC.COMM  ,KC.DOT   ,KC.SLSH  ,KC.SLSH  ,KC.RSHIFT,
     KC.LCTRL ,KC.LGUI  ,KC.MO(1) ,KC.NO    ,KC.NO    ,KC.NO    ,KC.SPACE ,KC.NO    ,KC.NO    ,KC.NO    ,KC.RALT  ,KC.NO    ,KC.RGUI  ,KC.RCTRL ],
    #Layer 1 - function layer left
    [KC.TILDE ,KC.F1    ,KC.F2    ,KC.F3    ,KC.F4    ,KC.F5    ,KC.F6    ,KC.F7    ,KC.F8    ,KC.F9    ,KC.F10   ,KC.F11   ,KC.F12   ,KC.DELETE,
     KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.UP    ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,
     KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.LEFT  ,KC.DOWN  ,KC.RIGHT ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,
     KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,
     KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ,KC.RALT  ,KC.TRNS  ,KC.TRNS  ,KC.TRNS  ]
]

if __name__ == '__main__':
    keyboard.go()
    #1234567890-=qwertyuiop[]\Asdfghjkldfghdfghasdfasdffghj';

    #zxcvbnm,.<>/:?hjkljhjklZXc   Hello worrld howdy hey asdfasdfaslkjl'jqwei
