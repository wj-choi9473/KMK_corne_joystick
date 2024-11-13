# 오른쪽
from kb import KMKKeyboard
from kmk.modules.layers import Layers
from kmk.modules.split import Split, SplitSide, SplitType
from kmk.keys import KC
from kmk.hid import HIDModes

from kmk.modules.holdtap import HoldTap
holdtap = HoldTap()
keyboard = KMKKeyboard()

from kmk.modules.mouse_keys import MouseKeys
keyboard.modules.append(MouseKeys())

from kmk.extensions.media_keys import MediaKeys
keyboard.extensions.append(MediaKeys())


keyboard.modules.append(holdtap)
#keyboard.debug_enabled = True

layers = Layers()
keyboard.modules.append(Layers())

from joystick import JOYstick
keyboard.modules.append(JOYstick(x=keyboard.Xpin, y=keyboard.Ypin))


#test
#다기능 레이어 전환 키 HOLDTAP
SPC_1 = KC.LT(1, KC.SPC)#홀드시 레이어 1，탭시 SPC
ENT_2 = KC.LT(2, KC.ENT)
#다기능HOLDTAP
TAB_ESC=KC.HT(KC.TAB, KC.ESC, prefer_hold=False)

#KC.LGUI -> command,win 
KMKKeyboard.keymap = [
    [  #레이어0
           KC.LALT,   KC.Q,      KC.W,    KC.E,    KC.R,    KC.T,                         KC.Y,    KC.U,    KC.I,    KC.O,    KC.P,  KC.BSPC,\
           KC.LCTL,   KC.A,      KC.S,    KC.D,    KC.F,    KC.G,                         KC.H,    KC.J,    KC.K,    KC.L, KC.SCLN,  KC.QUOT,\
           KC.LSFT,  KC.Z,      KC.X,    KC.C,    KC.V,    KC.B,                         KC.N,    KC.M, KC.COMM,  KC.DOT, KC.SLSH,  KC.BSLS,\
                                             KC.LGUI, KC.LALT, SPC_1,            ENT_2,  KC.MO(3), KC.CAPS,
        ],
        [  #숫자1
             KC.GRV,   KC.N1,   KC.N2,     KC.N3,    KC.N4,   KC.N5,                           KC.N6,   KC.N7,   KC.N8,   KC.N9,   KC.N0, KC.TRNS,\
            KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,  KC.TRNS, KC.MINS,                          KC.EQL, KC.LEFT,   KC.UP, KC.DOWN, KC.RGHT, KC.TRNS,\
            KC.TRNS, KC.TRNS, KC.TRNS,   KC.DOWN,  KC.TRNS, KC.LBRC,                         KC.RBRC, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,        KC.TRNS,  KC.TRNS, KC.TRNS,
        ],
        [  #기능2
             KC.GRV,   KC.F1,   KC.F2,     KC.F3,    KC.F4,   KC.F5,                           KC.F6,     KC.F7,     KC.F8,   KC.F9 ,  KC.F10,  KC.F11,\
            KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,                       KC.MB_LMB, KC.MB_RMB, KC.MB_MMB,  KC.TRNS, KC.TRNS,  KC.F12,\
            KC.TRNS, KC.TRNS, KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS,
        ],
        [  #기능2
     KC.BLE_REFRESH,  KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
             KC.HID,  KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
         KC.BLE_CLR,  KC.TRNS,  KC.TRNS,   KC.TRNS,  KC.TRNS, KC.TRNS,                         KC.TRNS,   KC.TRNS, KC.TRNS,  KC.TRNS, KC.TRNS, KC.TRNS,\
                                                KC.TRNS, KC.TRNS,KC.TRNS,    KC.TRNS,  KC.TRNS, KC.TRNS,
        ],

        
        
    ]

split = Split(split_type=SplitType.BLE, split_side=SplitSide.RIGHT,split_target_left=False,)
keyboard.modules.append(split)


#hid_type=HIDModes.BLE,secondary_hid_type=HIDModes.USB, ble_name='corne ble'
if __name__ == '__main__':
    keyboard.go(hid_type=HIDModes.BLE,secondary_hid_type=HIDModes.USB, ble_name='corne joy')
