"""
Purple Owl v1.0 KMK Build
"""

import board

from kmk.kmk_keyboard import KMKKeyboard
from kmk.scanners.keypad import ShiftRegisterKeys
from kmk.keys import KC
from kmk.modules.layers import Layers
from kmk.extensions.RGB import RGB, AnimationModes


# Pinout
PIN_DAT = board.D9
PIN_CLK = board.D8
PIN_LD  = board.D7
PIN_RGB = board.D6
NUM_KEYS = 61

class PurpleOwl(KMKKeyboard):
    def __init__(self):
        # =============================================================
        # Scanner: 74HC165 scan chain
        self.matrix = ShiftRegisterKeys(
            clock=PIN_CLK,
            data=PIN_DAT,
            latch=PIN_LD,
            key_count=NUM_KEYS,
            value_to_latch=True,
            value_when_pressed=False,
            interval=0.02,
            max_events=64
        )

        # =============================================================
        # Physical Layout
        self.coord_mapping = [
            0,  4,  8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52,
            1,  5,  9, 13, 17, 21, 25, 29, 33, 37, 41, 45, 49, 53,
            2,  6, 10, 14, 18, 22, 26, 30, 34, 38, 42, 46, 50, 54,
            3,  7, 11, 15, 19, 23, 27, 31, 35, 39, 43, 47, 51, 55,
                       56, 57, 58, 59, 60,
        ]

        # =============================================================
        # Extensions
        layer_ext = Layers()
        rgb_ext = RGB(
            pixel_pin=PIN_RGB, 
            num_pixels=16,
            hue_step=13,
            sat_step=26,
            val_step=26,
            animation_speed=5,
            animation_mode=AnimationModes.SWIRL,
        )
        rgb_ext._rgb_tog()

        self.modules = [layer_ext, rgb_ext]

        # =============================================================
        # Keymap
        _______ = KC.TRNS
        XXXXXXX = KC.NO

        # RGB
        UG_TOG = KC.RGB_TOG                     # Toggles RGB
        UG_HUI = KC.RGB_HUI                     # Increase Hue
        UG_HUD = KC.RGB_HUD                     # Decrease Hue
        UG_SAI = KC.RGB_SAI                     # Increase Saturation
        UG_SAD = KC.RGB_SAD                     # Decrease Saturation
        UG_VAI = KC.RGB_VAI                     # Increase Value
        UG_VAD = KC.RGB_VAD                     # Decrease Value
        UG_ANI = KC.RGB_ANI                     # Increase animation speed
        UG_AND = KC.RGB_AND                     # Decrease animation speed
        UG_M0  = KC.RGB_MODE_PLAIN              # Static RGB
        UG_M1  = KC.RGB_MODE_BREATHE            # Breathing animation
        UG_M2  = KC.RGB_MODE_RAINBOW            # Rainbow animation
        UG_M3  = KC.RGB_MODE_BREATHE_RAINBOW    # Breathing rainbow animation
        UG_M4  = KC.RGB_MODE_KNIGHT             # Knight Rider animation
        UG_M5  = KC.RGB_MODE_SWIRL              # Swirl animation

        # Layers
        LOWER = KC.MO(1)
        RAISE = KC.MO(2)

        self.keymap = [
            [   # Base
                KC.ESC,   KC.N1,    KC.N2,    KC.N3,    KC.N4,    KC.N5,    KC.N6,    KC.N7,    KC.N8,    KC.N9,    KC.N0,    KC.MINUS,  KC.EQUAL,  KC.BSPC,  
                KC.TAB,   KC.Q,     KC.W,     KC.E,     KC.R,     KC.T,     KC.Y,     KC.U,     KC.I,     KC.O,     KC.P,     KC.LBRC,   KC.RBRC,   KC.BSLS,
                KC.LCTL,  KC.A,     KC.S,     KC.D,     KC.F,     KC.G,     KC.H,     KC.J,     KC.K,     KC.L,     KC.SCLN,  KC.QUOT,   KC.UP,     KC.ENT,
                KC.LSFT,  KC.Z,     KC.X,     KC.C,     KC.V,     KC.B,     KC.N,     KC.M,     KC.COMM,  KC.DOT,   KC.SLSH,  KC.LEFT,   KC.DOWN,   KC.RGHT,
                                              KC.LGUI,  LOWER,   KC.SPC,    RAISE,    KC.LALT,
            ],
            [   # Lower
                KC.GRV,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                _______,   UG_TOG,  UG_M0,    UG_M1,    UG_M2,    UG_M3,    UG_M4,    UG_M5,    _______,  _______,  _______,  _______,  _______,  _______,
                _______,   UG_HUI,  UG_SAI,   UG_VAI,   UG_ANI,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                _______,   UG_HUD,  UG_SAD,   UG_VAD,   UG_AND,   _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                                              _______,  _______,  _______,  _______,  _______,
            ],
            [   # Raise
                KC.TILD,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,  _______,
                                              _______,  _______,  _______,  _______,  _______,
            ],
        ]


if __name__ == '__main__':
    keyboard = PurpleOwl()
    keyboard.go()
