---
date: '2026-03-01T16:30:00+08:00'
publishDate: '2026-03-01T16:30:00+08:00'
draft: false
title: 'nanoCache'
description: 'A high-performance in-memory key-value store implemented in both C++17 and Go for comparative study.'
tags: ['project', 'c++', 'go', 'performance', 'cache']

---

## Overview

nanoCache is a sharded, thread-safe in-memory key-value store. This project serves as a **comparative study between Modern C++ (C++17) and Go**, implementing the same architectural design to explore the differences in concurrency models, memory management, and locking strategies.

## Architecture

To minimize lock contention in high-concurrency scenarios, nanoCache uses a **Sharding Strategy** (similar to BigCache or FreeCache):

- **Sharding:** The keyspace is divided into 256 shards based on FNV-1a hashing.
- **Locking:** Each shard has its own independent `RWMutex` (Go) or `std::shared_mutex` (C++).
- **Eviction:** Support for TTL (Time-To-Live) with both lazy deletion and background cleanup (Janitor).

## Project Structure

- **[`cpp-impl/`](./cpp-impl)**: The baseline implementation using C++17. Focuses on manual memory management using `std::shared_ptr` and `std::shared_mutex`.
- **[`go-impl/`](./go-impl)**: The target implementation using Go. Focuses on Goroutines, Channels, and the Go runtime scheduler.

## Getting Started

### C++ Implementation

Requirements: CMake >= 3.10, C++17 compliant compiler (GCC/Clang/MSVC).

```bash
cd cpp-impl
mkdir build && cd build
cmake ..
make
./nano_cache_cpp
```

### Go Implementation

Requirements: Go >= 1.20.

```bash
cd go-impl
go mod tidy
go run cmd/server/main.go
```

## Performance Benchmark

*Creating a baseline comparison between the two implementations.*

| Metric | C++ Implementation | Go Implementation |
| :--- | :--- | :--- |
| **Throughput (OPS)** | *TBD* | *TBD* |
| **Memory Footprint** | *TBD* | *TBD* |
| **Lock Contention** | *High/Low* | *High/Low* |

> *Benchmarks will be run on [Your CPU Specs] with 100 concurrent workers and 1M keys.*

## Key Learnings (The Migration Journey)

*This section documents the transition from C++ to Go.*

1.  **Memory Model:** Moving from `std::shared_ptr` semantics to Go's Garbage Collector.
2.  **Concurrency:** Comparing `std::thread` overhead vs. Goroutine context switching cost.
3.  **Code Complexity:** Lines of code required to implement the sharded map logic.

## License

MIT

## Links

- Code: https://github.com/L-Rocket/nanoCache
- Documentation: https://github.com/L-Rocket/nanoCache/blob/main/README.md