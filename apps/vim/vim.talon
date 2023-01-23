# USAGE: - See doc/vim.md for usage and tutorial
#  - See code/vim.py very implementation and additional motion grammars
#
# FILES:
#  Files are split up as follows largely to reduce the grammar size and prevent
#  talent from being overloaded when trying to switch contexts process the
#  grammar tree. Unfortunately this makes it slightly more difficult to find
#  commands quickly.
#   * vim.talon - general settings, tag management, and commands the work across
#                 all modes
#   * vim_motion_mode.talon   - commands that work across all motion modes
#   * vim_terminal_mode.talon - commands that only work in terminal mode
#   * vim_normal_mode.talon   - commands that only work in normal mode
#   * vim_visual_mode.talon   - commands that only work in visual mode
#   * vim_insert_mode.talon   - commands that only work in insert mode
#
# NOTE:
# Where applicable I try to explicitly select appropriate API for terminal
# escaping, etc. However in cases where it is unlikely you will say a command
# from terminal mode, I don't bother. Example "save file" doesn't have explicit
# terminal escaping. This also helps an embedded vim running inside of a vim
# terminal work properly.
#
# TODO:
#  - add word jumping and searching for command mode
#  - test on windows and mac
#  - everything in this files should technically use _exterm() version of
#    functions
#
# BUGS:
#  - With sending the command-line mode commands in the background via RPC we
#  miss out on the display of some features. Ex: ALEInfo becomes unreadable...
#  need to figure out how to fix this.
app: vim
and not tag: user.vim_command_mode
-

tag(): user.vim
tag(): user.tabs
# TODO - add line_commands, etc

# Talon VIM plugin tags - see plugins/ for implementations Comment out plugins
# below that you don't use Also see vim_motion_mode.talon for plugin grammars
# that aren't enabled in terminal mode

# they should only include things that you want enabled in effectively all
# modes, including terminal mode. anything else should be more granularly
# enabled
#tag(): user.vim_fzf
# tag(): user.vim_plug
# tag(): user.vim_copilot

# To the settings below dictate how certain parts of Talon VIM will work. You
# can leave them or tweak them to your needs.
settings():
    # Whether or not to always revert back to the previous mode. Example, if
    # you are in insert mode and say 'delete word' it will delete one word and
    # keep you in insert mode. Same as ctrl-o in VIM.
    user.vim_preserve_insert_mode = 1

    # Whether or not to automatically adjust modes when using commands. Example
    # saying "go line 50" will first switch you out of INSERT into NORMAL and
    # then jump to the line. Disabling this setting would put :50\n into your
    # file if you say "row 50" while in INSERT mode.
    user.vim_adjust_modes = 1

    # Select whether or not talon should dispatch notifications on mode changes
    # that are made. Not yet completed, as notifications are kind of wonky on
    # Linux
    user.vim_notify_mode_changes = 0

    # Whether or not all commands that transfer out of insert mode should also
    # automatically escape out of terminal mode. Turning this on is quite
    # troublesome.
    user.vim_escape_terminal_mode = 0

    # When issuing counted actions in vim you can prefix a count that will
    # dictate how many times the command is run, however some peoples talon
    # grammar already allows you to utter a number without a prefix (ex: voice
    # command "ten" will put 10 in your file) so we want to cancel any existing
    # counts that might already by queued in vim in error.
    #
    # This also helps prevent accidental number queueing if talon
    # mishears a command such as "delete line" as "delete" "nine". Without this
    # setting, if you then said "undo" it would undo the last 9 changes, which
    # is annoying.
    #
    # This setting only applies to commands run through the actual counted
    # actions grammar itself
    user.vim_cancel_queued_commands = 1

    # When you are escaping queued commands, it seems vim needs time to recover
    # before issuing the subsequent commands. This controls how long it waits,
    # in seconds
    user.vim_cancel_queued_commands_timeout = 0.20

    # It how long to wait before issuing commands after a mode change. You
    # want adjust this if when you say things like undo from INSERT mode, an
    # "u" gets inserted into INSERT mode. It in theory that shouldn't be
    # required if using pynvim.
    user.vim_mode_change_timeout = 0.25

    # When you preserve mode and switch into into insert mode it will often
    # move your cursor, which can mess up the commands you're trying to run from
    # insert. This setting controls the cursor move
    user.vim_mode_switch_moves_cursor = 0

    # Whether or not use pynvim rpc if it is available
    user.vim_use_rpc = 1

    # Adds debug output to the talon log
    user.vim_debug = 0

###
# File editing and management
###
file save all: user.vim_command_mode_exterm(":wa\n")

# no \n as a saftey measure
(close | quit) all: user.vim_command_mode_exterm(":qa")

force (close | quit) all: user.vim_command_mode_exterm(":qa!")

force (close | quit): user.vim_command_mode_exterm(":q!\n")
file (edit | open): user.vim_command_mode_exterm(":e ")
file (edit | open) clip:
    user.vim_command_mode_exterm(":e ")
    edit.paste()
file (edit | open) <user.paths>: user.vim_command_mode_exterm(":e {paths}\n")
(reload [vim] config | config reload):
    user.vim_command_mode_exterm(":so $MYVIMRC\n")

###
# Navigation, movement and jumping
#
# NOTE: Majority of more core movement verbs are in code/vim.py
###
# XXX - line conflicts too much with nine,
#[(go|jump)] [to] line <number>:
# XXX - lately row is conflicting with numb
go row <number>:
    user.vim_command_mode_exterm(":{number}\n")

    # These are especially useful when in terminal mode and you want to jump to
    # something in normal mode that is in the history. Doubley so if you use
    # set relativenumber in terminal mode
[go] relative up [line] <number_small>:
    user.vim_normal_mode_exterm("{number_small}k")

[go] relative down [line] <number_small>:
    user.vim_normal_mode_exterm("{number_small}j")

push line <number>:
    user.vim_command_mode_exterm(":{number}\n")
    user.vim_normal_mode_np("$a")

# jump list
# XXX - I'm not sure these are well usable from the terminal?
jump show: user.vim_command_mode_exterm(":jumps\n")
jump last [entry]: user.vim_normal_mode_exterm_key("ctrl-o")
jump next [entry]: user.vim_normal_mode_exterm_key("ctrl-i")

# scrolling and page position
# NOTE counted scrolling his handled in vim.py
# XXX - it seems like comboing \n in command mode doesn't work well?
# scroll [on] line <number>: user.vim_command_mode_exterm(":{number}\nzt")
# center [on] line <number>: user.vim_command_mode_exterm(":{number}\nz.")
scroll top: user.vim_normal_mode_exterm("zt")
scroll center: user.vim_normal_mode_exterm("zz")
scroll bottom: user.vim_normal_mode_exterm("zb")
# XXX - change these exist scroll top curse ?
# scroll top reset cursor: user.vim_normal_mode_exterm("z\n")
# scroll middle reset cursor: user.vim_normal_mode_exterm("z.")
# scroll bottom reset cursor: user.vim_normal_mode_exterm("z ")

###
# Buffers
###
(buf | buffer) list: user.vim_normal_mode_exterm(" bb")
(buf | buffer) (close | delete) [current]: user.vim_normal_mode_exterm(" bd")
(buf | buffer) (close | delete) all:
    user.vim_normal_mode_exterm(" b")
    key(ctrl-d)
    key(y)
[go] (buf | buffer) (left | prev): user.vim_normal_mode_exterm(" bp")
[go] (buf | buffer) (right | next): user.vim_normal_mode_exterm(" bn")
(buf | buffer) <number>: user.vim_normal_mode_exterm("\\{number}")
(buf | buffer) new : user.vim_normal_mode_exterm(" bN")

###
# Splits
#
# XXX - it may be cleaner to have these in a vim.py function
# XXX - most split open commands should be able to take a buffer argument
###
# creating splits
(split new horizontal):
    user.vim_set_normal_mode_exterm()
    key("ctrl-w")
    key(s)

(split new [vertical]):
    user.vim_set_normal_mode_exterm()
    key("ctrl-w")
    key(v)

# open specified buffer in new split
split (buf | buffer) <number>:
    user.vim_set_normal_mode_exterm()
    key("ctrl-w")
    key(v)
    user.vim_normal_mode_exterm(" wl")
    user.vim_normal_mode_exterm("\\{number}")

split (close | kill):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(q)

# navigating splits
split <user.vim_arrow>: user.vim_normal_mode_exterm(" w{vim_arrow}")

split next:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(w)
split (previous | prev):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(W)
split <number_small>:
    user.vim_normal_mode_exterm(" {number_small}")

# window resizing
(split equalize | balance):
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(=)

#split grow:
# XXX - it would be nice if this could grow it fatter but keep it centered,
# like if were in split zen mode, but we want to make the middle split
# bigger

# XXX - it would be nice to have percents for these resizes..
# atm comboing these with ordinals is best, but may add number support
split taller:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(+)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split shorter:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(-)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split fatter:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(>)
    # XXX - This should restore the original mode, is sometimes I use this from
    # terminal mode
split skinnier:
    user.vim_set_normal_mode_exterm()
    key(ctrl-w)
    key(<)
set split width: user.vim_command_mode_exterm(":resize ")
set split height: user.vim_set_command_mode_exterm(":vertical resize ")


###
# Settings
###
# Sometimes the command bar height is too big, this makes it smaller
rebalance command: user.vim_command_mode_exterm(":set cmdheight=1\n")
# XXX - this is a weird edge case because we actually probably want to slip back
# to the terminal mode after setting options, but atm
# user.vim_normal_mode_exterm() implies no preservation
lights off: user.vim_command_mode_exterm(":noh\n")
(unset paste | set no paste): user.vim_command_mode_exterm(":set nopaste\n")
# very useful for reviewing code you don't want to accidintally edit if talon
# mishears commands
set modifiable: user.vim_command_mode_exterm(":set modifiable\n")
(unset modifiable | set no modifiable):
    user.vim_command_mode_exterm(":set nomodifiable\n")

# XXX - this is quite slow pasting into a terminal, so might want to move
# this register into the paste register and then use the native?
(paste from | pastor) [register] <user.unmodified_key>:
    user.vim_any_motion_mode_exterm('"{unmodified_key}p')

###
# Mode Switching
###
[mode] normal: user.vim_set_normal_mode_np()
[mode] insert: user.vim_set_insert_mode()
mode terminal: user.vim_set_terminal_mode()
# command mode: user.vim_set_command_mode()
mode command [line]: user.vim_any_motion_mode_exterm_key(":")
(mode replace | overwrite): user.vim_set_replace_mode()
mode visual replace: user.vim_set_visual_replace_mode()
# This always conflicts with virtual pop somehow...
[mode] visual: user.vim_set_visual_mode()
mode line: user.vim_set_visual_line_mode()
mode block: user.vim_set_visual_block_mode()

# sort of quasi-modes - see vim_command_line.talon
show history: user.vim_command_mode(":hist\n")
command line (search | history) [mode]:
    user.vim_any_motion_mode_exterm_key("q:")
search command [mode]: user.vim_any_motion_mode_exterm_key("q/")

###
# Searching
###
# case insensitive search
search: user.vim_any_motion_mode_exterm("/\\c")

search clip:
    user.vim_any_motion_mode_exterm("/\\c")
    edit.paste()

# case sensitive search
search exact: user.vim_any_motion_mode_exterm("/\\C")

search exact clip:
    user.vim_any_motion_mode_exterm("/\\C")
    edit.paste()

# XXX - probably rename these
#search (reversed|reverse) <user.text>$:
#    user.vim_any_motion_mode_exterm("?\\c{text}\n")

search (reversed | reverse): user.vim_any_motion_mode_exterm("?\\c")

search exact (reversed | reverse): user.vim_any_motion_mode_exterm("?\\C")

###
# Visual Mode
###
(select | highlight) all: user.vim_normal_mode_exterm("ggVG")
reselect: user.vim_normal_mode_exterm("gv")

###
# Terminal mode
###

# case user doesn'i have `VIM mode:t` in titlestring
(term | terminal) new: user.vim_normal_mode_exterm(" '")
