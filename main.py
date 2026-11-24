"""One-Sentence Absurd Invention Pitch.

Writes a single-sentence pitch for a ridiculous invention that fixes a
tiny everyday annoyance to /output/entry.txt.
"""

from pathlib import Path


# The pitch: one sentence, naming the invention (a tax-filing toaster),
# the tiny everyday annoyance (doing taxes), and its silly mechanism
# (it burns only the evidence). 60 characters, well under the 220 cap.
ENTRY = "A toaster that files your taxes and burns only the evidence."


def main() -> None:
    output_path = Path("/output/entry.txt")
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(ENTRY, encoding="utf-8")


if __name__ == "__main__":
    main()
