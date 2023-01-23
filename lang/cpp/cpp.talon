tag: user.cplusplus
-

tag(): user.code_comment_line
tag(): user.code_comment_block_c_like
tag(): user.code_data_bool
tag(): user.code_data_null
tag(): user.code_functions
tag(): user.code_functions_common
tag(): user.code_libraries
tag(): user.code_libraries_gui
tag(): user.code_operators_array
tag(): user.code_operators_assignment
tag(): user.code_operators_bitwise
tag(): user.code_operators_math
tag(): user.code_operators_pointer

settings():
    user.code_private_function_formatter = "SNAKE_CASE"
    user.code_protected_function_formatter = "SNAKE_CASE"
    user.code_public_function_formatter = "SNAKE_CASE"
    user.code_private_variable_formatter = "SNAKE_CASE"
    user.code_protected_variable_formatter = "SNAKE_CASE"
    user.code_public_variable_formatter = "SNAKE_CASE"

^tip <user.cpp_tips>:
    insert(cpp_tips)
    key(alt-`)

type [<user.cpp_modifiers>] <user.cpp_integral>:
    "{cpp_modifiers} {cpp_integral} "
# Nouns.

<user.cpp_namespaced_type> : "{cpp_namespaced_type} "

state <user.cpp_known_namespaces>: insert(user.cpp_naked_namespace(cpp_known_namespaces))
<user.cpp_known_namespaces> scope : insert(user.cpp_namespace_with_joiner(cpp_known_namespaces))

<user.cpp_namespaced_template>:
    insert(cpp_namespaced_template)
    insert("<>")
    key(left)


label <user.text>:
    insert(user.formatted_text(text, "SNAKE_CASE,NO_SPACES"))
    insert(":")
    key(enter)

class <user.text>:
    insert(user.formatted_text(text, "PUBLIC_CAMEL_CASE,NO_SPACES"))

meth <user.text>:
    insert(user.formatted_text(text, "PRIVATE_CAMEL_CASE,NO_SPACES"))

struct <user.text>:
    insert(user.formatted_text(text, "SNAKE_CASE,NO_SPACES"))

field <user.text>:
    insert(user.formatted_text(text, "PRIVATE_CAMEL_CASE,NO_SPACES"))

local <user.text>:
    insert(user.formatted_text(text, "PRIVATE_CAMEL_CASE,NO_SPACES"))

funk <user.text>:
    insert(user.formatted_text(text, "SNAKE_CASE,NO_SPACES"))
