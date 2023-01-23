# XXX - this should have os awarenss

from talon import Context, Module

mod = Module()
mod.list("paths_public", desc="Common paths")
mod.list("paths_private", desc="Common private paths")
mod.list("folder_paths_public", desc="Common paths")
mod.list("folder_paths_private", desc="Common private paths")
ctx = Context()

TALON_REPO = "fidget"
arch_linux_paths = {
    "packman hooks": "/etc/pacman.d/hooks/",
}
# paths that will work with pivot command
linux_folder_paths = {
    "var F S": "/var/fs/",
    "opt": "/opt/",
    "ida config": "~/.idapro/",
    "ida plugins": "~/.idapro/plugins/",
    "ida themes": "~/.idapro/themes/",
    "ida loaders": "~/.idapro/loaders/",
    "user services": "~/.config/systemd/user/",
    "user timers": "~/.config/systemd/user/",
    "services": "/etc/systemd/system/",
    "you dev rules": "/etc/udev/rules.d/",
    "sue doers": "/etc/sudoers.d/",
    "vim sessions": "~/.vim/sessions/",
    "vim plugins": "~/.vim/plugged/",
    "vim": "~/.vim/",
    "temp": "/tmp/",
    "config": "/etc/",
    "it see": "/etc/",
    "bin": "/bin/",
    "S bin": "/sbin/",
    "var run": "/var/run/",
    "var log": "/var/log/",
    "user": "/usr/",
    "user bin": "/usr/bin/",
    "user S bin": "/usr/sbin/",
    "user lib": "/usr/lib/",
    "user lib debug": "/usr/lib/debug/",
    "user src": "/usr/src/",
    "user src debug": "/usr/src/debug/",
    "user share": "/usr/share/",
    "user local": "/usr/local/",
    "user local bin": "/usr/local/bin/",
    "user local S bin": "/usr/local/sbin/",
    "user local lib": "/usr/local/lib/",
    "user local config": "/usr/local/etc/",
    "user local share": "/usr/local/share/",
    "lib": "/lib/",
    "dev": "/dev/",
    "log": "/var/log/",
    "kernel trace": "/sys/kernel/tracing/",
    "K mem events": "/sys/kernel/tracing/events/kmem",
    "custom snippets": "~/.vim/custom-snippets/",
    "vim snippets": "~/.vim/plugged/vim-snippets/UltiSnips/",
    "talon": f"~/.talon/user/{TALON_REPO}/",
    "talon user": "~/.talon/user/",
    "back": "../",
    "tunnel": "~/.ssh/",
    "S S H": "~/.ssh/",
    "raffi": "~/.config/rofi/",
    "network manager": "/etc/NetworkManager/",
    "network manager dispatcher": "/etc/NetworkManager/dispatcher.d/",
    "network manager config": "/etc/NetworkManager/conf.d/",
    # ubuntu-esque stuff
    "lib linux": "/lib/x86_64-linux-gnu/",
    "lib sixty four": "/lib64/",
    "lib thirty two": "/lib32/",
    "lib three two": "/lib32/",
    "proc": "/proc/",
    "root": "/root/",
    "packman cache": "/var/cache/pacman/pkg/",
    "yay cache": "~/.cache/yay/",
    "open snitch rules": "/etc/opensnitchd/rules/",
    "local apps": "~/.local/share/applications/",
    "Polly bar": "~/.config/polybar/",
    "python sight packages": "/usr/lib/python3.10/site-packages",
}

linux_file_paths = {
    "G D B init": "~/.gdbinit",
    "known hosts": "~/.ssh/known_hosts",
    "password": "/etc/passwd",
    "groups": "/etc/group",
    "shadow": "/etc/shadow",
    "hosts": "/etc/hosts",
    "resolve": "/etc/resolv.conf",
    "null": "/dev/null",
    "dev null": "/dev/null",
    "zero": "/dev/zero",
    "vim": "~/.vim/",
    "grub config": "/etc/default/grub",
    "crypt tab": "/etc/crypttab",
    "f stab": "/etc/fstab",
    "make init config": "/etc/mkinitcpio.conf",
    "boot config": "/boot/grub/grub.cfg",
    "journal config": "/etc/systemd/journald.conf",
    "lib virt config": "/etc/libvirt/libvirtd.conf",
    "tunnel config": "~/.ssh/config",
    "shell config": "~/.zshrc",
    "zish config": "~/.zshrc",
    "zish R C": "~/.zshrc",
    "bash config": "~/.bashrc",
    "bash R C": "~/.bashrc",
    "git config": ".git/config",
    "poly bar config": "~/.config/polybar/config",
    "eye three config": "~/.i3/config",
    "vim config": "~/.vimrc",
    "c snippets": "~/.vim/plugged/vim-snippets/UltiSnips/c.snippets",
    "mark down snippets": "~/.vim/plugged/vim-snippets/UltiSnips/markdown.snippets",
    "python snippets": "~/.vim/plugged/vim-snippets/UltiSnips/python.snippets",
    "bash snippets": "~/.vim/plugged/vim-snippets/UltiSnips/bash.snippets",
    "kitty config": "~/.config/kitty/kitty.conf",
    "grub defaults": "/etc/default/grub",
    "raffi config": "~/.config/rofi/rofi.rasi",
    "raffi theme": "~/.config/rofi/colors.rasi",
    "lisp log": "~/.cache/nvim/lsp.log",
    "slab info": "/proc/slabinfo",
    "kernel active trace": "/sys/kernel/tracing/trace",
    "kernel current tracer": "/sys/kernel/tracing/current_tracer",
    "kernel available tracersm": "/sys/kernel/tracing/available_tracers",
    "Q emu config": "/etc/libvirt/qemu.conf",
    "proxy chains": "~/.proxychains/proxychains.conf",
    "open snitch log": "/var/log/opensnitchd.log",
    "howdy config": "/usr/lib/security/howdy/config.ini",
    "et see keeper": "/etc/etckeeper/etckeeper.conf",
    "var log messages": "/var/log/messages",
}

# this is used for specific commands like pivot
ctx.lists["user.folder_paths_public"] = {
    **linux_folder_paths,
}
ctx.lists["user.folder_paths_private"] = {}

# this is used for any path based commands that don't care of about files or
# folder difference
ctx.lists["user.paths_public"] = {**linux_folder_paths, **linux_file_paths}

# Arch Linux

ctx.lists["user.paths_private"] = {}

# XXX - add support for selecting
windows_paths = {
    "desktop": "%USERPROFILE%\\Desktop",
    "profile": "%USERPROFILE%",
    "root": "%SYSTEMROOT%",
    "windows": "%SYSTEMROOT%",
    "system": "%SYSTEMROOT%\\System32",
    "drivers": "%SYSTEMROOT%\\System32\\Drivers",
    "programs": "%PROGRAMFILES%",
}


@mod.capture(rule="{user.folder_paths_public}")
def folder_paths_public(m) -> str:
    "One path representing a public folder"
    return m.folder_paths_public


@mod.capture(rule="{user.folder_paths_private}")
def folder_paths_private(m) -> str:
    "One path representing a public folder"
    return m.folder_paths_private


@mod.capture(rule="{user.paths_public}")
def paths_public(m) -> str:
    "One public path representing a file or folder"
    return m.paths_public


@mod.capture(rule="{user.paths_private}")
def paths_private(m) -> str:
    "One private path representing a file or folder"
    return m.paths_private


@mod.capture(rule="<user.folder_paths_public>|<user.folder_paths_private>")
def folder_paths(m) -> str:
    "One public or private path that represents a folder"
    return m


@mod.capture(rule="<user.paths_public>|<user.paths_private>")
def paths(m) -> str:
    "One public or private path that represents a file or folder"
    return m


@mod.action_class
class Actions:
    def path_traverse(num: int) -> str:
        """creates a string num path traversal sequences"""
        return "../" * num

    # XXX - this should be an overridable type of method so that we can
    # have language specific escaping, for multiple types of scenarios
    def escape_path(path: str):
        """Escape separators in a path string"""
        return path.replace("/", "\\/")
