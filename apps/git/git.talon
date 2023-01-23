tag: terminal
and tag: user.git
and not tag: user.vim
-
git {user.git_command} [<user.git_arguments>]:
    args = git_arguments or ""
    "git {git_command}{args} "
git commit [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git commit{args} --message '{message}", "'")
git stash [push] [<user.git_arguments>] message [<user.prose>]:
    args = git_arguments or ""
    message = prose or ""
    user.insert_between("git stash push{args} --message '{message}", "'")

# Optimistic execution for frequently used commands that are harmless (don't
# change repository or index state).
git status$: "git status\n"
git add patch$: "git add --patch\n"
git show head$: "git show HEAD\n"
git diff$: "git diff\n"
git diff (cached | cashed)$: "git diff --cached\n"

git add all: "git add -a"
git commit: "git commit -m "
git pull: "git pull"
git pull main: "git pull origin main"
git push: "git push"
git checkout: "git checkout"
git log: "git log"
git fetch: "git fetch"

# Convenience
git clone clipboard:
    insert("git clone ")
    edit.paste()
git checkout clipboard:
    insert("git fetch")
    key("enter")
    insert("git checkout ")
    edit.paste()
git diff highlighted:
    edit.copy()
    insert("git diff ")
    edit.paste()
git diff clipboard:
    insert("git diff ")
    edit.paste()
git add highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
git add clipboard:
    insert("git add ")
    edit.paste()
git commit highlighted:
    edit.copy()
    insert("git add ")
    edit.paste()
    insert("\ngit commit\n")
