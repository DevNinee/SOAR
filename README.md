# SOAR
# SOAR de Dispositivos de Rede Local

![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![Scapy](https://img.shields.io/badge/Scapy-2.5.0-red.svg)
![SQLite](https://img.shields.io/badge/SQLite-3-green.svg)
![Status](https://img.shields.io/badge/Status-MVP%20Funcional-brightgreen.svg)

> **Monitore quem está na sua rede. Detecte intrusos. Proteja seu perímetro.**

---

## O que é?

O SOAR é uma ferramenta de **monitoramento de rede local** que escaneia dispositivos conectados, compara com uma lista de autorizados e gera alertas quando encontra algo novo. É o primeiro passo para montar um **SIEM caseiro** (Sistema de Gerenciamento de Eventos de Segurança).

---

## Por que isso existe?

| Problema | Solução do Guardião |
|:---|:---|
| Não sei quem está no meu Wi‑Fi | Lista todos os IPs, MACs e fabricantes |
| Dispositivos estranhos passam despercebidos | Compara com whitelist e emite alertas |
| Não tenho histórico de conexões | Registra tudo em banco SQLite |
| Quero aprender cyber na prática | Projeto real com ARP, TCP, whitelist, logs |

---

## Tecnologias

| Tecnologia | Para que serve? |
|:---|:---|
| **Python 3.8+** | Linguagem principal |
| **Scapy** | Manipulação de pacotes de rede (ARP Scan) |
| **Socket** | Verificação de portas abertas |
| **SQLite** | Banco de dados local para histórico |
| **JSON** | Armazenamento da lista branca |
| **Streamlit** (futuro) | Painel visual interativo |

---

## Estrutura do Projeto

soar-network-monitor/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── docs/
│   ├── arquitetura.md
│   ├── roadmap.md
│   ├── aprendizados/
│
├── src/
│   ├── scanner/
│   ├── database/
│   ├── alerts/
│   ├── network/
│   ├── utils/
│   ├── config/
│   └── main.py
│
├── data/
│   ├── database.db
│   └── whitelist.json
│
├── tests/
│
└── logs/
