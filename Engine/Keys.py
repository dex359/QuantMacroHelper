# Keys.py part of QuickMacro

from pynput.keyboard import Key, KeyCode


TABLE = {

    # SPECIAL KEYS
    'esc':         (Key.esc,                 0x1B),  # Escape
    'backspace':   (Key.backspace,           0x08),  # Backspace
    'tab':         (Key.tab,                 0x09),  # Tab
    'caps_lock':   (Key.caps_lock,           0x14),  # Caps Lock
    'enter':       (Key.enter,               0x0D),  # Enter
    'shift':       (Key.shift,               0x10),  # Shift
    'r_shift':     (Key.shift_r,             0xA1),  # Right Shift
    'ctrl':        (Key.ctrl_l,              0xA2),  # Left Ctrl
    'r_ctrl':      (Key.ctrl_r,              0xA3),  # Right Ctrl
    'alt':         (Key.alt_l,               0xA4),  # Left Alt
    'r_alt':       (Key.alt_r,               0xA5),  # Right Alt
    'space':       (Key.space,               0x20),  # Space
    'ptscr':       (Key.print_screen,        0x2C),  # Print Screen
    'scroll_lock': (Key.scroll_lock,         0x91),  # Scroll Lock
    'pause':       (Key.pause,               0x13),  # Pause
    'insert':      (Key.insert,              0x2D),  # Insert
    'home':        (Key.home,                0x24),  # Home
    'delete':      (Key.delete,              0x2E),  # Delete
    'end':         (Key.end,                 0x23),  # End
    'page_up':     (Key.page_up,             0x21),  # Page Up
    'page_down':   (Key.page_down,           0x22),  # Page Down
    'l_win':       (Key.cmd,                 0x5B),  # Left Windows Key
    'r_win':       (Key.cmd_r,               0x5C),  # Right Windows Key
    'menu':        (Key.menu,                0x5D),  # Menu Key

    # FUNCTIONAL KEYS
    'f1':          (Key.f1,                  0x70),  # F1
    'f2':          (Key.f2,                  0x71),  # F2
    'f3':          (Key.f3,                  0x72),  # F3
    'f4':          (Key.f4,                  0x73),  # F4
    'f5':          (Key.f5,                  0x74),  # F5
    'f6':          (Key.f6,                  0x75),  # F6
    'f7':          (Key.f7,                  0x76),  # F7
    'f8':          (Key.f8,                  0x77),  # F8
    'f9':          (Key.f9,                  0x78),  # F9
    'f10':         (Key.f10,                 0x79),  # F10
    'f11':         (Key.f11,                 0x7A),  # F11
    'f12':         (Key.f12,                 0x7B),  # F12
    'f13':         (Key.f13,                 0x7C),  # F13
    'f14':         (Key.f14,                 0x7D),  # F14
    'f15':         (Key.f15,                 0x7E),  # F15
    'f16':         (Key.f16,                 0x7F),  # F16
    'f17':         (Key.f17,                 0x80),  # F17
    'f18':         (Key.f18,                 0x81),  # F18
    'f19':         (Key.f19,                 0x82),  # F19
    'f20':         (Key.f20,                 0x83),  # F20
    'f21':         (Key.f21,                 0x84),  # F21
    'f22':         (Key.f22,                 0x85),  # F22
    'f23':         (Key.f23,                 0x86),  # F23
    'f24':         (Key.f24,                 0x87),  # F24

    # NUMERIC ROW
    '1':           (KeyCode.from_char('1'),  0x31),  # 1
    '2':           (KeyCode.from_char('2'),  0x32),  # 2
    '3':           (KeyCode.from_char('3'),  0x33),  # 3
    '4':           (KeyCode.from_char('4'),  0x34),  # 4
    '5':           (KeyCode.from_char('5'),  0x35),  # 5
    '6':           (KeyCode.from_char('6'),  0x36),  # 6
    '7':           (KeyCode.from_char('7'),  0x37),  # 7
    '8':           (KeyCode.from_char('8'),  0x38),  # 8
    '9':           (KeyCode.from_char('9'),  0x39),  # 9
    '0':           (KeyCode.from_char('0'),  0x30),  # 0

    # SYMBOLIC KEYS
    'q':           (KeyCode.from_char('q'),  0x51),  # Q
    'w':           (KeyCode.from_char('w'),  0x57),  # W
    'e':           (KeyCode.from_char('e'),  0x45),  # E
    'r':           (KeyCode.from_char('r'),  0x52),  # R
    't':           (KeyCode.from_char('t'),  0x54),  # T
    'y':           (KeyCode.from_char('y'),  0x59),  # Y
    'u':           (KeyCode.from_char('u'),  0x55),  # U
    'i':           (KeyCode.from_char('i'),  0x49),  # I
    'o':           (KeyCode.from_char('o'),  0x4F),  # O
    'p':           (KeyCode.from_char('p'),  0x50),  # P
    'a':           (KeyCode.from_char('a'),  0x41),  # A
    's':           (KeyCode.from_char('s'),  0x53),  # S
    'd':           (KeyCode.from_char('d'),  0x44),  # D
    'f':           (KeyCode.from_char('f'),  0x46),  # F
    'g':           (KeyCode.from_char('g'),  0x47),  # G
    'h':           (KeyCode.from_char('h'),  0x48),  # H
    'j':           (KeyCode.from_char('j'),  0x4A),  # J
    'k':           (KeyCode.from_char('k'),  0x4B),  # K
    'l':           (KeyCode.from_char('l'),  0x4C),  # L
    'z':           (KeyCode.from_char('z'),  0x5A),  # Z
    'x':           (KeyCode.from_char('x'),  0x58),  # X
    'c':           (KeyCode.from_char('c'),  0x43),  # C
    'v':           (KeyCode.from_char('v'),  0x56),  # V
    'b':           (KeyCode.from_char('b'),  0x42),  # B
    'n':           (KeyCode.from_char('n'),  0x4E),  # N
    'm':           (KeyCode.from_char('m'),  0x4D),  # M
    '~' :          (KeyCode.from_char('~'),  0xC0),  # ~
    '-':           (KeyCode.from_char('-'),  0xBD),  # -
    '=':           (KeyCode.from_char('='),  0xBB),  # =
    '[':           (KeyCode.from_char('['),  0xDB),  # [
    ']':           (KeyCode.from_char(']'),  0xDD),  # ]
    '\\':          (KeyCode.from_char('\\'), 0xDC),  # \
    ';':           (KeyCode.from_char(';'),  0xBA),  # ;
    '\'':          (KeyCode.from_char('\''), 0xDE),  # '
    ',':           (KeyCode.from_char(','),  0xBC),  # ,
    '.':           (KeyCode.from_char('.'),  0xBE),  # .
    '/':           (KeyCode.from_char('/'),  0xBF),  # /

    # NUMPAD
    'num_lock':    (Key.num_lock,            0x90),  # Num Lock
    'num0':        (KeyCode.from_char('0'),  0x60),  # Numpad 0
    'num1':        (KeyCode.from_char('1'),  0x61),  # Numpad 1
    'num2':        (KeyCode.from_char('2'),  0x62),  # Numpad 2
    'num3':        (KeyCode.from_char('3'),  0x63),  # Numpad 3
    'num4':        (KeyCode.from_char('4'),  0x64),  # Numpad 4
    'num5':        (KeyCode.from_char('5'),  0x65),  # Numpad 5
    'num6':        (KeyCode.from_char('6'),  0x66),  # Numpad 6
    'num7':        (KeyCode.from_char('7'),  0x67),  # Numpad 7
    'num8':        (KeyCode.from_char('8'),  0x68),  # Numpad 8
    'num9':        (KeyCode.from_char('9'),  0x69),  # Numpad 9
    'num+':        (KeyCode.from_char('+'),  0x6B),  # Numpad +
    'num-':        (KeyCode.from_char('-'),  0x6D),  # Numpad -
    'num*':        (KeyCode.from_char('*'),  0x6A),  # Numpad *
    'num/':        (KeyCode.from_char('/'),  0x6F),  # Numpad /
    'num.':        (KeyCode.from_char('.'),  0x6E),  # Numpad .
}