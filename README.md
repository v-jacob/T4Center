# T4Center

PySide6 desktop application for monitoring and controlling a dual-Teensy USB controller bridge [T4Nexus]

## Features
- **Gamepad Telemetry** — Real-time visualization of controller state read from the DevMon HID interface
- **CV Script Manager** — Browse, select, and launch Python computer vision scripts that send gamepad inputs to Teensy B via RawHID
- **CV Preview** — Live video feed from the running CV script displayed inside the app
- **Serial Monitor** — Debug output from Teensy A (forwarded through Teensy B via UART)

## USB Hardware
Targets a **Teensy 4.1** (Teensy B) running the T4Nexus firmware:

| Interface | Name   | Usage Page | Packet Size | Direction       |
|-----------|--------|------------|-------------|-----------------|
| 0         | RawHID | `0xFFAB`   | 1024 bytes  | Bidirectional   |
| 1         | SerEmu | `0xFFC9`   | 64/32 bytes | Bidirectional   |
| 2         | DevMon | `0xFFAC`   | 64 bytes    | Teensy → PC     |

VID `0x16C0` / PID `0x0486` (Teensyduino RawHID), High-speed USB (480 Mbit/s).

## Requirements
- Python 3.10+
- Windows (primary target)

## Setup
```bash
pip install PySide6 hidapi opencv-python
```

## Usage
```bash
python main.py
```

## Packaging
```bash
pyinstaller --onefile --windowed main.py
```

## Tech Stack

| Library | Purpose |
|---------|---------|
| PySide6 | Qt6 GUI framework |
| hidapi  | USB HID communication with Teensy B |
| OpenCV  | CV preview frame display |
| PyInstaller | Standalone `.exe` packaging |

## Architecture
- **QThread + signals** for HID reading and CV preview (never blocks the main thread)
- **QProcess** to launch CV scripts as separate processes with their own Python interpreter and HID handle
- USB protocol constants (VID, PID, usage pages, packet offsets) centralized in a single config module
