---
title: "Implementation Plan on C++"
description: "A technical framework for applying Deep Coding methodology to C++: structural specifications, generative conformance, skeleton-tissue architecture, build system integration, and incremental migration from legacy codebases."
author: "Nanawith7"
layout: default
categories: ["Software Engineering", "C++", "AI-Assisted Development"]
tags: ["Deep Coding", "C++20", "Generative Conformance", "Structural Specification", "CMake", "Modules", "Concepts", "Code Generation"]
---

# Implementation Plan on C++

## 1. Scope

This document provides a **technical implementation plan** for applying the Deep Coding methodology to C++.  
It assumes the reader understands Deep Coding’s core principles (structural separation, generative conformance, skeleton‑tissue architecture, fixed premises, recursive refinement) and focuses exclusively on their **C++‑specific realization**.  

No philosophical or metaphysical claims are made; all terms are mapped to concrete language features and build tools.

## 2. Mapping Deep Coding Principles to C++

| Deep Coding Principle | C++ Realization | Required Language / Tool Feature |
|-----------------------|----------------|----------------------------------|
| **Structural specification** | Interface contracts expressed as C++20 Concepts + JSON Schema / OpenAPI | Concepts (`<concepts>`), external schema files |
| **Generative conformance** | Code generation from schema → implementation | External generators (Avrotize, GTAD) or template metaprogramming (TMP) |
| **Skeleton (invariant)** | Non‑virtual interface (NVI) base classes or CRTP templates; C++20 module interface units | `virtual` + `sealed`, CRTP, `export module` |
| **Tissue (generated)** | Concrete derived classes or template instantiations; module implementation units | Derived classes, template specializations, `module :private` |
| **Fixed premise** | Git commit hash embedded in binary + module interface frozen | `-DGIT_COMMIT_HASH`, C++20 module BMI |
| **Recursive refinement** | Phased commits + incremental regeneration | Git tags, CMake `CODEGEN` target |
| **Validation gate** | Static assertions (Concepts) + architecture tests (custom CMake/CTest) | `static_assert`, `clang-check`, `add_test` |

## 3. Structural Specification in C++

### 3.1 Interface‑Level Constraints (Concepts)

Use C++20 Concepts to define **compile‑time contracts** for template arguments.  
Example:
```cpp
template<typename T>
concept Serializable = requires(T t, std::ostream& os) {
    { t.serialize(os) } -> std::convertible_to<bool>;
};
```

### 3.2 Data Structure Specifications (JSON Schema / OpenAPI)

For cross‑language or versioned data, define a **JSON Schema** or **OpenAPI** file.  
Generate C++ classes using **Avrotize** (recommended) or **GTAD** (for Qt projects).  
These generators produce header‑only or source‑only classes that strictly conform to the schema.

### 3.3 Module Boundary Specifications (C++20 Modules)

Use **module interface units** (`.ixx`) as the physical boundary of a structural specification.  
All public symbols are `export`ed; implementation details are hidden in module implementation units (`.cpp`).  
This enforces **fixed premise**: once the interface unit is committed, its binary interface (BMI) is frozen.

## 4. Generative Conformance

### 4.1 External Generation (Build‑Time)

**CMake integration** (modern, recommended for most cases):
```cmake
add_custom_command(
    OUTPUT ${CMAKE_CURRENT_BINARY_DIR}/generated/player.hpp
    COMMAND avrotize -i player.schema.json -o ${CMAKE_CURRENT_BINARY_DIR}/generated
    DEPENDS player.schema.json
    COMMENT "Generating C++ classes from JSON schema"
)
add_library(generated_objects OBJECT ${CMAKE_CURRENT_BINARY_DIR}/generated/player.hpp)
```

**CMake 3.31+ `CODEGEN` target** – run only code generation without full build:
```bash
cmake --build . --target codegen
```

### 4.2 Compile‑Time Generation (Template Metaprogramming)

For type‑level generation (e.g., compile‑time dispatch, policy selection), use **TMP** with Concepts.  
Example: generating a visitor from a type list:
```cpp
template<typename... Ts> struct overload : Ts... { using Ts::operator()...; };
template<typename... Ts> overload(Ts...) -> overload<Ts...>;
// usage: overload{[](int i){}, [](double d){}} visitor;
```
TMP incurs zero runtime overhead but is limited to type‑level transformations.

### 4.3 Future: C++26 Reflection (Expected 2028–2029)

Once available, `#embed` + reflection will replace external generators:
```cpp
#include <embed>
constexpr std::string_view schema_data = std::embed("player.schema.json");
// use reflection to generate struct Player { ... } at compile time
```
Plan for a smooth migration by keeping generation logic in a separate CMake module.

## 5. Skeleton–Tissue Architecture

### 5.1 Skeleton (Invariant, Human‑Maintained)

Implement as:
- **Abstract base class** with **NVI** pattern (public non‑virtual, private/protected virtual).
- **CRTP** base template for zero‑overhead static polymorphism.
- **Module interface unit** (`.ixx`) that exports only the skeleton.

Example (NVI):
```cpp
class ServiceSkeleton {
public:
    void execute() final { before(); doExecute(); after(); }
private:
    virtual void doExecute() = 0;
    virtual void before() {}
    virtual void after() {}
};
```

### 5.2 Tissue (Generated, AI‑ or Tool‑Managed)

Implement as:
- Derived classes that override virtual hooks (for NVI).
- Template specializations (for CRTP).
- Module implementation units (`.cpp`) that `import` the skeleton interface.

**Dependency rule**: Tissue may depend on Skeleton, but never the reverse. Enforce via:
- CMake `target_link_libraries(tissue PRIVATE skeleton)`.
- Clang‑check rule: `"tissue/.*" include only "skeleton/.*"`.

### 5.3 Physical Separation

| Artifact | Location | Ownership | Regeneration |
|----------|----------|-----------|---------------|
| Skeleton (interface unit) | `skeleton/module.ixx` | Human (hand‑written) | Never |
| Skeleton implementation (if any) | `skeleton/impl.cpp` | Human | Never |
| Tissue (implementation unit) | `tissue/module.cpp` | Generated | On specification change |
| Tissue (additional headers) | `tissue/*.hpp` | Generated | On specification change |

## 6. Build System Integration (CMake)

### 6.1 Required CMake Version

- **CMake 3.20+** for basic `add_custom_command` and `target_sources`.
- **CMake 3.31+** for `CODEGEN` target and `DEPFILE` support (recommended).

### 6.2 Fixed Premise via Git Hash

Embed the current commit hash into a generated header:
```cmake
execute_process(COMMAND git rev-parse HEAD
    OUTPUT_VARIABLE GIT_HASH
    OUTPUT_STRIP_TRAILING_WHITESPACE)
configure_file(version.h.in ${CMAKE_BINARY_DIR}/version.h)
```
`version.h.in`:
```cpp
#define GIT_COMMIT_HASH "@GIT_HASH@"
```
This allows runtime verification that the binary matches a known specification.

### 6.3 Recursive Refinement Workflow

1. **Phase N** completed → `git tag phase-N-complete`
2. Modify structural specification (e.g., `player.schema.json`)
3. Run `cmake --build . --target codegen` (regenerate tissue only)
4. Build and test: `cmake --build . && ctest`
5. Commit new tissue code (optional, but recommended for reproducibility)
6. `git tag phase-N+1-complete`

### 6.4 Validation Gates in CI

Add to GitHub Actions / GitLab CI:
```yaml
- name: Check generated code matches specification
  run: |
    cmake --build . --target codegen
    git diff --exit-code -- '**/*.generated.*'
- name: Architecture dependency test
  run: |
    ! grep -r "#include \"skeleton/" tissue/ | grep -v "skeleton/interface"
- name: ABI compatibility (if skeleton unchanged)
  run: abi-compliance-checker -old libold.so -new libnew.so
```

## 7. Legacy Code Integration (Strangler Pattern)

### 7.1 Step 1 – Interface Extraction

Use **Clang LibTooling** to automatically extract public method signatures from a legacy class:
```bash
clang-extract -p compile_commands.json LegacyClass.cpp --extract-class LegacyClass
```
This produces a candidate interface (pure virtual class). Manually refine it into a **skeleton**.

### 7.2 Step 2 – Parallel Implementation

Implement the new tissue (generated from specification) alongside the legacy implementation.  
Use a factory that switches based on a compile‑time flag or runtime config.

### 7.3 Step 3 – Gradual Switchover

Replace call sites one by one. After each replacement, run the same regression tests.

### 7.4 Step 4 – Remove Legacy Code

Once no callers remain, delete the legacy implementation. The skeleton interface remains as the permanent contract.

### 7.5 Adaptor for Reverse Dependencies

If legacy code must call new Deep‑Coded modules, write a **facade** inside the legacy codebase that forwards to the new module. The facade implements the legacy‑expected interface but delegates to the generated tissue.

## 8. Recommended Toolchain

| Component | Tool | Version Requirement |
|-----------|------|----------------------|
| Compiler | GCC, Clang, or MSVC | C++20 full support |
| Build system | CMake | 3.31+ (for `CODEGEN`) |
| Schema → C++ | Avrotize | 3.0+ |
| Schema → C++ (Qt) | GTAD | latest |
| ABI checking | abi‑compliance‑checker | 2.3+ |
| AST analysis | Clang LibTooling | matching compiler |
| Version control | Git | any |
| CI | GitHub Actions / GitLab CI | – |

## 9. Phased Rollout Plan

| Phase | Duration | Activities | Success Metric |
|-------|----------|------------|----------------|
| **0: Pilot** | 1‑2 weeks | Pick one non‑critical module (e.g., configuration reader). Write JSON schema, generate C++ classes, integrate into build. | Generation works; tests pass. |
| **1: Single module** | 2‑4 weeks | Replace one internal component with Deep‑Coded version. Keep old code as fallback. | No regression; build time increase <10%. |
| **2: Expand to API layer** | 1‑2 months | Convert all REST/DTO classes to generated code. Use OpenAPI generator. | API bugs drop by >50%. |
| **3: Introduce Modules** | 2‑3 months | Convert skeleton interfaces to C++20 module interface units. Separate tissue into module implementation units. | Build times improve due to BMI reuse. |
| **4: Full adoption** | 6‑12 months | Apply methodology to all new features; migrate legacy modules on a need‑basis. | Implementation‑level bugs near zero; specification changes become the primary development activity. |

## 10. Constraints and Exceptions

Do **not** apply Deep Coding to:

- **Performance‑critical loops** (e.g., inner rendering loops, real‑time signal processing) – use hand‑tuned code with static dispatch.
- **Macro‑heavy codebases** (e.g., legacy C with `#define` state machines) – extraction cost exceeds benefit.
- **UI event handling** (callback‑heavy, framework‑specific) – generate only data models, not event logic.
- **One‑off scripts or prototypes** – overhead not justified.

For these areas, maintain conventional C++ practices and only use generated data structures (not logic).

## 11. Summary

Deep Coding can be implemented in C++ using **Concepts + JSON Schema + CMake + Modules + TMP**.  
The methodology reduces implementation‑level bugs, makes interfaces explicit, and enables safe, incremental evolution.  
The provided toolchain and phased plan allow gradual adoption in both greenfield and legacy projects.  
C++26 reflection will further simplify generation but is not required for immediate benefit.