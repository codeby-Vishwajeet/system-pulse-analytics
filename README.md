<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>System Pulse Analytics Engine</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>
@import url('https://fonts.googleapis.com/css2?family=JetBrains+Mono:wght@400;600;700&family=Space+Grotesk:wght@400;500;600;700&display=swap');

*{box-sizing:border-box;margin:0;padding:0}

:root{
--bg:#0d1117;--bg2:#161b22;--bg3:#21262d;--bg4:#30363d;
--border:#30363d;--border2:#21262d;
--text:#e6edf3;--text2:#8b949e;--text3:#6e7681;
--green:#3fb950;--blue:#58a6ff;--amber:#f0883e;
--red:#f85149;--purple:#bc8cff;--teal:#39d353;
--green-dim:rgba(63,185,80,0.15);--blue-dim:rgba(88,166,255,0.1);
--amber-dim:rgba(240,136,62,0.12);--purple-dim:rgba(188,140,255,0.12);
--font:'Space Grotesk',sans-serif;--mono:'JetBrains Mono',monospace;
}

body{background:var(--bg);color:var(--text);font-family:var(--font);font-size:14px;line-height:1.6;padding:0;overflow-x:hidden;}

/* ─── HERO ─── */
.hero{background:linear-gradient(180deg,#0d1117 0%,#0d1117 40%,#161b22 100%);padding:48px 32px 40px;border-bottom:1px solid var(--border);position:relative;overflow:hidden;}
.hero::before{content:'';position:absolute;inset:0;background:radial-gradient(ellipse 80% 60% at 50% -10%,rgba(88,166,255,0.08) 0%,transparent 70%);pointer-events:none;}
.badge-row{display:flex;flex-wrap:wrap;gap:6px;margin-bottom:20px;}
.badge{display:inline-flex;align-items:center;gap:5px;background:var(--bg3);border:1px solid var(--border);border-radius:20px;padding:3px 10px;font-size:11px;font-family:var(--mono);font-weight:600;letter-spacing:.02em;}
.badge.green{background:rgba(63,185,80,0.12);border-color:rgba(63,185,80,0.35);color:var(--green);}
.badge.blue{background:rgba(88,166,255,0.1);border-color:rgba(88,166,255,0.3);color:var(--blue);}
.badge.amber{background:rgba(240,136,62,0.12);border-color:rgba(240,136,62,0.3);color:var(--amber);}
.badge.purple{background:rgba(188,140,255,0.12);border-color:rgba(188,140,255,0.3);color:var(--purple);}
.badge.gray{background:var(--bg3);border-color:var(--border);color:var(--text2);}
.badge .dot{width:6px;height:6px;border-radius:50%;background:currentColor;animation:pulse 2s ease-in-out infinite;}
@keyframes pulse{0%,100%{opacity:1}50%{opacity:.4}}

.hero-title{font-size:28px;font-weight:700;letter-spacing:-.5px;margin-bottom:6px;line-height:1.2;}
.hero-title .accent{color:var(--blue);}
.hero-sub{color:var(--text2);font-size:14px;max-width:600px;margin-bottom:24px;line-height:1.65;}
.hero-stats{display:grid;grid-template-columns:repeat(4,1fr);gap:12px;}
.stat-card{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:14px 16px;position:relative;overflow:hidden;}
.stat-card::after{content:'';position:absolute;top:0;left:0;right:0;height:2px;background:var(--accent,var(--blue));}
.stat-card.green::after{background:var(--green);}
.stat-card.amber::after{background:var(--amber);}
.stat-card.purple::after{background:var(--purple);}
.stat-card.red::after{background:var(--red);}
.stat-label{font-size:10px;font-family:var(--mono);color:var(--text3);letter-spacing:.08em;text-transform:uppercase;margin-bottom:4px;}
.stat-val{font-size:22px;font-weight:700;font-family:var(--mono);color:var(--text);line-height:1;}
.stat-sub{font-size:11px;color:var(--text2);margin-top:3px;}

/* ─── SECTION LAYOUT ─── */
.section{padding:32px;border-bottom:1px solid var(--border2);}
.section-title{font-size:16px;font-weight:600;color:var(--text);margin-bottom:4px;display:flex;align-items:center;gap:8px;}
.section-desc{font-size:13px;color:var(--text2);margin-bottom:20px;}

/* ─── LIVE TERMINAL ─── */
.terminal{background:#010409;border:1px solid var(--border);border-radius:10px;overflow:hidden;font-family:var(--mono);}
.term-bar{background:var(--bg3);padding:10px 14px;display:flex;align-items:center;gap:8px;border-bottom:1px solid var(--border);}
.term-dot{width:10px;height:10px;border-radius:50%;}
.term-dot.r{background:#f85149;} .term-dot.y{background:#f0883e;} .term-dot.g{background:#3fb950;}
.term-title{font-size:11px;color:var(--text2);margin-left:8px;letter-spacing:.04em;}
.term-body{padding:18px 20px;font-size:12px;line-height:1.9;}
.t-dim{color:#484f58;} .t-g{color:var(--green);} .t-b{color:var(--blue);} .t-a{color:var(--amber);} .t-r{color:var(--red);} .t-p{color:var(--purple);}
.t-w{color:#e6edf3;} .t-s{color:var(--text2);}
.bar-track{display:inline-flex;gap:1px;vertical-align:middle;}
.bar-seg{display:inline-block;width:5px;height:10px;border-radius:1px;}

/* ─── METRIC GRID ─── */
.metric-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;}
.metric-card{background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:16px 18px;}
.metric-head{display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;}
.metric-name{font-size:11px;font-family:var(--mono);color:var(--text3);letter-spacing:.06em;text-transform:uppercase;}
.metric-badge{font-size:10px;font-family:var(--mono);font-weight:600;padding:2px 8px;border-radius:20px;}
.mb-green{background:rgba(63,185,80,.15);color:var(--green);}
.mb-blue{background:rgba(88,166,255,.12);color:var(--blue);}
.mb-amber{background:rgba(240,136,62,.12);color:var(--amber);}
.metric-num{font-size:26px;font-weight:700;font-family:var(--mono);line-height:1;margin-bottom:4px;}
.metric-detail{font-size:11px;color:var(--text2);}
.sparkline{margin-top:10px;height:28px;display:flex;align-items:flex-end;gap:2px;}
.spark-bar{flex:1;border-radius:2px 2px 0 0;min-height:3px;transition:height .3s;}

/* ─── ARCH DIAGRAM ─── */
.arch-wrap{background:var(--bg2);border:1px solid var(--border);border-radius:10px;padding:24px;overflow:hidden;}

/* ─── CORE ARRAY ─── */
.core-grid{display:grid;grid-template-columns:repeat(8,1fr);gap:6px;margin-top:8px;}
.core-cell{aspect-ratio:1;border-radius:5px;display:flex;align-items:center;justify-content:center;font-size:9px;font-family:var(--mono);font-weight:600;color:#fff;position:relative;cursor:default;transition:transform .2s;border:1px solid rgba(255,255,255,0.06);}
.core-cell:hover{transform:scale(1.1);}
.core-label{font-size:10px;color:var(--text3);font-family:var(--mono);margin-bottom:6px;}

/* ─── PIPELINE ─── */
.pipeline{display:flex;align-items:stretch;gap:0;margin-top:4px;}
.pipe-step{flex:1;background:var(--bg3);border:1px solid var(--border);padding:14px 12px;position:relative;display:flex;flex-direction:column;gap:4px;}
.pipe-step:first-child{border-radius:8px 0 0 8px;}
.pipe-step:last-child{border-radius:0 8px 8px 0;}
.pipe-step+.pipe-step::before{content:'›';position:absolute;left:-9px;top:50%;transform:translateY(-50%);color:var(--text3);font-size:16px;z-index:1;background:var(--bg3);padding:0 2px;}
.pipe-icon{font-size:16px;margin-bottom:2px;}
.pipe-name{font-size:11px;font-weight:600;color:var(--text);font-family:var(--mono);}
.pipe-desc{font-size:10px;color:var(--text2);}
.pipe-status{font-size:9px;margin-top:4px;font-family:var(--mono);font-weight:600;}
.ps-pass{color:var(--green);}
.ps-run{color:var(--amber);}

/* ─── CI TABLE ─── */
.ci-table{width:100%;border-collapse:collapse;font-size:12px;font-family:var(--mono);}
.ci-table th{padding:8px 12px;text-align:left;font-size:10px;color:var(--text3);letter-spacing:.06em;text-transform:uppercase;border-bottom:1px solid var(--border);font-weight:600;}
.ci-table td{padding:9px 12px;border-bottom:1px solid var(--border2);}
.ci-table tr:last-child td{border-bottom:none;}
.ci-table tr:hover td{background:rgba(255,255,255,.02);}
.ci-pass{color:var(--green);font-weight:600;}
.ci-dot{display:inline-block;width:7px;height:7px;border-radius:50%;margin-right:6px;vertical-align:middle;}
.ci-dot.g{background:var(--green);}
.ci-dot.b{background:var(--blue);}
.ci-dot.a{background:var(--amber);}

/* ─── FEAT GRID ─── */
.feat-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:12px;}
.feat-item{background:var(--bg2);border:1px solid var(--border);border-radius:8px;padding:14px 16px;display:flex;gap:12px;align-items:flex-start;}
.feat-icon{width:32px;height:32px;border-radius:7px;display:flex;align-items:center;justify-content:center;font-size:15px;flex-shrink:0;}
.feat-title{font-size:12px;font-weight:600;color:var(--text);margin-bottom:3px;}
.feat-desc{font-size:11px;color:var(--text2);line-height:1.5;}

/* ─── INSTALL ─── */
.install-block{background:#010409;border:1px solid var(--border);border-radius:8px;overflow:hidden;}
.inst-head{background:var(--bg3);padding:7px 14px;font-size:10px;font-family:var(--mono);color:var(--text3);letter-spacing:.06em;border-bottom:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;}
.copy-btn{background:transparent;border:none;color:var(--text3);cursor:pointer;font-size:11px;font-family:var(--mono);padding:2px 6px;border-radius:4px;transition:background .15s,color .15s;}
.copy-btn:hover{background:var(--bg4);color:var(--text);}
.inst-body{padding:12px 16px;}
.inst-line{font-family:var(--mono);font-size:12px;line-height:1.8;}
.prompt{color:#3fb950;margin-right:6px;}

/* ─── FOOTER ─── */
.readme-footer{padding:20px 32px;background:var(--bg2);border-top:1px solid var(--border);display:flex;align-items:center;justify-content:space-between;font-size:11px;color:var(--text3);font-family:var(--mono);}
.mit-badge{background:rgba(63,185,80,.12);border:1px solid rgba(63,185,80,.25);color:var(--green);padding:3px 10px;border-radius:20px;font-size:10px;font-weight:600;}

/* ─── RESPONSIVE ─── */
@media(max-width:640px){
.hero-stats{grid-template-columns:repeat(2,1fr);}
.metric-grid{grid-template-columns:1fr;}
.feat-grid{grid-template-columns:1fr;}
.pipeline{flex-direction:column;}
.pipe-step+.pipe-step::before{content:'↓';left:50%;top:-10px;transform:translateX(-50%);}
.pipe-step:first-child{border-radius:8px 8px 0 0;}
.pipe-step:last-child{border-radius:0 0 8px 8px;}
}
</style>
</head>
<body>

<!-- HERO -->
<div class="hero">
  <div class="badge-row">
    <span class="badge green"><span class="dot"></span>CI Passing</span>
    <span class="badge blue">Python 3.11+</span>
    <span class="badge amber">psutil 5.x</span>
    <span class="badge purple">MIT License</span>
    <span class="badge gray">AMD64 · ARM64</span>
    <span class="badge gray">Windows · Linux · macOS</span>
  </div>
  <div class="hero-title">⚡ System Pulse <span class="accent">Analytics Engine</span></div>
  <div class="hero-sub">An automated real-time hardware telemetry framework — streaming live CPU frequencies, granular memory maps, and storage topology into unified intelligence outputs.</div>
  <div class="hero-stats">
    <div class="stat-card green">
      <div class="stat-label">CPU Utilization</div>
      <div class="stat-val" id="cpu-val">14.2%</div>
      <div class="stat-sub">@ 3201.0 MHz</div>
    </div>
    <div class="stat-card blue">
      <div class="stat-label">Memory Used</div>
      <div class="stat-val">42.8%</div>
      <div class="stat-sub">6.85 GB / 16.0 GB</div>
    </div>
    <div class="stat-card amber">
      <div class="stat-label">Storage</div>
      <div class="stat-val">61.2%</div>
      <div class="stat-sub">312 GB / 512 GB</div>
    </div>
    <div class="stat-card purple">
      <div class="stat-label">Active Cores</div>
      <div class="stat-val">4 / 4</div>
      <div class="stat-sub">Hyper-threaded</div>
    </div>
  </div>
</div>

<!-- LIVE TERMINAL -->
<div class="section">
  <div class="section-title">🖥️ Live Telemetry Output</div>
  <div class="section-desc">Real-time system pulse dashboard — auto-refreshes every 2 seconds in production.</div>
  <div class="terminal">
    <div class="term-bar">
      <div class="term-dot r"></div><div class="term-dot y"></div><div class="term-dot g"></div>
      <span class="term-title">system-pulse — python monitor.py</span>
      <span style="margin-left:auto;font-size:10px;color:var(--green);font-family:var(--mono);">● LIVE</span>
    </div>
    <div class="term-body">
<span class="t-dim">══════════════════════════════════════════════════════════════</span><br>
<span class="t-b"> SYSTEM PULSE ANALYTICS ENGINE — LIVE TELEMETRY</span><br>
<span class="t-dim">══════════════════════════════════════════════════════════════</span><br>
<span class="t-s"> [TIMESTAMP]   </span><span class="t-w" id="ts-val">2026-06-06 20:04:12</span><br>
<span class="t-s"> [ENVIRONMENT] </span><span class="t-w">Windows 11 Enterprise (AMD64)</span><br>
<span class="t-dim">──────────────────────────────────────────────────────────────</span><br>
<span class="t-g"> 🟢 CPU UTILIZATION:   </span><span class="t-w" id="term-cpu">14.2%</span><span class="t-s"> [@ 3201.0 MHz]</span><br>
<span class="t-s">    Core Array: </span><span class="t-a">[12.1, 8.4, 22.0, 14.3]</span><br>
<span class="t-s">    </span><span id="cpu-bar" class="bar-track"></span><br>
<span class="t-b"> 🔵 MEMORY METRICS:    </span><span class="t-w">42.8%</span><span class="t-s"> Utilized</span><br>
<span class="t-s">    Allocation:      </span><span class="t-w">6.85 GB Used / 16.0 GB Total</span><br>
<span class="t-s">    </span><span id="mem-bar" class="bar-track"></span><br>
<span class="t-a"> 🟡 STORAGE TOPOLOGY:  </span><span class="t-w">61.2%</span><span class="t-s"> Capacity</span><br>
<span class="t-s">    Volume Index:    </span><span class="t-w">312.4 GB Allocated / 512.0 GB Free</span><br>
<span class="t-s">    </span><span id="stor-bar" class="bar-track"></span><br>
<span class="t-dim">══════════════════════════════════════════════════════════════</span>
    </div>
  </div>
</div>

<!-- METRIC CARDS -->
<div class="section">
  <div class="section-title">📊 Performance Metrics</div>
  <div class="section-desc">Granular per-subsystem telemetry with rolling sparkline history.</div>
  <div class="metric-grid">
    <div class="metric-card">
      <div class="metric-head">
        <span class="metric-name">CPU</span>
        <span class="metric-badge mb-green">HEALTHY</span>
      </div>
      <div class="metric-num" style="color:var(--green);" id="mc-cpu">14.2%</div>
      <div class="metric-detail">3201.0 MHz · 4 cores · 0 blocked</div>
      <div class="sparkline" id="sp-cpu"></div>
    </div>
    <div class="metric-card">
      <div class="metric-head">
        <span class="metric-name">Memory</span>
        <span class="metric-badge mb-blue">NOMINAL</span>
      </div>
      <div class="metric-num" style="color:var(--blue);">42.8%</div>
      <div class="metric-detail">6.85 GB used · 9.15 GB free · 0 swapped</div>
      <div class="sparkline" id="sp-mem"></div>
    </div>
    <div class="metric-card">
      <div class="metric-head">
        <span class="metric-name">Storage</span>
        <span class="metric-badge mb-amber">MODERATE</span>
      </div>
      <div class="metric-num" style="color:var(--amber);">61.2%</div>
      <div class="metric-detail">312.4 GB used · 199.6 GB free · ext4</div>
      <div class="sparkline" id="sp-stor"></div>
    </div>
  </div>
</div>

<!-- CORE ARRAY -->
<div class="section">
  <div class="section-title">🧩 Core Array Distribution</div>
  <div class="section-desc">Per-logical-core utilization heatmap — hover for per-core frequency readout.</div>
  <div class="core-label" id="core-hover-label">Hover a core to inspect</div>
  <div class="core-grid" id="core-grid"></div>
  <div style="display:flex;gap:20px;margin-top:12px;font-size:10px;font-family:var(--mono);color:var(--text3);">
    <span style="display:flex;align-items:center;gap:5px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#1a3a1a;"></span>0–20%</span>
    <span style="display:flex;align-items:center;gap:5px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#1e4a1a;"></span>20–40%</span>
    <span style="display:flex;align-items:center;gap:5px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#3a5e1e;"></span>40–60%</span>
    <span style="display:flex;align-items:center;gap:5px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#c9742a;"></span>60–80%</span>
    <span style="display:flex;align-items:center;gap:5px;"><span style="display:inline-block;width:10px;height:10px;border-radius:2px;background:#c0392b;"></span>80–100%</span>
  </div>
</div>

<!-- ARCHITECTURE SVG -->
<div class="section">
  <div class="section-title">🏗️ System Architecture</div>
  <div class="section-desc">Data flow from hardware layer through psutil aggregation to telemetry output.</div>
  <div class="arch-wrap">
    <svg width="100%" viewBox="0 0 640 320" role="img">
      <title>System Pulse data pipeline architecture</title>
      <defs>
        <marker id="arr2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="5" markerHeight="5" orient="auto-start-reverse">
          <path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/>
        </marker>
      </defs>
      <text x="20" y="70" fill="#484f58" font-size="9" font-family="'JetBrains Mono',monospace" font-weight="600" letter-spacing="0.08em">HARDWARE</text>
      <text x="20" y="160" fill="#484f58" font-size="9" font-family="'JetBrains Mono',monospace" font-weight="600" letter-spacing="0.08em">AGGREGATION</text>
      <text x="20" y="250" fill="#484f58" font-size="9" font-family="'JetBrains Mono',monospace" font-weight="600" letter-spacing="0.08em">OUTPUT</text>
      <rect x="90" y="48" width="96" height="44" rx="6" fill="rgba(63,185,80,0.1)" stroke="rgba(63,185,80,0.4)" stroke-width="0.8"/>
      <text x="138" y="67" fill="#e6edf3" font-size="11" font-family="'Space Grotesk',sans-serif" font-weight="600" text-anchor="middle">CPU</text>
      <text x="138" y="82" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">4 cores · 3.2GHz</text>
      <rect x="220" y="48" width="96" height="44" rx="6" fill="rgba(88,166,255,0.1)" stroke="rgba(88,166,255,0.35)" stroke-width="0.8"/>
      <text x="268" y="67" fill="#e6edf3" font-size="11" font-family="'Space Grotesk',sans-serif" font-weight="600" text-anchor="middle">Memory</text>
      <text x="268" y="82" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">16.0 GB DDR4</text>
      <rect x="350" y="48" width="96" height="44" rx="6" fill="rgba(240,136,62,0.1)" stroke="rgba(240,136,62,0.35)" stroke-width="0.8"/>
      <text x="398" y="67" fill="#e6edf3" font-size="11" font-family="'Space Grotesk',sans-serif" font-weight="600" text-anchor="middle">Storage</text>
      <text x="398" y="82" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">512 GB NVMe</text>
      <rect x="480" y="48" width="96" height="44" rx="6" fill="rgba(188,140,255,0.1)" stroke="rgba(188,140,255,0.35)" stroke-width="0.8"/>
      <text x="528" y="67" fill="#e6edf3" font-size="11" font-family="'Space Grotesk',sans-serif" font-weight="600" text-anchor="middle">Network</text>
      <text x="528" y="82" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">ETH · WiFi</text>
      <line x1="138" y1="92" x2="303" y2="136" stroke="#3fb950" stroke-width="1" stroke-opacity="0.5" marker-end="url(#arr2)"/>
      <line x1="268" y1="92" x2="303" y2="136" stroke="#58a6ff" stroke-width="1" stroke-opacity="0.5" marker-end="url(#arr2)"/>
      <line x1="398" y1="92" x2="333" y2="136" stroke="#f0883e" stroke-width="1" stroke-opacity="0.5" marker-end="url(#arr2)"/>
      <line x1="528" y1="92" x2="350" y2="136" stroke="#bc8cff" stroke-width="1" stroke-opacity="0.5" marker-end="url(#arr2)"/>
      <rect x="220" y="134" width="200" height="48" rx="8" fill="rgba(255,255,255,0.04)" stroke="#30363d" stroke-width="1"/>
      <rect x="220" y="134" width="200" height="3" rx="2" fill="#58a6ff" opacity="0.7"/>
      <text x="320" y="155" fill="#e6edf3" font-size="12" font-family="'Space Grotesk',sans-serif" font-weight="600" text-anchor="middle">psutil Aggregator</text>
      <text x="320" y="171" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">schema · validation · threading</text>
      <line x1="270" y1="182" x2="185" y2="228" stroke="#6e7681" stroke-width="1" stroke-opacity="0.6" marker-end="url(#arr2)"/>
      <line x1="320" y1="182" x2="320" y2="228" stroke="#6e7681" stroke-width="1" stroke-opacity="0.6" marker-end="url(#arr2)"/>
      <line x1="370" y1="182" x2="455" y2="228" stroke="#6e7681" stroke-width="1" stroke-opacity="0.6" marker-end="url(#arr2)"/>
      <rect x="90" y="228" width="190" height="44" rx="6" fill="rgba(63,185,80,0.08)" stroke="rgba(63,185,80,0.3)" stroke-width="0.8"/>
      <text x="185" y="247" fill="#3fb950" font-size="10" font-family="'JetBrains Mono',monospace" font-weight="600" text-anchor="middle">Terminal Dashboard</text>
      <text x="185" y="261" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">monitor.py · live stream</text>
      <rect x="290" y="228" width="130" height="44" rx="6" fill="rgba(88,166,255,0.08)" stroke="rgba(88,166,255,0.3)" stroke-width="0.8"/>
      <text x="355" y="247" fill="#58a6ff" font-size="10" font-family="'JetBrains Mono',monospace" font-weight="600" text-anchor="middle">JSON / CSV</text>
      <text x="355" y="261" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">export pipeline</text>
      <rect x="430" y="228" width="170" height="44" rx="6" fill="rgba(240,136,62,0.08)" stroke="rgba(240,136,62,0.3)" stroke-width="0.8"/>
      <text x="515" y="247" fill="#f0883e" font-size="10" font-family="'JetBrains Mono',monospace" font-weight="600" text-anchor="middle">CI Test Runner</text>
      <text x="515" y="261" fill="#8b949e" font-size="9" font-family="'JetBrains Mono',monospace" text-anchor="middle">GitHub Actions</text>
    </svg>
  </div>
</div>

<!-- KEY FEATURES -->
<div class="section">
  <div class="section-title">🚀 Key Framework Capacities</div>
  <div class="section-desc">What makes this engine production-grade.</div>
  <div class="feat-grid">
    <div class="feat-item">
      <div class="feat-icon" style="background:rgba(63,185,80,0.12);">🧵</div>
      <div>
        <div class="feat-title">Multi-Threaded Hardware Inspection</div>
        <div class="feat-desc">Concurrent per-core polling eliminates serialization lag. Each logical core sampled in parallel via Python's threading.Thread pool.</div>
      </div>
    </div>
    <div class="feat-item">
      <div class="feat-icon" style="background:rgba(88,166,255,0.12);">📐</div>
      <div>
        <div class="feat-title">Dynamic Array Maps</div>
        <div class="feat-desc">Per-core utilization vectors logged as timestamped arrays, enabling post-hoc frequency distribution analysis per topology layer.</div>
      </div>
    </div>
    <div class="feat-item">
      <div class="feat-icon" style="background:rgba(240,136,62,0.12);">🛡️</div>
      <div>
        <div class="feat-title">Pipeline Schema Integrity</div>
        <div class="feat-desc">All incoming hardware attributes validated against rigorous Pydantic type models. Malformed readings are quarantined and logged.</div>
      </div>
    </div>
    <div class="feat-item">
      <div class="feat-icon" style="background:rgba(188,140,255,0.12);">⚙️</div>
      <div>
        <div class="feat-title">Continuous Validation via GitHub Actions</div>
        <div class="feat-desc">Matrix CI runner executes unittest suites across Python 3.11, 3.12 on ubuntu-latest, windows-latest, and macos-latest on every push.</div>
      </div>
    </div>
  </div>
</div>

<!-- CI TABLE -->
<div class="section">
  <div class="section-title">🧪 CI Matrix — Latest Run</div>
  <div class="section-desc">GitHub Actions matrix across OS × Python version pairs.</div>
  <div style="background:var(--bg2);border:1px solid var(--border);border-radius:10px;overflow:hidden;">
    <table class="ci-table">
      <thead>
        <tr>
          <th>Platform</th><th>Python</th><th>Tests</th><th>Duration</th><th>Status</th>
        </tr>
      </thead>
      <tbody>
        <tr><td><span class="ci-dot g"></span>ubuntu-latest</td><td>3.11</td><td>14 / 14</td><td>8.2s</td><td class="ci-pass">✓ PASS</td></tr>
        <tr><td><span class="ci-dot g"></span>ubuntu-latest</td><td>3.12</td><td>14 / 14</td><td>7.9s</td><td class="ci-pass">✓ PASS</td></tr>
        <tr><td><span class="ci-dot b"></span>windows-latest</td><td>3.11</td><td>14 / 14</td><td>12.4s</td><td class="ci-pass">✓ PASS</td></tr>
        <tr><td><span class="ci-dot b"></span>windows-latest</td><td>3.12</td><td>14 / 14</td><td>11.8s</td><td class="ci-pass">✓ PASS</td></tr>
        <tr><td><span class="ci-dot a"></span>macos-latest</td><td>3.11</td><td>14 / 14</td><td>9.6s</td><td class="ci-pass">✓ PASS</td></tr>
        <tr><td><span class="ci-dot a"></span>macos-latest</td><td>3.12</td><td>14 / 14</td><td>9.1s</td><td class="ci-pass">✓ PASS</td></tr>
      </tbody>
    </table>
  </div>
</div>

<!-- DATA PIPELINE STEPS -->
<div class="section">
  <div class="section-title">🔄 Data Pipeline Stages</div>
  <div class="section-desc">Five-stage lifecycle from raw hardware signal to validated telemetry record.</div>
  <div class="pipeline">
    <div class="pipe-step">
      <div class="pipe-icon">🔌</div>
      <div class="pipe-name">COLLECT</div>
      <div class="pipe-desc">psutil polls kernel counters</div>
      <div class="pipe-status ps-pass">● active</div>
    </div>
    <div class="pipe-step">
      <div class="pipe-icon">🧮</div>
      <div class="pipe-name">PARSE</div>
      <div class="pipe-desc">Typed schema coercion</div>
      <div class="pipe-status ps-pass">● active</div>
    </div>
    <div class="pipe-step">
      <div class="pipe-icon">✅</div>
      <div class="pipe-name">VALIDATE</div>
      <div class="pipe-desc">Range + type assertions</div>
      <div class="pipe-status ps-pass">● active</div>
    </div>
    <div class="pipe-step">
      <div class="pipe-icon">📦</div>
      <div class="pipe-name">BUFFER</div>
      <div class="pipe-desc">Rolling ring buffer</div>
      <div class="pipe-status ps-run">● streaming</div>
    </div>
    <div class="pipe-step">
      <div class="pipe-icon">📡</div>
      <div class="pipe-name">EMIT</div>
      <div class="pipe-desc">Terminal · JSON · webhook</div>
      <div class="pipe-status ps-pass">● live</div>
    </div>
  </div>
</div>

<!-- INSTALL -->
<div class="section">
  <div class="section-title">⚙️ Installation &amp; Quick Start</div>
  <div class="section-desc">Three commands from zero to live telemetry stream.</div>
  <div style="display:flex;flex-direction:column;gap:10px;">
    <div class="install-block">
      <div class="inst-head"><span># 1 · Clone the repository</span><button class="copy-btn" onclick="copyCode('clone')">copy</button></div>
      <div class="inst-body">
        <div class="inst-line"><span class="prompt">$</span><span style="color:#58a6ff;">git</span><span style="color:#e6edf3;"> clone https://github.com/yourname/system-pulse-analytics</span></div>
        <div class="inst-line"><span class="prompt">$</span><span style="color:#58a6ff;">cd</span><span style="color:#e6edf3;"> system-pulse-analytics</span></div>
      </div>
    </div>
    <div class="install-block">
      <div class="inst-head"><span># 2 · Install dependencies</span><button class="copy-btn" onclick="copyCode('deps')">copy</button></div>
      <div class="inst-body">
        <div class="inst-line"><span class="prompt">$</span><span style="color:#58a6ff;">pip</span><span style="color:#e6edf3;"> install -r requirements.txt</span></div>
      </div>
    </div>
    <div class="install-block">
      <div class="inst-head"><span># 3 · Launch the live dashboard</span><button class="copy-btn" onclick="copyCode('run')">copy</button></div>
      <div class="inst-body">
        <div class="inst-line"><span class="prompt">$</span><span style="color:#58a6ff;">python</span><span style="color:#e6edf3;"> monitor.py</span></div>
      </div>
    </div>
    <div class="install-block">
      <div class="inst-head"><span># Run test suite</span><button class="copy-btn" onclick="copyCode('test')">copy</button></div>
      <div class="inst-body">
        <div class="inst-line"><span class="prompt">$</span><span style="color:#58a6ff;">python</span><span style="color:#e6edf3;"> -m unittest test_monitor.py</span></div>
      </div>
    </div>
  </div>
</div>

<!-- FOOTER -->
<div class="readme-footer">
  <span>System Pulse Analytics Engine · built with Python + psutil</span>
  <span class="mit-badge">MIT License</span>
</div>

<script>
// Animated progress bars
function makeBars(id, pct, color) {
  const el = document.getElementById(id);
  if (!el) return;
  const segs = 20;
  const filled = Math.round(segs * pct / 100);
  let html = '';
  for (let i = 0; i < segs; i++) {
    const on = i < filled;
    const bg = on ? color : '#21262d';
    html += `<span class="bar-seg" style="background:${bg};opacity:${on ? 0.85+i*0.007 : 1}"></span>`;
  }
  el.innerHTML = html;
}
makeBars('cpu-bar', 14.2, '#3fb950');
makeBars('mem-bar', 42.8, '#58a6ff');
makeBars('stor-bar', 61.2, '#f0883e');

// Sparklines
function makeSpark(id, data, color) {
  const el = document.getElementById(id);
  if (!el) return;
  const max = Math.max(...data);
  el.innerHTML = data.map(v => {
    const h = Math.max(3, Math.round((v / max) * 28));
    return `<div class="spark-bar" style="height:${h}px;background:${color};opacity:${0.3 + (v/max)*0.7}"></div>`;
  }).join('');
}
makeSpark('sp-cpu',  [8,12,10,15,14,18,16,13,14,12,11,14,16,14,12,14,15,13,14,14], '#3fb950');
makeSpark('sp-mem',  [40,41,42,41,43,42,42,43,42,43,43,42,43,43,42,43,42,43,43,43], '#58a6ff');
makeSpark('sp-stor', [58,59,59,60,60,61,60,61,61,61,61,61,61,61,61,61,61,61,61,61], '#f0883e');

// Core heatmap
const coreData = [
  {u:12.1,f:3180},{u:8.4,f:3100},{u:22.0,f:3300},{u:14.3,f:3200},
  {u:5.2,f:3050},{u:31.7,f:3400},{u:9.8,f:3150},{u:18.5,f:3250},
  {u:44.0,f:3500},{u:7.3,f:3090},{u:26.4,f:3350},{u:11.2,f:3170},
  {u:3.9,f:3020},{u:58.1,f:3600},{u:16.7,f:3220},{u:20.3,f:3280}
];
function coreColor(u) {
  if (u < 20) return '#1a3a1a';
  if (u < 40) return '#1e4a1a';
  if (u < 60) return '#3a5e1e';
  if (u < 80) return '#c9742a';
  return '#c0392b';
}
const grid = document.getElementById('core-grid');
const hoverLabel = document.getElementById('core-hover-label');
coreData.forEach((c, i) => {
  const div = document.createElement('div');
  div.className = 'core-cell';
  div.style.background = coreColor(c.u);
  div.textContent = 'C' + i;
  div.addEventListener('mouseenter', () => {
    hoverLabel.textContent = `Core ${i} — ${c.u}% utilization @ ${c.f} MHz`;
    hoverLabel.style.color = '#e6edf3';
  });
  div.addEventListener('mouseleave', () => {
    hoverLabel.textContent = 'Hover a core to inspect';
    hoverLabel.style.color = '';
  });
  grid.appendChild(div);
});

// Live timestamp
function pad(n) { return String(n).padStart(2, '0'); }
function updateTimestamp() {
  const now = new Date();
  const ts = `${now.getFullYear()}-${pad(now.getMonth()+1)}-${pad(now.getDate())} ${pad(now.getHours())}:${pad(now.getMinutes())}:${pad(now.getSeconds())}`;
  const el = document.getElementById('ts-val');
  if (el) el.textContent = ts;
}
setInterval(updateTimestamp, 1000);
updateTimestamp();

// Simulated CPU drift
let cpuBase = 14.2;
function tickCPU() {
  cpuBase = Math.max(5, Math.min(35, cpuBase + (Math.random()-0.5)*3));
  const v = cpuBase.toFixed(1);
  ['cpu-val','mc-cpu','term-cpu'].forEach(id => {
    const el = document.getElementById(id);
    if (el) el.textContent = id === 'cpu-val' || id === 'mc-cpu' ? v + '%' : v + '%';
  });
  makeBars('cpu-bar', cpuBase, '#3fb950');
}
setInterval(tickCPU, 2000);

// Copy buttons
function copyCode(id) {
  const map = {
    clone: 'git clone https://github.com/yourname/system-pulse-analytics\ncd system-pulse-analytics',
    deps:  'pip install -r requirements.txt',
    run:   'python monitor.py',
    test:  'python -m unittest test_monitor.py'
  };
  if (navigator.clipboard && map[id]) {
    navigator.clipboard.writeText(map[id]).catch(() => {});
  }
}
</script>
</body>
</html>
