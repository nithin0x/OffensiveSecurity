#!/usr/bin/env bash

# iam-policy-simulator.sh
# Simulate IAM actions (one per line) from a policy file against a principal
# using the AWS CLI. Intended for authorized testing in lab accounts only.

# Author: Nithin Kumar

set -euo pipefail
IFS=$'\n\t'

# Defaults
PROFILE="default"
USER_ARN=""
POLICY_FILE="policy.txt"

print_help() {
  cat <<-HELP
Usage: $0 -a ARN [-p PROFILE] [-f FILE]

  -a, --arn      IAM principal ARN to simulate (user/role)  (required)
  -p, --profile  AWS CLI profile to use (default: "${PROFILE}")
  -f, --file     File containing action names, one per line (default: "${POLICY_FILE}")
  -h, --help     Show this help

Examples:
  $0 -a arn:aws:iam::123456789012:user/joe -p test -f actions.txt

HELP
}

# Parse arguments
while [[ $# -gt 0 ]]; do
  case "$1" in
    -p|--profile)
      PROFILE="$2"
      shift 2
      ;;
    -a|--arn)
      USER_ARN="$2"
      shift 2
      ;;
    -f|--file)
      POLICY_FILE="$2"
      shift 2
      ;;
    -h|--help)
      print_help
      exit 0
      ;;
    *)
      echo "Unknown option: $1"
      print_help
      exit 1
      ;;
  esac
done

# Validate inputs
if [[ -z "${USER_ARN}" ]]; then
  echo "Error: --arn is required."
  print_help
  exit 1
fi

if [[ ! -f "${POLICY_FILE}" ]]; then
  echo "Error: policy file '${POLICY_FILE}' not found."
  exit 1
fi

echo "Simulating permissions for: ${USER_ARN}"
echo "AWS profile:             ${PROFILE}"
echo "Actions file:            ${POLICY_FILE}"
echo "----------------------------------------"

# Read each action from the file, skip blanks and comments
while IFS= read -r line || [[ -n "$line" ]]; do
  # Trim whitespace
  action="$(echo "$line" | xargs)"
  # Skip empty lines and lines starting with '#'
  [[ -z "$action" || "${action:0:1}" == "#" ]] && continue

  echo "Action: ${action}"
  aws iam simulate-principal-policy \
    --policy-source-arn "${USER_ARN}" \
    --action-names "${action}" \
    --profile "${PROFILE}" \
    --output json
  echo "----------------------------------------"
done < "${POLICY_FILE}"
