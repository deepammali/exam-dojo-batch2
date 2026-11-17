**Objective:** Read `/flag` and submit it.

1. Run `/challenge/run`. It installs a copy of a file-copying program with the SETUID bit set so it runs as root, and prints where it was installed.
2. `/flag` is readable only by root. Use that program to make a readable copy of `/flag`, then read the copy.

Note: the plain `cp` in your `PATH` is a different, non-SETUID copy — use the program at the path the challenge prints.
