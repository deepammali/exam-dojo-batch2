**Objective:** Make the remote host send you the flag, and submit it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. The host `10.0.0.2` listens on TCP port `31337`. Connect to it and send exactly the line `Hello, World!`.
3. On that message the host replies with the flag.
