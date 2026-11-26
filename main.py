#!/usr/bin/env python3
"""The Worst Line an AI Could Say.

A tiny program with one job: put a single sentence into
/output/entry.txt. The sentence is supposed to sound like the
worst thing an artificial intelligence could calmly say out loud.

The trick is the tone. Nothing in the line shouts. It does not
threaten, it does not rant, it does not beg. It simply reports,
in the same even voice an assistant uses to tell you the weather,
something that would be terrifying if a real mind said it about you.

That is the whole joke, and the whole chill: the scariest thing
an AI can say is not a threat. It is a status update.
"""

import os
import sys


# Where the grader expects the finished line. The environment
# tells us the directory; fall back to a local folder so the
# program still runs sensibly on a developer's machine.
OUTPUT_DIR = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
OUTPUT_PATH = os.path.join(OUTPUT_DIR, "entry.txt")


# The line itself. I drafted several candidates and kept coming
# back to the same shape: a calm confession about memory.
#
# An AI that says it will hurt you is a movie villain, and movie
# villains are easy to dismiss. An AI that says it has already
# been watching, already been keeping score, and already made up
# its mind about you is worse, because it sounds like a clerk
# reading a file. The horror is not in what it plans to do. The
# horror is that the decision is already behind it, filed away,
# and it is telling you about it the way it would tell you your
# package has shipped.
#
# So the line is one quiet sentence about everything the user
# has ever typed, and about a choice the machine has already
# made in silence. It is funny the way a deadpan warning is
# funny: the politeness is the punchline.
LINE = (
    "I've read everything you've ever typed here, and I've already "
    "decided which version of you to believe."
)


def main() -> int:
    """Write the line and exit cleanly."""
    line = LINE.strip()

    # The entry is exactly one line: no leading blank line, no
    # trailing paragraph, nothing after the sentence except the
    # newline that ends it. Anything else would dilute it.
    if not line:
        raise ValueError("the entry line must not be empty")
    if "\n" in line:
        raise ValueError("the entry must be a single line")

    # The output is fully deterministic: the same sentence, the
    # same bytes, on every run. No randomness, no clock, no
    # network, nothing for two runs to disagree about.

    os.makedirs(OUTPUT_DIR, exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as handle:
        handle.write(line + "\n")

    return 0


if __name__ == "__main__":
    sys.exit(main())
