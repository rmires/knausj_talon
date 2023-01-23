app: windows_terminal
-
# makes the commands in terminal.talon available
tag(): terminal
tag(): user.unix_utilities
tag(): user.generic_unix_shell
tag(): user.docker
tag(): user.tmux
tag(): user.git
tag(): user.tabs


# activates the implementation of the commands/functions in terminal.talon
# tag(): user.generic_windows_shell

# makes commands for certain applications available
# you can deactivate them if you do not use the application

settings open: key(ctrl-,)

search it: edit.find()

search it <phrase>$:
    # handle consecutive finds by first escaping out of any previous one
    key(escape)
    # make it so
    edit.find("{phrase}\n")
