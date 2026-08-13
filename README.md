# Cybersecurity Portfolio - Joel Massicot

> Technology and Business Operations Leader | Cybersecurity | US/Dutch Veteran | US-EU Bridge

[![ISC2 CC](https://img.shields.io/badge/ISC2-Certified_in_Cybersecurity-green)](https://www.isc2.org/)
[![Google Cybersecurity](https://img.shields.io/badge/Google-Cybersecurity_Professional-blue)](https://grow.google/certificates/cybersecurity/)
[![Security+](https://img.shields.io/badge/CompTIA-Security%2B_In_Progress-orange)]()

---

## About

19-year entrepreneur and US Marine Corps / Army veteran transitioning into cybersecurity with a focus on SOC operations, threat detection, and security automation.

**Background:** Co-founded and led Masacote Entertainment for 19 years, managing global operations across 30+ countries, building digital platforms, and developing teams under pressure. Now applying that operational discipline to cybersecurity.

**Location:** Breda, Netherlands. Legally authorized to work in both the US and EU (US/Dutch dual citizen) with active knowledge of NIST CSF and EU NIS2 frameworks.

---

## Published Work

| Title | Type | Date |
|---|---|---|
| [How I Detected a Network Attack in My Home Lab Using Splunk and Nmap](https://www.linkedin.com/pulse/how-i-detected-network-attack-my-home-lab-using-splunk-joel-massicot-uwoce/) | LinkedIn Article | Aug 5, 2026 |

Covers: Nmap reconnaissance from Kali Linux, UFW firewall blocking, Splunk SIEM ingestion of 76,234 events, SPL query isolating 10 attack events from the source IP. Full end-to-end blue team exercise with screenshots.

---

## Certifications

| Certification | Issuer | Status |
|---|---|---|
| Certified in Cybersecurity (CC) | ISC2 | Active (Feb 2025 - Feb 2028) |
| Google Cybersecurity Professional Certificate | Google / Coursera | Complete (Jun 2025) |
| Google AI Essentials | Google | Complete (Jan 2026) |
| Google Prompting Essentials | Google | Complete (Mar 2025) |
| CompTIA Security+ (SY0-701) | CompTIA | In Progress |

---

## Home Lab

**Architecture:**
- Red Team (Attack): Kali Linux -- IP 192.168.153.128 -- Nmap, Metasploit, Wireshark
- Blue Team (Defense): Linux Mint -- IP 192.168.153.129 -- Splunk SIEM, UFW firewall
- Network isolation: VMware host-only network between machines

**Completed Exercises:**

| Exercise | Date | Description |
|---|---|---|
| Lab architecture setup | Aug 4, 2026 | VMware isolation, static IPs, Splunk install, /var/log directory monitoring |
| Nmap reconnaissance + UFW blocking | Aug 4, 2026 | Kali ran Nmap scan against Mint; UFW blocked and logged the traffic |
| Splunk SIEM detection | Aug 4, 2026 | Ingested 76,234 events; SPL query isolated 10 UFW BLOCK events from Kali source IP |

**SPL Detection Query:**
```
index=main sourcetype=syslog "UFW BLOCK" src_ip=192.168.153.128
```

**Next exercises:** SPL alert rules, Metasploit exploitation, log correlation, Python automation

---

## Google Cybersecurity Certificate -- Portfolio Artifacts

Hands-on portfolio work completed as part of the Google Cybersecurity Professional Certificate. All artifacts are in the [`google-cybersecurity-certificate/`](./google-cybersecurity-certificate/) folder.

Key work includes:
- NIST CSF incident response application
- Security incident reports (network analysis)
- Risk register and data leak worksheet
- File permissions audit (Linux)
- SQL access control filtering
- Vulnerability assessment using NIST SP 800-30

*Files are in .docx format -- download individually or browse the folder.*

---

## Repository Structure

```
cybersecurity-portfolio/
|- home-lab/                          Home lab setup, SIEM config, architecture notes
|- google-cybersecurity-certificate/  Google cert portfolio artifacts
|- security-tools/                    Python scripts for threat detection
|- automation/                        Security monitoring automation scripts
|- write-ups/                         Lab write-ups and published articles
```

---

## Skills

| Category | Tools / Concepts |
|---|---|
| **SIEM** | Splunk (Active) -- log ingestion, SPL queries, event correlation |
| **Network Analysis** | Nmap, Wireshark, UFW, TCP/IP |
| **Offensive Tools** | Metasploit, Kali Linux |
| **Frameworks** | NIST CSF, CIS Controls, OWASP, NIS2 |
| **Languages** | Python, Bash, SQL |
| **Platforms** | Linux (Kali, Mint/Ubuntu), Windows |

---

## Contact

- **LinkedIn:** [Joel Massicot](https://www.linkedin.com/in/joel-massicot-07301a2bb/)
- **Location:** Breda, Netherlands (US/EU work authorization)
- **Email:** joel.massicot@zohomail.eu

---

*Building toward Security+ certification and a SOC Analyst or Cybersecurity Operations role in the Netherlands.*
