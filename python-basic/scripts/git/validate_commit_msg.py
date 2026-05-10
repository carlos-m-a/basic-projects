import re
import sys

# Conventional Commits regex
PATTERN = re.compile(
    r"^(feat|fix|docs|style|refactor|test|chore|build|ci|perf)(\(.+\))?: .{1,72}$"
)

def main():
    commit_msg_file = sys.argv[1]

    with open(commit_msg_file, "r", encoding="utf-8") as f:
        msg = f.read().strip()

    # Ignorar merge commits automáticamente
    if msg.startswith("Merge"):
        return 0

    if not PATTERN.match(msg):
        print("\n❌ Invalid commit message format")
        print("\nExpected format:")
        print("  type(scope): description")
        print("\nExamples:")
        print("  feat(auth): add login system")
        print("  fix(api): handle null response\n")
        sys.exit(1)

    return 0


if __name__ == "__main__":
    main()
