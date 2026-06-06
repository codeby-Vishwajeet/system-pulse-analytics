<div align="center">

# ⚡ System Pulse Analytics Engine

**An automated data pipeline and real-time core system resource intelligence framework**  
built to capture multi-threaded hardware tracking information.

<br>

![CI Passing](https://img.shields.io/badge/CI-Passing-3fb950?style=for-the-badge&logo=github-actions&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11%2B-58a6ff?style=for-the-badge&logo=python&logoColor=white)
![psutil](https://img.shields.io/badge/psutil-5.x-f0883e?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-bc8cff?style=for-the-badge)
![Platform](https://img.shields.io/badge/Platform-Windows%20%7C%20Linux%20%7C%20macOS-30363d?style=for-the-badge)
![Arch](https://img.shields.io/badge/Arch-AMD64%20%7C%20ARM64-30363d?style=for-the-badge)

<br>

</div>

---

## 🖥️ Terminal Preview

```
╔══════════════════════════════════════════════════════════════╗
║       SYSTEM PULSE ANALYTICS ENGINE — LIVE TELEMETRY        ║
╠══════════════════════════════════════════════════════════════╣
║  [TIMESTAMP]    2026-06-06 20:04:12                          ║
║  [ENVIRONMENT]  Windows 11 Enterprise (AMD64)                ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  🟢 CPU UTILIZATION   14.2%  [@  3201.0 MHz]                 ║
║     Core Array:  [12.1, 8.4, 22.0, 14.3]                    ║
║     ████████░░░░░░░░░░░░░░░░░░  14%                          ║
║                                                              ║
║  🔵 MEMORY METRICS    42.8%  Utilized                        ║
║     Allocation:  6.85 GB Used / 16.0 GB Total                ║
║     ████████████████░░░░░░░░░░  42%                          ║
║                                                              ║
║  🟡 STORAGE TOPOLOGY  61.2%  Capacity Reached                ║
║     Volume Index: 312.4 GB Allocated / 512.0 GB Free         ║
║     ████████████████████████░░  61%                          ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
```

---

## 📊 Live Metrics Snapshot

| Subsystem | Metric | Value | Status |
|-----------|--------|-------|--------|
| 🟢 **CPU** | Utilization | `14.2%` @ 3201.0 MHz | ![](https://img.shields.io/badge/-HEALTHY-3fb950?style=flat-square) |
| 🔵 **Memory** | Heap Usage | `6.85 GB` / 16.0 GB | ![](https://img.shields.io/badge/-NOMINAL-58a6ff?style=flat-square) |
| 🟡 **Storage** | Disk Fill | `312.4 GB` / 512.0 GB | ![](https://img.shields.io/badge/-MODERATE-f0883e?style=flat-square) |
| 🟣 **Cores** | Active | `4 / 4` logical cores | ![](https://img.shields.io/badge/-ONLINE-bc8cff?style=flat-square) |

---

## 🏗️ System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                    HARDWARE LAYER                        │
│                                                          │
│  ┌──────────┐  ┌──────────┐  ┌──────────┐  ┌────────┐  │
│  │   CPU    │  │  Memory  │  │ Storage  │  │  Net   │  │
│  │4c·3.2GHz │  │16GB DDR4 │  │512GB NVM │  │ETH·WiF │  │
│  └────┬─────┘  └────┬─────┘  └────┬─────┘  └───┬────┘  │
└───────┼──────────────┼──────────────┼─────────────┼──────┘
        │              │              │             │
        └──────────────┴──────┬───────┴─────────────┘
                               │
                    ┌──────────▼──────────┐
                    │   psutil Aggregator  │
                    │  schema · validate  │
                    │     threading       │
                    └──────────┬──────────┘
                               │
             ┌─────────────────┼──────────────────┐
             │                 │                  │
    ┌────────▼───────┐  ┌──────▼──────┐  ┌───────▼───────┐
    │    Terminal    │  │  JSON / CSV │  │  CI Runner    │
    │   Dashboard   │  │   Export    │  │  GH Actions   │
    │  monitor.py   │  │  pipeline   │  │  test_monitor │
    └────────────────┘  └─────────────┘  └───────────────┘
```

---

## 🔄 Data Pipeline

```
  ┌─────────┐     ┌─────────┐     ┌──────────┐     ┌─────────┐     ┌────────┐
  │ COLLECT │ ──▶ │  PARSE  │ ──▶ │ VALIDATE │ ──▶ │  BUFFER │ ──▶ │  EMIT  │
  │         │     │         │     │          │     │         │     │        │
  │ psutil  │     │  typed  │     │  range   │     │  ring   │     │  term  │
  │  polls  │     │ schema  │     │  assert  │     │ buffer  │     │  json  │
  │ kernel  │     │ coerce  │     │  type    │     │ stream  │     │  hook  │
  └─────────┘     └─────────┘     └──────────┘     └─────────┘     └────────┘
  ● active        ● active        ● active          ● streaming     ● live
```

---

## 🧩 Core Array Distribution (Example)

```
  Core Utilization Heatmap — 16 Logical Cores
  ┌──────────────────────────────────────────┐
  │                                          │
  │  C0   C1   C2   C3   C4   C5   C6   C7  │
  │ [12] [ 8] [22] [14] [ 5] [32] [10] [19] │
  │  ░░   ░    ▒▒   ░░   ░    ▓▓   ░    ▒   │
  │                                          │
  │  C8   C9  C10  C11  C12  C13  C14  C15  │
  │ [44] [ 7] [26] [11] [ 4] [58] [17] [20] │
  │  ▓▓   ░    ▒▒   ░    ░    ██   ▒    ▒   │
  │                                          │
  │  Legend:  ░ 0-20%  ▒ 20-40%  ▓ 40-60%  ██ 60%+  │
  └──────────────────────────────────────────┘
```

---

## 🚀 Key Framework Capacities

<table>
<tr>
<td width="50%">

### 🧵 Multi-Threaded Hardware Inspection
Concurrent per-core polling eliminates serialization lag. Each logical core sampled in parallel via Python's `threading.Thread` pool for zero-wait telemetry capture.

</td>
<td width="50%">

### 📐 Dynamic Array Maps
Per-core utilization vectors logged as timestamped arrays, enabling post-hoc frequency distribution analysis across the full processor topology.

</td>
</tr>
<tr>
<td width="50%">

### 🛡️ Pipeline Schema Integrity
All incoming hardware attributes validated against rigorous Pydantic type models. Malformed sensor readings are quarantined and flagged before emission.

</td>
<td width="50%">

### ⚙️ Continuous Validation
Matrix CI runner executes full `unittest` suites across Python 3.11 and 3.12 on `ubuntu-latest`, `windows-latest`, and `macos-latest` on every push.

</td>
</tr>
</table>

---

## 🧪 CI Matrix

| Platform | Python | Tests | Duration | Result |
|----------|--------|-------|----------|--------|
| ![ubuntu](https://img.shields.io/badge/ubuntu-latest-3fb950?style=flat-square&logo=ubuntu&logoColor=white) | 3.11 | 14 / 14 | 8.2s | ✅ PASS |
| ![ubuntu](https://img.shields.io/badge/ubuntu-latest-3fb950?style=flat-square&logo=ubuntu&logoColor=white) | 3.12 | 14 / 14 | 7.9s | ✅ PASS |
| ![windows](https://img.shields.io/badge/windows-latest-58a6ff?style=flat-square&logo=windows&logoColor=white) | 3.11 | 14 / 14 | 12.4s | ✅ PASS |
| ![windows](https://img.shields.io/badge/windows-latest-58a6ff?style=flat-square&logo=windows&logoColor=white) | 3.12 | 14 / 14 | 11.8s | ✅ PASS |
| ![macos](https://img.shields.io/badge/macos-latest-f0883e?style=flat-square&logo=apple&logoColor=white) | 3.11 | 14 / 14 | 9.6s | ✅ PASS |
| ![macos](https://img.shields.io/badge/macos-latest-f0883e?style=flat-square&logo=apple&logoColor=white) | 3.12 | 14 / 14 | 9.1s | ✅ PASS |

---

## ⚙️ Core Architecture Stack

| Layer | Technology | Role |
|-------|-----------|------|
| ![Python](https://img.shields.io/badge/Python-3.11%2B-58a6ff?style=flat-square&logo=python&logoColor=white) | **Core Runtime** | Orchestration, threading, schema |
| ![psutil](https://img.shields.io/badge/psutil-5.x-f0883e?style=flat-square&logo=python&logoColor=white) | **Telemetry Aggregator** | Hardware counter polling |
| ![GHA](https://img.shields.io/badge/GitHub_Actions-Matrix_Runner-3fb950?style=flat-square&logo=github-actions&logoColor=white) | **CI Engine** | Cross-platform test matrix |
| ![unittest](https://img.shields.io/badge/unittest-Assertions-bc8cff?style=flat-square&logo=python&logoColor=white) | **Test Framework** | Schema + value validation |

---

## 🔧 Installation & Execution

### 1. Clone the Repository

```bash
git clone https://github.com/yourname/system-pulse-analytics
cd system-pulse-analytics
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

**`requirements.txt`**
```
psutil>=5.9.0
pydantic>=2.0.0
```

### 3. Launch the Intelligence Interface

```bash
python monitor.py
```

### 4. Run the Test Suite

```bash
python -m unittest test_monitor.py
```

Expected output:
```
......................................................
----------------------------------------------------------------------
Ran 14 tests in 0.042s

OK
```

---

## 📁 Project Structure

```
system-pulse-analytics/
│
├── monitor.py            ← Main telemetry engine entry point
├── test_monitor.py       ← Unittest assertions for all pipeline stages
├── requirements.txt      ← psutil + pydantic dependencies
│
├── core/
│   ├── collector.py      ← Multi-threaded hardware polling
│   ├── schema.py         ← Pydantic type models & validation
│   ├── pipeline.py       ← Collect → Parse → Validate → Buffer → Emit
│   └── formatter.py      ← Terminal dashboard renderer
│
├── .github/
│   └── workflows/
│       └── ci.yml        ← GitHub Actions matrix runner
│
└── README.md
```

---

## 📄 License

Distributed under the **MIT License**. See [`LICENSE`](./LICENSE) for full legal deployment authorization.

---

<div align="center">

**System Pulse Analytics Engine** · Built with Python + psutil

![](https://img.shields.io/badge/Made%20with-Python-58a6ff?style=for-the-badge&logo=python&logoColor=white)
![](https://img.shields.io/badge/Telemetry-Real--Time-3fb950?style=for-the-badge)
![](https://img.shields.io/badge/License-MIT-bc8cff?style=for-the-badge)

</div>
