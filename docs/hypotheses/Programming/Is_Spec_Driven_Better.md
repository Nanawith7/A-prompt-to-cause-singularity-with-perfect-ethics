---
title: "Is Spec Driven Better"
description: "A technical evaluation of Spec-Driven Development (SDD) versus traditional codebase-context loading in AI coding, based on 2025-2026 tooling and research."
author: "Nanawith7"
layout: default
categories: ["AI Engineering", "Software Architecture"]
tags: ["Spec-Driven_Development", "Context_Engineering", "AI_Coding_Agents", "Codebase_Architecture"]
---

# Is Spec Driven Better

## 1. The Core Question

In AI‑assisted coding, an API works by reading only its specification (interface). A codebase, however, forces AI tools to load large parts of the entire codebase. The question arises: **Should codebases be structured to rely only on specifications, just like APIs?**

## 2. Why APIs Work With Only Specifications

APIs function on specifications alone because of two established principles:

- **Information hiding**: The interface hides implementation details that are likely to change.
- **Design by Contract (DbC)**: Each function defines preconditions, postconditions, and invariants. This creates a formal handshake between components.

An API defines *what* a component does, not *how* it does it. The consumer never needs the internal state or side effects.

## 3. Why Codebases Cannot Be Reduced to Specifications Only

Codebases resist a specification‑only structure due to four inherent factors:

| Factor | Description |
|--------|-------------|
| **State** | Most software complexity comes from state. State creates temporal coupling – same input may produce different outputs at different times. |
| **Implicit dependencies** | Many dependencies between components are not explicit; they can only be discovered by analyzing the code itself. |
| **Context boundary mismatch** | A compiler sees a codebase as a graph. An LLM sees it as a finite buffer of text tokens. The LLM cannot traverse dependencies deterministically. |
| **Spec‑implementation gap** | Even with perfect intent, the abstraction gap between specification and implementation always exists. |

Pure functional programming (immutability, referential transparency) reduces these factors but does not eliminate them for real‑world systems that require I/O, databases, or user interaction.

## 4. Why AI Coding Tools Load “Everything”

Current AI coding assistants do not literally send every file to the LLM on every request. Instead, they use four architectural patterns to make the entire codebase *referencable*:

| Pattern | Tools | Mechanism |
|---------|-------|-----------|
| Dynamic RAG + index | Cursor | Semantic graph of symbols, retrieved by vector similarity |
| Real‑time context extraction | GitHub Copilot | Ranked selection from open files, imports, and embeddings |
| Repository map + graph ranking | Aider | Dependency graph with token‑budgeted node selection |
| Agentic dynamic exploration (no RAG) | Cline | AST‑driven, on‑demand import tracing |

The perception of “loading everything” arises because tools try to avoid missing implicit dependencies. However, sending too much irrelevant information causes the **Lost in the Middle** problem: important signals are diluted, and model performance degrades.

## 5. Spec‑Driven Development (SDD) as the Alternative

Spec‑Driven Development (SDD) is a methodology where the specification becomes the source of truth, and code is a generated or verified secondary artifact. Major implementations as of 2026 include:

- **OpenSpec**: Lightweight spec layer (`openspec/specs/` and `openspec/changes/`) added to existing codebases (brownfield‑first).
- **GitHub Spec Kit**: Three‑step process (requirements → design → tasks) plus a “Constitution” for invariant rules.
- **Amazon Kiro**: Guided workflow for requirements, design, and task creation.
- **Tessl Framework**: Radical approach – maintain the specification, not the code.

SDD shifts the developer’s work from code editing to specification iteration. Changes are cheap at the spec level and expensive at the code level.

## 6. Does SDD Make “Spec‑Only” Codebases Achievable?

SDD does not eliminate code. It adds a **specification layer** that is versioned alongside the code. The specification layer serves as the primary input for AI agents.

**What SDD achieves**:
- High signal‑to‑noise ratio for LLM context
- Persistent, session‑spanning project knowledge
- Reduced token cost (Context Engineering shows up to 5.5× fewer tokens)

**What SDD does not solve completely**:
- Brownfield intent problem: Existing codebases with real users have accumulated intent that is hard to extract into specs.
- Spec‑code divergence: Humans may forget to update specs when changing code.
- Review cost: Long spec files become difficult to review.

## 7. Context Engineering and Recursive Access

Two parallel developments address the “load everything” problem without requiring a full spec‑only codebase:

### Context Engineering
- Uses files like `CLAUDE.md`, `.claudeignore`, and sub‑agents to give AI agents explicit, structured knowledge about the project.
- Focuses on *what information the model should access right now* rather than *how to phrase the prompt*.

### Recursive Language Model (RLM)
- Treats the codebase as an external environment that the LLM can explore programmatically.
- A root LM recursively calls itself on sub‑chunks, retrieving only the needed symbols, callers, or implementations on demand.
- CodeRLM (MIT) applies this pattern to codebases using Tree‑sitter based indexes.

## 8. Evaluation: Is Spec‑Driven Better?

The comparison between traditional “load everything” and SDD depends on the project phase and codebase age.

| Dimension | Traditional (full‑context loading) | Spec‑Driven Development |
|-----------|-------------------------------------|-------------------------|
| **Greenfield (0→1)** | Acceptable, but often includes noise | Better – high S/N ratio, fast iteration |
| **Brownfield (existing)** | Pragmatic – works without upfront spec investment | Requires tooling like OpenSpec; harder but possible |
| **Token cost** | Higher (inefficient retrieval) | Lower (spec is compact) |
| **Risk of spec‑code drift** | None (code is truth) | Present – needs discipline or automation |
| **Handling implicit dependencies** | Captures them (at cost of noise) | May miss them if not explicitly described |

**Observed industry shift (2025‑2026)** : The trend moves from “Vibe Coding” (chat‑based, exploratory) to **Spec Coding** (spec‑first, convergent). Gartner predicts that by 2028, 75% of enterprise software engineers will use AI code assistants, and by 2030, 80% of organizations will reorganize into AI‑augmented “tiny teams” where specifications drive the work.

## 9. Conclusion

Spec‑Driven Development is **better** for greenfield projects and for modules where the specification can be kept precise and up‑to‑date. For large, brownfield codebases with accumulated implicit dependencies, a hybrid approach works best: add a specification layer (e.g., OpenSpec) while still allowing AI agents to perform targeted, recursive access to the actual code when the spec is insufficient.

The long‑term direction is a codebase where the specification is a first‑class citizen. Complete elimination of code is neither necessary nor feasible. Instead, the evolution is from “make the AI read all the code” to “make the AI read the specification and verify against the code.”

Thus, the answer to “Is Spec Driven Better?” is: **Yes, under conditions where specifications can be maintained as a live, executable source of truth. For existing systems, a gradual addition of a spec layer outperforms the naive “load everything” approach.**