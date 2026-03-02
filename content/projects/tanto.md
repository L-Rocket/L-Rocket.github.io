---
date: '2026-03-01T14:30:00+08:00'
publishDate: '2026-03-01T14:30:00+08:00'
draft: false
title: 'Tanto'
description: 'A global efficiency tool designed specifically for Windows developers, bringing Vim-like editing philosophy to the global environment.'
tags: ['project', 'productivity', 'vim', 'autohotkey']

---

## Overview

Tanto is a global efficiency tool designed specifically for Windows developers. Built on AutoHotkey v2.0, it brings the core operational logic of Vim into the global environment while enforcing a "One-shot" editing philosophy.

## Core Philosophy

Mode switching should not be a burden. Entering a mode is for completing specific atomic tasks (selecting, copying, deleting). Once the task is triggered, the script immediately and automatically returns to editing mode.

## Key Features

- **Select on Entry (Default Visual Mode)**: Clicking `CapsLock` enters Visual Mode by default, allowing for instant code selection.
- **Native Immersive Cursor Experience**: Different cursor styles for different modes (Crosshair for Visual Mode, Four-way Arrow for Normal Mode).
- **One-shot Action**: All operations automatically release the logic state and return to Insert Mode immediately after execution.
- **Typeout Simulation (With Safety Brake)**: Press `t` in Normal Mode to type out clipboard content character by character.
- **Portable Design**: Icon resources are automatically packed into the EXE, making it a single file you can take anywhere.

## Key Bindings

### Modes & Status
- `CapsLock`: Visual Mode (Default), Crosshair cursor
- `v`: Toggles between Visual and Normal modes
- `Esc`: Force quit navigation and return to Edit Mode

### Basic Movement
- `i` / `k` / `j` / `l`: Up / Down / Left / Right
- `u` / `o`: Home / End
- `h`: High-Impact Select (Selects the entire current line)
- `Ctrl` + `i/k`: Vertical Jump (5 lines)
- `Ctrl` + `j/l`: Horizontal Jump (By Word)

## Installation

**No installation required. Works out of the box.**

1. Go to the [Releases Page](https://github.com/L-Rocket/Tanto/releases)
2. Download the latest `Tanto.exe`
3. Double-click to run (Setting it to run on startup is recommended)

## Links

- Code: https://github.com/L-Rocket/Tanto
- Releases: https://github.com/L-Rocket/Tanto/releases