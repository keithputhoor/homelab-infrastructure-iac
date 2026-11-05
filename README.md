# Homelab Infrastructure, Self-Hosting & Automation (IaC)

![Proxmox VE](https://img.shields.io/badge/Proxmox_VE-Hypervisor-e57000?style=flat-square)
![Docker Compose](https://img.shields.io/badge/Docker-Compose-2496ed?style=flat-square)
![Cloudflare Zero Trust](https://img.shields.io/badge/Cloudflare-Zero_Trust-f38020?style=flat-square)
![Ollama](https://img.shields.io/badge/Ollama-GTX_1650_Ti_Mobile-76b900?style=flat-square)
![Home Assistant](https://img.shields.io/badge/Home_Assistant-Zigbee2MQTT-41bdf5?style=flat-square)

Infrastructure-as-Code (IaC) configurations, Proxmox LXC hardware passthrough setups, multi-drive storage pools, Docker Compose stacks, smart home automations, and engineering runbooks for my self-hosted **Proxmox VE** homelab and Python projects.

---

## Projects Included

| Directory | Stack | Summary |
| :--- | :--- | :--- |
| [**`proxmox-media-stack/`**](./proxmox-media-stack/) | Proxmox VE, Debian, MergerFS, Docker Compose, Cloudflare Zero Trust | Containerized self-hosted media streaming, `.srt` subtitle synchronization (`Bazarr`), digital document library (`Jellyfin`, `Jellyseerr`, `Kavita`), and `n8n` automation backed by a 2-HDD (`Drive 1` 1TB + `Drive 2` 4TB) `MergerFS` storage pool (`/mnt/storage`) and zero-port-forward Cloudflare Access tunnels. |
| [**`local-ai-inference/`**](./local-ai-inference/) | Proxmox VE, NVIDIA GeForce GTX 1650 Ti Mobile, LXC Passthrough, Ollama, Open WebUI | GPU-accelerated local LLM server with Proxmox host/LXC `/dev/nvidia*` (`c 195:*`) and `/dev/nvidia-uvm` (`c 508:*`) passthrough (`--no-kernel-module`) serving Open WebUI and REST APIs for n8n SOC alert triage. |
| [**`smart-home-zigbee/`**](./smart-home-zigbee/) | Home Assistant, Zigbee2MQTT, Mosquitto MQTT, Sonoff SLZB-06p7 PoE | Local Zigbee 3.0 mesh on Channel 20 (`20 dBm`) using an SLZB-06p7 LAN coordinator (`tcp://...:6638`) and mains-powered micro-relay routers, correlating Hobeian ZG-102ZM vibration sensors with mmWave human presence sensors. |
| [**`restaurant-analytics-cli/`**](./restaurant-analytics-cli/) | Python 3, CSV I/O, Pandas, Matplotlib | Foundational Python CLI menu ordering and dish summary tool using CSV storage (`newline=""`, `dropna()`) and Matplotlib pie charts. |
