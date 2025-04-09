# KeyCodes.py part of QuickMacro


from pynput import keyboard as kb


# Mapping table by key names
# abstract names for convenience when creating a macro
KEY_NAMES_TABLE = {

    # Special keys
    'esc':         (kb.Key.esc,                 0x1B),  # Escape
    'backspace':   (kb.Key.backspace,           0x08),  # Backspace
    'tab':         (kb.Key.tab,                 0x09),  # Tab
    'caps_lock':   (kb.Key.caps_lock,           0x14),  # Caps Lock
    'enter':       (kb.Key.enter,               0x0D),  # Enter
    'shift':       (kb.Key.shift,               0x10),  # Shift
    'r_shift':     (kb.Key.shift_r,             0xA1),  # Right Shift
    'ctrl':        (kb.Key.ctrl_l,              0xA2),  # Left Ctrl
    'r_ctrl':      (kb.Key.ctrl_r,              0xA3),  # Right Ctrl
    'alt':         (kb.Key.alt_l,               0xA4),  # Left Alt
    'r_alt':       (kb.Key.alt_r,               0xA5),  # Right Alt
    'space':       (kb.Key.space,               0x20),  # Space
    'ptscr':       (kb.Key.print_screen,        0x2C),  # Print Screen
    'scroll_lock': (kb.Key.scroll_lock,         0x91),  # Scroll Lock
    'pause':       (kb.Key.pause,               0x13),  # Pause
    'insert':      (kb.Key.insert,              0x2D),  # Insert
    'home':        (kb.Key.home,                0x24),  # Home
    'delete':      (kb.Key.delete,              0x2E),  # Delete
    'end':         (kb.Key.end,                 0x23),  # End
    'page_up':     (kb.Key.page_up,             0x21),  # Page Up
    'page_down':   (kb.Key.page_down,           0x22),  # Page Down
    'l_win':       (kb.Key.cmd,                 0x5B),  # Left Windows Key
    'r_win':       (kb.Key.cmd_r,               0x5C),  # Right Windows Key
    'menu':        (kb.Key.menu,                0x5D),  # Menu Key

    # Functional keys
    'f1':          (kb.Key.f1,                  0x70),  # F1
    'f2':          (kb.Key.f2,                  0x71),  # F2
    'f3':          (kb.Key.f3,                  0x72),  # F3
    'f4':          (kb.Key.f4,                  0x73),  # F4
    'f5':          (kb.Key.f5,                  0x74),  # F5
    'f6':          (kb.Key.f6,                  0x75),  # F6
    'f7':          (kb.Key.f7,                  0x76),  # F7
    'f8':          (kb.Key.f8,                  0x77),  # F8
    'f9':          (kb.Key.f9,                  0x78),  # F9
    'f10':         (kb.Key.f10,                 0x79),  # F10
    'f11':         (kb.Key.f11,                 0x7A),  # F11
    'f12':         (kb.Key.f12,                 0x7B),  # F12
    'f13':         (kb.Key.f13,                 0x7C),  # F13
    'f14':         (kb.Key.f14,                 0x7D),  # F14
    'f15':         (kb.Key.f15,                 0x7E),  # F15
    'f16':         (kb.Key.f16,                 0x7F),  # F16
    'f17':         (kb.Key.f17,                 0x80),  # F17
    'f18':         (kb.Key.f18,                 0x81),  # F18
    'f19':         (kb.Key.f19,                 0x82),  # F19
    'f20':         (kb.Key.f20,                 0x83),  # F20
    'f21':         (kb.Key.f21,                 0x84),  # F21
    'f22':         (kb.Key.f22,                 0x85),  # F22
    'f23':         (kb.Key.f23,                 0x86),  # F23
    'f24':         (kb.Key.f24,                 0x87),  # F24

    # Numeric row
    '1':           (kb.KeyCode.from_char('1'),  0x31),  # 1
    '2':           (kb.KeyCode.from_char('2'),  0x32),  # 2
    '3':           (kb.KeyCode.from_char('3'),  0x33),  # 3
    '4':           (kb.KeyCode.from_char('4'),  0x34),  # 4
    '5':           (kb.KeyCode.from_char('5'),  0x35),  # 5
    '6':           (kb.KeyCode.from_char('6'),  0x36),  # 6
    '7':           (kb.KeyCode.from_char('7'),  0x37),  # 7
    '8':           (kb.KeyCode.from_char('8'),  0x38),  # 8
    '9':           (kb.KeyCode.from_char('9'),  0x39),  # 9
    '0':           (kb.KeyCode.from_char('0'),  0x30),  # 0

    # Symbolic keys
    'q':           (kb.KeyCode.from_char('q'),  0x51),  # Q
    'w':           (kb.KeyCode.from_char('w'),  0x57),  # W
    'e':           (kb.KeyCode.from_char('e'),  0x45),  # E
    'r':           (kb.KeyCode.from_char('r'),  0x52),  # R
    't':           (kb.KeyCode.from_char('t'),  0x54),  # T
    'y':           (kb.KeyCode.from_char('y'),  0x59),  # Y
    'u':           (kb.KeyCode.from_char('u'),  0x55),  # U
    'i':           (kb.KeyCode.from_char('i'),  0x49),  # I
    'o':           (kb.KeyCode.from_char('o'),  0x4F),  # O
    'p':           (kb.KeyCode.from_char('p'),  0x50),  # P
    'a':           (kb.KeyCode.from_char('a'),  0x41),  # A
    's':           (kb.KeyCode.from_char('s'),  0x53),  # S
    'd':           (kb.KeyCode.from_char('d'),  0x44),  # D
    'f':           (kb.KeyCode.from_char('f'),  0x46),  # F
    'g':           (kb.KeyCode.from_char('g'),  0x47),  # G
    'h':           (kb.KeyCode.from_char('h'),  0x48),  # H
    'j':           (kb.KeyCode.from_char('j'),  0x4A),  # J
    'k':           (kb.KeyCode.from_char('k'),  0x4B),  # K
    'l':           (kb.KeyCode.from_char('l'),  0x4C),  # L
    'z':           (kb.KeyCode.from_char('z'),  0x5A),  # Z
    'x':           (kb.KeyCode.from_char('x'),  0x58),  # X
    'c':           (kb.KeyCode.from_char('c'),  0x43),  # C
    'v':           (kb.KeyCode.from_char('v'),  0x56),  # V
    'b':           (kb.KeyCode.from_char('b'),  0x42),  # B
    'n':           (kb.KeyCode.from_char('n'),  0x4E),  # N
    'm':           (kb.KeyCode.from_char('m'),  0x4D),  # M
    '~' :          (kb.KeyCode.from_char('~'),  0xC0),  # ~
    '-':           (kb.KeyCode.from_char('-'),  0xBD),  # -
    '=':           (kb.KeyCode.from_char('='),  0xBB),  # =
    '[':           (kb.KeyCode.from_char('['),  0xDB),  # [
    ']':           (kb.KeyCode.from_char(']'),  0xDD),  # ]
    '\\':          (kb.KeyCode.from_char('\\'), 0xDC),  # \
    ';':           (kb.KeyCode.from_char(';'),  0xBA),  # ;
    '\'':          (kb.KeyCode.from_char('\''), 0xDE),  # '
    ',':           (kb.KeyCode.from_char(','),  0xBC),  # ,
    '.':           (kb.KeyCode.from_char('.'),  0xBE),  # .
    '/':           (kb.KeyCode.from_char('/'),  0xBF),  # /

    # Numpad
    'num_lock':    (kb.Key.num_lock,            0x90),  # Num Lock
    'num0':        (kb.KeyCode.from_char('0'),  0x60),  # Numpad 0
    'num1':        (kb.KeyCode.from_char('1'),  0x61),  # Numpad 1
    'num2':        (kb.KeyCode.from_char('2'),  0x62),  # Numpad 2
    'num3':        (kb.KeyCode.from_char('3'),  0x63),  # Numpad 3
    'num4':        (kb.KeyCode.from_char('4'),  0x64),  # Numpad 4
    'num5':        (kb.KeyCode.from_char('5'),  0x65),  # Numpad 5
    'num6':        (kb.KeyCode.from_char('6'),  0x66),  # Numpad 6
    'num7':        (kb.KeyCode.from_char('7'),  0x67),  # Numpad 7
    'num8':        (kb.KeyCode.from_char('8'),  0x68),  # Numpad 8
    'num9':        (kb.KeyCode.from_char('9'),  0x69),  # Numpad 9
    'num+':        (kb.KeyCode.from_char('+'),  0x6B),  # Numpad +
    'num-':        (kb.KeyCode.from_char('-'),  0x6D),  # Numpad -
    'num*':        (kb.KeyCode.from_char('*'),  0x6A),  # Numpad *
    'num/':        (kb.KeyCode.from_char('/'),  0x6F),  # Numpad /
    'num.':        (kb.KeyCode.from_char('.'),  0x6E),  # Numpad .
}

# Mapping table by Key & KeyCode instances from pynput.keyboard
KEY_CODES_TABLE = {}
for kn, (kc, vc) in KEY_NAMES_TABLE.items():
    KEY_CODES_TABLE[kc] = kn, vc

# Mapping table by MS Windows vc_code
# check full reference here:
# https://learn.microsoft.com/ru-ru/windows/win32/inputdev/virtual-key-codes
VC_CODES_TABLE = {}
for kn, (kc, vc) in KEY_NAMES_TABLE.items():
    VC_CODES_TABLE[vc] = kn, kc


class _KeyObj:

    def __init__(self, key_name, key_code, vc_code):
        self.key_name = key_name
        self.key_code = key_code
        self.vc_code  = vc_code


class _KeyBuffer:

    def __init__(self):
        self._buffer  = {}

    def get(self, arg):
        try:
            return self._buffer[arg]
        except KeyError:
            if isinstance(arg, str):
                if not arg in KEY_NAMES_TABLE:
                    raise NameError(f"Invalid key name: {arg}")
                obj = _KeyObj(arg, KEY_NAMES_TABLE[arg][0], KEY_NAMES_TABLE[arg][1])
            elif isinstance(arg, kb.Key) or isinstance(arg, kb.KeyCode):
                obj = _KeyObj(KEY_CODES_TABLE[arg][0], arg, KEY_CODES_TABLE[arg][1])
            elif isinstance(arg, int) and 0 < arg < 255:
                obj = _KeyObj(VC_CODES_TABLE[arg][0], VC_CODES_TABLE[arg][1], arg)
            else:
                raise AttributeError(f" Invalid arg while creating key: {arg}")
            self._buffer[obj.key_name] = self._buffer[obj.key_code] = self._buffer[obj.vc_code] = obj
            return obj


_KeyBuffer = _KeyBuffer()
Key = lambda arg: _KeyBuffer.get(arg)