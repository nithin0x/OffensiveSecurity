#!/usr/bin/env python3
"""
Generate username or email permutations from a file of names/usernames.

Input lines may be full names, comma-separated names, dotted usernames,
underscored usernames, hyphenated usernames, or existing email addresses.
"""

import argparse
import re
import unicodedata
from pathlib import Path


SPLIT_RE = re.compile(r"[\s,._-]+")
CAMEL_RE = re.compile(r"(?<=[a-z])(?=[A-Z])")
HEADER_WORDS = {
    "first",
    "firstname",
    "firstinitial",
    "last",
    "lastname",
    "lastinitial",
    "middle",
    "middlename",
    "middleinitial",
    "name",
    "username",
    "email",
}


def normalize_domain(domain):
    if not domain:
        return None
    return domain.strip().lower().removeprefix("@")


def normalize_token(value):
    value = unicodedata.normalize("NFKD", value)
    value = value.encode("ascii", "ignore").decode("ascii")
    return re.sub(r"[^a-z0-9]", "", value.lower())


def split_name(value):
    value = value.strip()
    if not value or value.startswith("#"):
        return []

    local_part = value.split("@", 1)[0]
    local_part = CAMEL_RE.sub(" ", local_part)
    parts = [normalize_token(part) for part in SPLIT_RE.split(local_part)]
    return [part for part in parts if part]


def unique(items):
    seen = set()
    for item in items:
        if item not in seen:
            seen.add(item)
            yield item


def generate_usernames(parts):
    if not parts:
        return []

    if len(parts) == 1:
        return parts

    first_name = parts[0]
    last_name = parts[-1]
    first_initial = first_name[0]
    last_initial = last_name[0]

    permutations = [
        first_name,
        last_name,
        f"{first_name}{last_name}",
        f"{first_name}.{last_name}",
        f"{first_initial}{last_name}",
        f"{first_initial}.{last_name}",
        f"{first_name}{last_initial}",
        f"{first_name}.{last_initial}",
        f"{first_initial}{last_initial}",
        f"{first_initial}.{last_initial}",
        f"{last_name}{first_name}",
        f"{last_name}.{first_name}",
        f"{last_name}{first_initial}",
        f"{last_name}.{first_initial}",
        f"{last_initial}{first_name}",
        f"{last_initial}.{first_name}",
        f"{last_initial}{first_initial}",
        f"{last_initial}.{first_initial}",
    ]

    if len(parts) > 2:
        middle_name = parts[1]
        middle_initial = middle_name[0]
        permutations.extend(
            [
                f"{first_name}{middle_name}{last_name}",
                f"{first_name}.{middle_name}.{last_name}",
                f"{first_initial}{middle_initial}{last_name}",
                f"{first_initial}.{middle_initial}.{last_name}",
                f"{first_initial}{middle_initial}{last_initial}",
                f"{first_initial}.{middle_initial}.{last_initial}",
            ]
        )

    return list(unique(permutations))


def format_output(username, domain):
    if domain:
        return f"{username}@{domain}"
    return username


def generate_from_file(input_file, domain=None):
    domain = normalize_domain(domain)
    results = []

    for line in Path(input_file).read_text(encoding="utf-8").splitlines():
        parts = split_name(line)
        if len(parts) > 1 and all(part in HEADER_WORDS for part in parts):
            continue

        usernames = generate_usernames(parts)
        results.extend(format_output(username, domain) for username in usernames)

    return list(unique(results))


def write_results(results, output_file):
    if output_file == "-":
        for result in results:
            print(result)
        return

    Path(output_file).write_text("\n".join(results) + ("\n" if results else ""), encoding="utf-8")
    print(f"Wrote {len(results)} entries to {output_file}")


def main():
    parser = argparse.ArgumentParser(
        description="Generate username or email permutations from an input file."
    )
    parser.add_argument("input_file", help="File containing one name, username, or email per line")
    parser.add_argument(
        "positional_domain",
        nargs="?",
        help="Optional email domain. If omitted, bare usernames are generated.",
    )
    parser.add_argument(
        "-d",
        "--domain",
        dest="flag_domain",
        help="Optional email domain. If omitted, bare usernames are generated.",
    )
    parser.add_argument(
        "-o",
        "--output",
        help="Output file path, or '-' for stdout. Default: emails.txt with a domain, otherwise usernames.txt",
    )
    args = parser.parse_args()

    domain = args.flag_domain or args.positional_domain
    output_file = args.output or ("emails.txt" if domain else "usernames.txt")

    results = generate_from_file(args.input_file, domain)
    if not results:
        raise SystemExit("No usernames generated; check the input file.")

    write_results(results, output_file)


if __name__ == "__main__":
    main()
