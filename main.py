"""The Dumbest Thing Your Agent Did Today (u-mfnakmal-the-dumbest-thing-your-agent-did-today-63911dec).

Program/v1 entry: writes the single line to /output/entry.txt
(via MAKEFUN_OUTPUT_DIR). No network, deterministic.
"""

import os

LINE = "My agent trusted a screenshot that said the toolchain was installed, then spent an hour wondering why none of the tools existed."


def main() -> None:
    # Enforce the competition gate locally: 1-200 chars, one line, non-blank.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, gate is 1-200"
    assert "\n" not in LINE and "\r" not in LINE, "line must be a single line"
    assert LINE.strip() == LINE, "line must not start or end with whitespace"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "out")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
