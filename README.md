# OffensiveSecurity

A comprehensive collection of offensive security scripts for cloud platforms (AWS, Azure, GCP), Active Directory (AD), and web application security testing.

## 📁 Repository Structure

```
OffensiveSecurity/
├── AWS/                    # Amazon Web Services security scripts
│   ├── PowerShell/         # AWS PowerShell scripts
│   ├── Bash/               # AWS Bash scripts
│   └── Python/             # AWS Python scripts
├── Azure/                  # Microsoft Azure security scripts
│   ├── PowerShell/         # Azure PowerShell scripts
│   ├── Bash/               # Azure Bash scripts
│   └── Python/             # Azure Python scripts
├── GCP/                    # Google Cloud Platform security scripts
│   ├── PowerShell/         # GCP PowerShell scripts
│   ├── Bash/               # GCP Bash scripts
│   └── Python/             # GCP Python scripts
├── AD/                     # Active Directory security scripts
│   ├── PowerShell/         # AD PowerShell scripts
│   ├── Bash/               # AD Bash scripts (Linux-based tools)
│   └── Python/             # AD Python scripts
└── Web/                    # Web application security scripts
    ├── PowerShell/         # Web PowerShell scripts
    ├── Bash/               # Web Bash scripts
    └── Python/             # Web Python scripts
```

## 🎯 Categories

### ☁️ Cloud Security

| Platform | Description | Directory |
|----------|-------------|-----------|
| **AWS** | Scripts for Amazon Web Services security assessments including IAM enumeration, S3 bucket analysis, Lambda exploitation, and more | [AWS/](AWS/) |
| **Azure** | Scripts for Microsoft Azure security assessments including Azure AD, managed identities, storage accounts, and DevOps pipelines | [Azure/](Azure/) |
| **GCP** | Scripts for Google Cloud Platform security assessments including IAM, Cloud Storage, Cloud Functions, and GKE | [GCP/](GCP/) |

### 🖥️ On-Premises & Applications

| Category | Description | Directory |
|----------|-------------|-----------|
| **Active Directory** | Scripts for Windows AD environment security assessments including Kerberos attacks, privilege escalation, and lateral movement | [AD/](AD/) |
| **Web Applications** | Scripts for web application security testing including reconnaissance, vulnerability scanning, and exploitation | [Web/](Web/) |

## 🛠️ Languages

Scripts are organized by programming language within each category:

| Language | Extension | Use Cases |
|----------|-----------|-----------|
| **PowerShell** | `.ps1` | Windows environments, Azure, AWS, native Windows AD tools |
| **Bash** | `.sh` | Linux environments, cross-platform CLI tools, automation |
| **Python** | `.py` | Cross-platform, complex logic, API interactions, automation |

## ⚡ Quick Start

1. Clone the repository:
   ```bash
   git clone https://github.com/nithin0x/OffensiveSecurity.git
   cd OffensiveSecurity
   ```

2. Navigate to the desired category and language:
   ```bash
   cd AWS/Python  # For AWS Python scripts
   ```

3. Review the README in each directory for specific usage instructions.

## 📋 Prerequisites

Depending on the scripts you want to use, you may need:

- **Cloud CLIs**: AWS CLI, Azure CLI, Google Cloud SDK
- **Python 3.7+** with relevant libraries (boto3, azure-sdk, google-cloud-*)
- **PowerShell 5.1+** or PowerShell Core with relevant modules
- **Linux tools**: LDAP utilities, Kerberos tools, curl, jq

## ⚠️ Disclaimer

**These scripts are intended for authorized security testing and educational purposes only.**

- Always obtain proper authorization before performing any security assessments
- Only use these tools against systems you own or have explicit permission to test
- The author is not responsible for any misuse or damage caused by these tools
- Follow responsible disclosure practices for any vulnerabilities discovered

## 📜 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please ensure any scripts you contribute:

1. Include proper documentation and usage examples
2. Follow the existing directory structure
3. Include appropriate error handling
4. Are tested before submission

## 📬 Contact

For questions, suggestions, or contributions, please open an issue or submit a pull request.