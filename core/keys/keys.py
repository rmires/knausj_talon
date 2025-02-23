from talon import Context, Module, actions, app

from ..user_settings import get_list_from_csv


def setup_default_alphabet():
    """set up common default alphabet.

    no need to modify this here, change your alphabet using alphabet.csv"""
    initial_default_alphabet = "air bat cap drum each fine gust harp sit jury crunch look made near odd pit quench red sun trap urge vest whale plex yank zip".split(
        " "
    )
    initial_letters_string = "abcdefghijklmnopqrstuvwxyz"
    initial_default_alphabet_dict = dict(
        zip(initial_default_alphabet, initial_letters_string)
    )

    return initial_default_alphabet_dict


alphabet_list = get_list_from_csv(
    "alphabet.csv", ("Letter", "Spoken Form"), setup_default_alphabet())

hex_alphabet = "A B C D E F".split(" ")
hex_letters_string = "abcdef"

default_digits = "zero one two three four five six seven eight nine".split(" ")
numbers = [str(i) for i in range(10)]
default_f_digits = (
    "one two three four five six seven eight nine ten eleven twelve".split(" ")
)

mod = Module()
mod.list("letter", desc="The spoken phonetic alphabet")
mod.list("hex_letter", desc="Spoken hex letters (a-f)")
mod.list("symbol_key", desc="All symbols from the keyboard")
mod.list("arrow_key", desc="All arrow keys")
mod.list("number_key", desc="All number keys")
mod.list("modifier_key", desc="All modifier keys")
mod.list("function_key", desc="All function keys")
mod.list("special_key", desc="All special keys")
mod.list("punctuation", desc="words for inserting punctuation into text")


@mod.capture(rule="{self.modifier_key}+")
def modifiers(m) -> str:
    "One or more modifier keys"
    return "-".join(m.modifier_key_list)


@mod.capture(rule="{self.arrow_key}")
def arrow_key(m) -> str:
    "One directional arrow key"
    return m.arrow_key


@mod.capture(rule="<self.arrow_key>+")
def arrow_keys(m) -> str:
    "One or more arrow keys separated by a space"
    return str(m)


@mod.capture(rule="{self.number_key}")
def number_key(m) -> str:
    "One number key"
    return m.number_key


@mod.capture(rule="{self.letter}")
def letter(m) -> str:
    "One letter key"
    return m.letter


@mod.capture(rule="{self.hex_letter}")
def hex_letter(m) -> str:
    "One hex letter key"
    return m.hex_letter


@mod.capture(rule="{self.letter}")
def upper_letter(m) -> str:
    "Return one upper case"
    return m.letter.upper()


@mod.capture(rule="{self.letters}")
def letters(m) -> str:
    "Multiple letter keys"
    return m.letters


@mod.capture(rule="{self.hex_letters}")
def hex_letters(m) -> str:
    "Multiple hex letter keys"
    return m.hex_letters


@mod.capture(rule="{self.special_key}")
def special_key(m) -> str:
    "One special key"
    return m.special_key


@mod.capture(rule="{self.symbol_key}")
def symbol_key(m) -> str:
    "One symbol key"
    return m.symbol_key


@mod.capture(rule="{self.function_key}")
def function_key(m) -> str:
    "One function key"
    return m.function_key


@mod.capture(rule="( <self.letter> | <self.number_key> | <self.symbol_key> )")
def any_alphanumeric_key(m) -> str:
    "any alphanumeric key"
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.special_key> )"
)
def unmodified_key(m) -> str:
    """A single key with no modifiers.

    Excludes arrow keys and function keys
    """
    return str(m)


@mod.capture(
    rule="( <self.letter> | <self.number_key> | <self.symbol_key> "
    "| <self.arrow_key> | <self.function_key> | <self.special_key> )"
)
def all_unmodified_key(m) -> str:
    "A single key including F keys and arrow keys, with no modifiers"
    return str(m)


@mod.capture(rule="{self.modifier_key}* <self.all_unmodified_key>")
def key(m) -> str:
    "A single key with optional modifiers"
    try:
        mods = m.modifier_key_list
    except AttributeError:
        mods = []
    return "-".join(mods + [m.all_unmodified_key])


@mod.capture(rule="<self.key>+")
def keys(m) -> str:
    "A sequence of one or more keys with optional modifiers"
    return " ".join(m.key_list)


@mod.capture(rule="{self.letter}+")
def letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.letter_list)


@mod.capture(rule="{self.hex_letter}+")
def hex_letters(m) -> str:
    "Multiple letter keys"
    return "".join(m.hex_letter_list)


ctx = Context()
modifier_keys = {
    # If you find 'alt' is often misrecognized, try using 'alter'.
    "alter": "alt",  #'alter': 'alt',
    "control": "ctrl",  #'troll':   'ctrl',
    "shift": "shift",  #'sky':     'shift',
    "super": "super",
}
if app.platform == "mac":
    modifier_keys["command"] = "cmd"
    modifier_keys["option"] = "alt"
ctx.lists["self.modifier_key"] = modifier_keys
ctx.lists["self.letter"] = alphabet_list

# `punctuation_words` is for words you want available BOTH in dictation and as
# key names in command mode.
# `symbol_key_words` is for key names that should be available in command mode, but NOT during dictation.
# XXX - There should be a way to make some things only available in dictation
# mode...
punctuation_words = {
    "back tick": "`",
    #  "grave": "`",
    "comma": ",",
    # Workaround for issue with conformer b-series; see #946
    "coma": ",",
    "period": ".",
    #  "full stop": ".",
    "semicolon": ";",
    "colon": ":",
    "forward slash": "/",
    "question mark": "?",
    "exclamation mark": "!",
    "exclamation point": "!",
    "asterisk": "*",
    "hash sign": "#",
    "number sign": "#",
    "percent sign": "%",
    "at sign": "@",
    "and sign": "&",
    "ampersand": "&",
    # Currencies
    "dollar sign": "$",
    "pound sign": "£",
}
symbol_key_words = {
    "dot": ".",
    #  "point": ".",
    "quote": "'",
    "question": "?",
    "apostrophe": "'",
    "L square": "[",
    "left square": "[",
    "square": "[",
    "R square": "]",
    "right square": "]",
    "slash": "/",
    "backslash": "\\",
    "minus": "-",
    #  "dash": "-",
    "equals": "=",
    "plus": "+",
    "tilde": "~",
    "bang": "!",
    #  "down score": "_",
    "underscore": "_",
    "paren": "(",
    "L paren": "(",
    "left paren": "(",
    "R paren": ")",
    "right paren": ")",
    #  "brace": "{",
    #  "left brace": "{",
    "curly": "{",
    "l curly": "{",
    "left curly": "{",
    #  "r brace": "}",
    #  "right brace": "}",
    "right curly": "}",
    "r curly": "}",
    "right curly": "}",
    "angle": "<",
    "left angle": "<",
    "less than": "<",
    "R angle": ">",
    "right angle": ">",
    "greater than": ">",
    "star": "*",
    "hash": "#",
    "percent": "%",
    "caret": "^",
    "ampersand": "&",
    "pipe": "|",
    "dub quote": '"',
    "double quote": '"',
    # Currencies
    "dollar": "$",
}

# make punctuation words also included in {user.symbol_keys}
symbol_key_words.update(punctuation_words)
ctx.lists["self.punctuation"] = punctuation_words
ctx.lists["self.symbol_key"] = symbol_key_words
number_keys = dict(zip(default_digits, numbers))
ctx.lists["self.number_key"] = number_keys


hex_spoken = dict(zip(list(alphabet_list.values())[0:6], hex_letters_string))
hex_alphabet = dict(zip(hex_alphabet, hex_letters_string))
ctx.lists["self.hex_letter"] = {**hex_spoken, **hex_alphabet, **number_keys}

ctx.lists["self.arrow_key"] = {
    "down": "down",
    "left": "left",
    "right": "right",
    "up": "up",
}

simple_keys = [
    #  "end",
    "enter",
    "escape",
    #"home",
    #"insert",
    #"pagedown",
    #"pageup",
    "space",
    "tab",
]

alternate_keys = {
    "wipe": "backspace",
    "delete": "delete",
    "page up": "pageup",
    "page down": "pagedown",
}
# mac apparently doesn't have the menu key.
if app.platform in ("windows", "linux"):
    alternate_keys["menu key"] = "menu"
    alternate_keys["print screen"] = "printscr"

special_keys = {k: k for k in simple_keys}
special_keys.update(alternate_keys)
ctx.lists["self.special_key"] = special_keys
ctx.lists["self.function_key"] = {
    f"F {default_f_digits[i]}": f"f{i + 1}" for i in range(12)
}


@mod.action_class
class Actions:
    def move_cursor(s: str):
        """Given a sequence of directions, eg. 'left left up', moves the cursor accordingly using edit.{left,right,up,down}."""
        for d in s.split():
            if d in ("left", "right", "up", "down"):
                getattr(actions.edit, d)()
            else:
                raise RuntimeError(f"invalid arrow key: {d}")
