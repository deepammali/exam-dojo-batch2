**Objective:** Complete a TCP handshake by hand with the remote host to reveal the flag.

1. Run `/challenge/run`. Your shell moves into the challenge network as host `10.0.0.1`. Type `exit` to leave it.
2. Perform a full TCP three-way handshake with `10.0.0.2`. Your opening packet must use TCP `sport=31337`, `dport=31337`, `seq=31337`.
3. Send the SYN, read the host's SYN-ACK, and send the matching ACK with the correct sequence and acknowledgement numbers. When the handshake completes, the flag is printed.
