# System Information and Network Adapter List Script
[![YouTube Video Thumbnail](https://img.youtube.com/vi/S-bTmTY8ceU/0.jpg)](https://youtu.be/S-bTmTY8ceU)


This Python script fetches system information such as user names, private IP, public IP, OS version, SSH version, and network adapter list, and presents it in a visually appealing format.

## Disclaimer | Running the Script

**Author:** Lalatendu Swain | [GitHub](https://github.com/Lalatenduswain) | [Website](https://blog.lalatendu.info/)

This script is provided as-is and may require modifications or updates based on your specific environment and requirements. Use it at your own risk. The authors of the script are not liable for any damages or issues caused by its usage.

## Donations

If you find this script useful and want to show your appreciation, you can donate via [Buy Me a Coffee](https://www.buymeacoffee.com/lalatendu.swain).

## Usage

1. Clone this repository:

```bash
git clone https://github.com/Lalatenduswain/System-Info-Network-Adapter-Script
```

2. Navigate to the directory:

```bash
cd System-Info-Network-Adapter-Script
```

3. Run the script:

```bash
python3 system_info_network_adapter.py
```

## Requirements

- Python 3
- `psutil` library (install via `pip install psutil`)
- `rich` library (install via `pip install rich`)

## Script Output

The script provides the following information:

- User Names
- Private IP
- Public IP
- OS Version
- SSH Version
- Network Adapter List

## Example Output

```
System Information
┌────────────┬────────────────────────────────────────────────────────────┐
│  Category  │                      Information                           │
├────────────┼────────────────────────────────────────────────────────────┤
│ User Names │ root, daemon, bin, sys, sync, games, man, lp, mail, news, │
│            │  uucp, proxy, www-data, backup, list, irc, gnats, nobody, │
│            │    systemd-network, systemd-resolve, messagebus, ...       │
├────────────┼────────────────────────────────────────────────────────────┤
│ Private IP │                       192.168.1.10                           │
├────────────┼────────────────────────────────────────────────────────────┤
│ Public IP  │                      203.0.113.10                            │
├────────────┼────────────────────────────────────────────────────────────┤
│ OS Version │    Linux-5.4.0-84-generic-x86_64-with-glibc2.27              │
├────────────┼────────────────────────────────────────────────────────────┤
│ SSH Version│       OpenSSH_8.2p1 Ubuntu-4ubuntu0.3, OpenSSL 1.1.1f      │
└────────────┴────────────────────────────────────────────────────────────┘

Network Adapter List
Adapter: lo
  Family: AF_INET, Address: 127.0.0.1
  Family: AF_INET6, Address: ::1

Adapter: enp0s3
  Family: AF_PACKET, Address: 08:00:27:17:72:fa

Adapter: wlp0s8
  Family: AF_PACKET, Address: 00:24:17:d8:18:30
  Family: AF_INET, Address: 192.168.1.10
  Family: AF_INET6, Address: fe80::dd7d:4c1d:ce8c:8d3d%wlp0s8
