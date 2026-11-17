# Next-round challenges (NOT wired into the live exam)

Staged challenges for a FUTURE exam round. They are committed but deliberately
NOT listed in dojo.yml, so pwn.college ingests the repo without showing them in
the current exam. Test each one on a live dojo before putting it in an exam.

## osint/ — Web-recon OSINT  (fulfils Assignment 7)
A company web server on 10.0.0.2 leaks the flag. Intended solve:
  - curl http://10.0.0.2/           (company site)
  - curl http://10.0.0.2/robots.txt (reveals  Disallow: /backup/)
  - curl http://10.0.0.2/backup/    (flag is in an HTML comment)
Self-contained, no live internet. Uses dojjail + flask (same stack as the
working Sniffing Cookies challenge).

### To add it to a dojo
1. Move osint/ under the module folder, e.g.  veggie-patch/osint/
2. In dojo.yml, under the module's challenges:
     - id: osint
       name: Challenge N - OSINT
       privileged: true     # needs dojjail network namespaces
3. In grade.py MARKS, add:  "osint": <marks>
4. Deploy, update the dojo, restart the instance, then smoke-test:
     /challenge/run ; curl 10.0.0.2/robots.txt ; curl 10.0.0.2/backup/

## dns/ — DNS TXT-record lookup  (fulfils Assignment 5, name-resolution half)
A DNS server on 10.0.0.2 stores the flag in the TXT record for `flag.lab.test`.
Intended solve:
  - dig TXT flag.lab.test @10.0.0.2 +short
  - or: nslookup -type=TXT flag.lab.test 10.0.0.2
Self-contained; a hand-rolled minimal DNS responder (no external packages).
The DNS wire format was verified locally against real dig/nslookup.

### Wire it in the same way as osint/ (own run, privileged: true, add marks).

TEST CAVEAT: the student needs a DNS client (dig / nslookup / host). These were
NOT in the base challenge Dockerfile; the dojo workspace may still provide them.
Confirm `which dig nslookup host` inside the challenge when you test. If none are
present, install dnsutils in the dojo image, or the challenge can be solved with
a short python query.

## dhcp/ — (not built)
DHCP is broadcast lease negotiation (DORA) and doesn't map cleanly to a
"find the flag" container; left out. The DNS challenge above covers the
name-resolution half of Assignment 5.
