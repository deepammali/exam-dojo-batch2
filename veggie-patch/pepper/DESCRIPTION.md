**Objective:** Make the remote host send you the flag, and submit it.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. Outbound traffic from `10.0.0.1` to TCP port `31337` has been blocked. The host `10.0.0.2` serves the flag on port `31337`.
3. Allow the outbound traffic, then connect to `10.0.0.2:31337` to get the flag.
