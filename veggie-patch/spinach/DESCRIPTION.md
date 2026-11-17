**Objective:** Find a hidden host and get the flag from it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. The network is `10.0.0.0/24`. Exactly one other host is on it, at an address you are not told.
3. That host serves the flag on TCP port `31337`. Find the host's address, connect to it, and get the flag.
