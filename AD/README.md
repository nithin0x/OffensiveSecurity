# Active Directory Offensive Security Scripts

This directory contains offensive security scripts targeting Active Directory (AD) environments.

## Overview

Scripts in this folder are designed for security assessments, penetration testing, and red team operations against Windows Active Directory infrastructure.

## Subdirectories

| Directory | Description |
|-----------|-------------|
| [PowerShell/](PowerShell/) | PowerShell scripts for AD security assessments |
| [Bash/](Bash/) | Bash scripts for AD security assessments (Linux-based tools) |
| [Python/](Python/) | Python scripts for AD security assessments |

## Common Use Cases

- Domain enumeration and reconnaissance
- Kerberos attacks (Kerberoasting, AS-REP Roasting)
- Password spraying and credential attacks
- Privilege escalation paths identification
- ACL abuse and delegation attacks
- Group Policy analysis
- Trust relationship enumeration
- Certificate Services (ADCS) exploitation
- Lateral movement techniques
- Persistence mechanisms

## Prerequisites

- Domain-joined Windows machine (for PowerShell scripts)
- Impacket suite (for Python scripts)
- LDAP tools and Kerberos utilities (for Linux-based attacks)

## Disclaimer

These scripts are intended for authorized security testing only. Always obtain proper authorization before performing any security assessments.
