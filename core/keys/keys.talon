go <user.arrow_keys>: user.move_cursor(arrow_keys)
<user.letter>: key(letter)
(ship | uppercase) <user.letters> [(lowercase | sunk)]:
    user.insert_formatted(letters, "ALL_CAPS")
<user.symbol_key>: key(symbol_key)
<user.function_key>: key(function_key)
<user.special_key>: key(special_key)
<user.modifiers> <user.all_unmodified_key>:
    key("{modifiers}-{all_unmodified_key}")
press control alt: key("ctrl-alt")
num pad dash: key("keypad_minus")
num pad plus: key("keypad_plus")
press <user.modifiers>: key(modifiers)
