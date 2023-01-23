tag: user.tmux
-
mux: "tmux "

#session management
mux new session: insert("tmux new ")
mux reload:
    key(`)
    key(r)
mux sessions:
    key(`)
    key(s)
mux name session:
    key(`)
    key($)
mux kill session: insert("tmux kill-session -t ")
#window management
mux new window:
    key(`)
    key(c)
mux window <number>:
    key(`)
    key('{number}')
mux previous window:
    key(alt-h)
mux next window:
    key(alt-l)
mux rename window:
    key(`)
    key(,)
mux close window:
    key(`)
    key(&)
#pane management
mux split horizontal:
    key(`)
    key(-)
mux split vertical:
    key(`)
    key(|)
mux next pane:
    key(`)
    key(o)
mux move <user.arrow_key>:
    key(`)
    key(arrow_key)
mux close pane:
    key(`)
    key(x)
#Say a number right after this command, to switch to pane
mux pane numbers:
    key(`)
    key(q)
