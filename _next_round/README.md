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

## dns/ — (not built yet)
DNS/DHCP has no ready pwn.college challenge to import, so it must be custom.
A DNS "flag in a TXT record, retrieved with dig" challenge is tractable;
a full DHCP-config challenge is awkward to self-contain. Build on request.
