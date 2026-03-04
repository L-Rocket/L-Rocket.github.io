---
date: '2026-03-01T16:30:00+08:00'
publishDate: '2026-03-01T16:30:00+08:00'
draft: false
title: 'nanoCache'
description: 'A high-performance in-memory key-value store implemented in both C++17 and Go for comparative study.'
tags: ['project', 'c++', 'go', 'performance', 'cache']
lastmod: '2026-03-04T10:40:00+08:00'

---

## Overview

nanoCache is a sharded, thread-safe in-memory key-value store. This project serves as a **comparative study between Modern C++ (C++17) and Go**, implementing the same architectural design to explore the differences in concurrency models, memory management, and locking strategies. It ships with aligned benchmark workflows, CI smoke checks for both language implementations, and bilingual documentation for reproducible C++/Go comparisons.

## Architecture

To minimize lock contention in high-concurrency scenarios, nanoCache uses a **Sharding Strategy** (similar to BigCache or FreeCache):

- **Sharding:** The keyspace is divided into 256 shards based on FNV-1a hashing.
- **Locking:** Each shard has its own independent `RWMutex` (Go) or `std::shared_mutex` (C++).
- **Eviction:** Support for TTL (Time-To-Live) with both lazy deletion and background cleanup (Janitor).

## Project Structure

- **[`cpp-impl/`](./cpp-impl)**: The baseline implementation using C++17. Focuses on manual memory management using `std::shared_ptr` and `std::shared_mutex`.
- **`go-iml/`**: The Go implementation using goroutines and the Go runtime scheduler.

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
cd go-iml
go mod tidy
go run cmd/server/main.go
```

## Performance Benchmark (Local Baseline)

Benchmark baseline from the latest local run on 2026-03-04 (Apple M4, macOS/darwin arm64).

Method:

- Aligned concurrency: `GOMAXPROCS=10` (Go) and `--threads 10` (C++)
- Aligned hot path: benchmark keys are precomputed before timing in both implementations
- Go command: `go test ./go-iml/cache -run '^$' -bench 'BenchmarkCache(Set|Get|ConcurrentSetGet)$' -benchmem -count=3`
- C++ command: `./cpp-impl/build/benchmark_sharded_cache --ops 300000 --threads 10` (3 runs averaged)

| Scenario | C++ (ops/s) | Go (ops/s) | Faster |
| :--- | :--- | :--- | :--- |
| Set | `10,195,253` | `3,686,323` | `C++ ~2.74x` |
| Get | `16,019,100` | `6,123,709` | `C++ ~2.62x` |
| Concurrent Set+Get | `27,554,267` | `5,154,838` | `C++ ~5.35x` |

Run local comparison from repository root:

```bash
./scripts/compare_cpp_go_perf.sh
```

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
