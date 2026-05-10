import re
import sys

MAX_LEN = 100

PATTERN = re.compile(
    rf"^(feat|fix|docs|style|refactor|test|chore|build|ci|perf)"
    rf"(\([a-z0-9\-_]+\))?: .{{1,{MAX_LEN}}}$"
)

IGNORED_PREFIXES = (
    "Merge",
    "Revert",
    "Release",
    "fixup!",
    "squash!",
    "Initial commit",
)

def main():
    commit_msg_file = sys.argv[1]

    with open(commit_msg_file, "r", encoding="utf-8") as f:
        lines = f.read().splitlines()

    # ignorar comentarios git (# ...)
    lines = [line for line in lines if line and not line.startswith("#")]

    if not lines:
        return 0

    subject = lines[0].strip()

    if subject.startswith(IGNORED_PREFIXES):
        return 0

    if not PATTERN.match(subject):
        print("\n❌ Invalid commit message format\n")
        print("Expected:")
        print("  type(scope): description\n")
        print("Examples:")
        print("  feat(auth): add login system")
        print("  fix(api): handle null response\n")
        sys.exit(1)

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
