# Grading for the Lab Internal Exam - Batch 2.
#
# Edit the settings below, push, and update the dojo. The admin Grades page
# (/dojo/<dojo>/admin/grades) recalculates every time it loads, so you can
# change marks after the exam is over.

# Marks per challenge, keyed by challenge id from dojo.yml.
# Paper 2: Section A = 1 mark each, Section B = 3 marks each (total 20).
MARKS = {
    "carrot": 1,      # Q1  Access Control level2
    "onion": 1,       # Q2  Send
    "potato": 1,      # Q3  Access Control level5 (SETUID cp)
    "pepper": 1,      # Q4  Firewall 3
    "garlic": 1,      # Q5  Access Control level10
    "spinach": 2,     # Q6  Scan 1
    "radish": 2,      # Q7  Access Control level17
    "celery": 2,      # Q8  Monitor 1
    "ginger": 2,      # Q9  Access Control level11
    "pumpkin": 2,     # Q10 TCP Handshake
    "osint": 2,       # Q11 OSINT (optional extra)
    "dns": 2,         # Q12 DNS  (optional extra)
}

MODULE_ID = "veggie-patch"

# Exam window (IST). Only solves at or after EXAM_START and at or before
# EXAM_END earn marks; solves outside the window score 0. ISO 8601 with the
# +05:30 offset = IST. Both None = no time limit.
# Set these for the Batch 2 slot, e.g. "2026-11-18T14:00:00+05:30".
EXAM_START = "2026-11-18T14:00:00+05:30"
EXAM_END   = "2026-11-18T16:00:00+05:30"

#
# Grading logic: you shouldn't need to change anything below.
#

import datetime

IST = datetime.timezone(datetime.timedelta(hours=5, minutes=30), "IST")


def parse_time(value):
    if not value:
        return None
    return datetime.datetime.fromisoformat(str(value).replace("Z", "+00:00"))


def fmt(value):
    return f"{value:g}"


def grade(data):
    if any(field not in data for field in ["solves", "modules", "course"]):
        return None

    start = parse_time(EXAM_START)
    end = parse_time(EXAM_END)

    # Collect EVERY solve time per challenge. pwn.college records one solve per
    # (user, challenge), and more than one account can be linked to the same
    # reg number (e.g. a pre-exam test solve plus the student's real solve), so
    # a challenge may have several solve times here. Do not take only the
    # earliest: an out-of-window solve must never hide a valid in-window one.
    solve_times = {}
    for solve in data["solves"]:
        if solve["module_id"] != MODULE_ID:
            continue
        solve_times.setdefault(solve["challenge_id"], []).append(parse_time(solve["timestamp"]))

    module = next((m for m in data["modules"] if m["id"] == MODULE_ID), {})

    assignments = []
    earned_total = 0
    max_total = 0
    for challenge in module.get("challenges", []):
        challenge_id = challenge["id"]
        max_marks = MARKS.get(challenge_id, 0)
        max_total += max_marks

        times = sorted(solve_times.get(challenge_id, []))
        windowed = [t for t in times if (not start or t >= start) and (not end or t <= end)]
        earned = 0
        if not times:
            status = "Not solved"
        elif windowed:
            earned = max_marks
            status = f"Solved at {windowed[0].astimezone(IST):%H:%M} IST"
        elif start and times[-1] < start:
            status = f"Solved before window ({times[0].astimezone(IST):%d %b %H:%M} IST)"
        else:
            status = f"Solved after window ({times[-1].astimezone(IST):%d %b %H:%M} IST)"
        earned_total += earned

        # Key order matters: the admin "Download CSV" button reads these
        # five columns by position (name, deadline, weight, progress, credit).
        assignments.append({
            "name": challenge.get("name", challenge_id),
            "deadline": EXAM_END or "-",
            "marks": max_marks,
            "progress": f"{status}: {fmt(earned)}/{fmt(max_marks)}",
            "credit": earned / max_marks if max_marks else 0,
        })

    return {
        "overall": {
            "credit": earned_total / max_total if max_total else 0,
            "letter": f"{fmt(earned_total)} / {fmt(max_total)} marks",
        },
        "assignments": assignments,
    }
