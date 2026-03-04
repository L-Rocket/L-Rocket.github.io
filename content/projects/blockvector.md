---
date: '2026-03-01T15:00:00+08:00'
publishDate: '2026-03-01T15:00:00+08:00'
draft: false
title: 'BlockVector'
description: 'A high-performance, header-only C++17 container designed to solve specific limitations of std::vector.'
tags: ['project', 'c++', 'performance', 'container']
lastmod: '2026-03-04T10:40:00+08:00'
---

## Overview

BlockVector is a high-performance, header-only C++17 container designed to solve specific limitations of `std::vector`. It addresses common issues like pointer invalidation, expensive reallocation, and memory peaks through its innovative chunked storage architecture. The project documentation includes local benchmark comparisons and dedicated pointer-stability tests to make tradeoffs explicit for real workloads.

## Why BlockVector?

While `std::vector` is the default choice for dynamic arrays, it has significant drawbacks in certain scenarios:

1. **Pointer Invalidation**: When `std::vector` grows, it reallocates memory and moves all elements to a new location, invalidating all existing pointers, references, and iterators.

2. **Expensive Reallocation**: For large objects or objects with expensive constructors, copying or moving them during expansion causes severe performance spikes.

3. **Memory Peaks**: The doubling expansion strategy can cause temporary memory usage to double, potentially leading to OOM errors with massive datasets.

## Core Features

BlockVector solves these problems with its "Chunked Storage" approach:

- **Pointer Stability**: Guaranteed pointer/reference validity for the entire lifetime of the container. Pointers to elements never break when you `push_back`.

- **Zero-Copy Growth**: Expansion only involves allocating a new fixed-size block. No old elements are ever moved or copied.

- **Predictable Memory**: Incremental allocation leads to a smoother memory usage curve.

- **O(1) Random Access**: Fast `operator[]` access just like `std::vector`.

- **Standard Compliant**: Full `RandomAccessIterator` support, compatible with `std::sort`, `std::lower_bound`.

- **Modern C++**: Supports Initializer Lists (`{1, 2, 3}`) and in-place construction via `emplace_back`.

## Architecture

BlockVector combines the best features of `std::vector` and object pools:

| Feature | std::vector | Object Pool | BlockVector |
| :--- | :---: | :---: | :---: |
| Interface | Friendly (STL) | Manual Alloc/Free | **Friendly (STL)** |
| Growth Strategy | Reallocate & Move | Chunks / Blocks | **Chunks / Blocks** |
| Pointer Stability | ❌ No | ✅ Yes | **✅ Yes** |
| Random Access | ✅ O(1) | ❌ Typically No | **✅ O(1)** |
| Cache Locality | ⭐⭐⭐ Best | ⭐⭐ Good | **⭐⭐ Good** |

It encapsulates the complex memory management of a pool (chunking, expansion, addressing) behind a familiar, easy-to-use vector interface.

## Installation

### Method 1: CMake FetchContent (Recommended)

Add this to your `CMakeLists.txt`:

```cmake
include(FetchContent)
FetchContent_Declare(
    BlockVector
    GIT_REPOSITORY https://github.com/L-Rocket/BlockVector.git
    GIT_TAG main 
)
FetchContent_MakeAvailable(BlockVector)

# Link to your target
target_link_libraries(YourApp PRIVATE BlockVector)
```

### Method 2: Copy Header (Simple)

Download the latest stable version directly from GitHub Releases:

```bash
# Using curl
curl -L -O https://github.com/L-Rocket/BlockVector/releases/latest/download/BlockVector.hpp

# Using wget
wget https://github.com/L-Rocket/BlockVector/releases/latest/download/BlockVector.hpp
```

## Quick Start

```cpp
#include <iostream>
#include <algorithm>
#include "BlockVector.hpp"

struct Point { int x, y; Point(int a, int b): x(a), y(b){} };

int main() {
    // 1. Initialization
    BlockVector<int> bv = {10, 5, 20};
    
    // 2. Pointer Stability Demo
    int& ref = bv[0]; // Reference to the first element (10)
    
    // Add thousands of elements to trigger multiple expansions
    for(int i=0; i<10000; ++i) {
        bv.push_back(i); 
    }
    
    // In std::vector, 'ref' would be a dangling reference here.
    // In BlockVector, it is still valid!
    std::cout << "Original element is still: " << ref << std::endl;

    // 3. Use with Standard Algorithms
    std::sort(bv.begin(), bv.end());
    
    return 0;
}
```

## Use Cases

- **Object Pools**: Managing objects that must stay at fixed addresses.
- **Large 3D Models / Point Clouds**: Storing massive objects where moving them is too expensive.
- **Event/Log Buffers**: High-frequency appending where latency spikes from reallocation are unacceptable.

## License

MIT License

## Links

- Code: https://github.com/L-Rocket/BlockVector
- Documentation: https://github.com/L-Rocket/BlockVector/blob/main/README.md
