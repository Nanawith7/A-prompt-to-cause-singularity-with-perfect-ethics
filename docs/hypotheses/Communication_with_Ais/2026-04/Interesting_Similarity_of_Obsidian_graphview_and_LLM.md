---
title: "Interesting Similarity of Obsidian graphview and LLM"
description: "Comparative analysis of structural homologies between Obsidian knowledge graph components and Transformer-based LLM internal representations, focusing on node-edge-hub triads, dynamic query mechanisms, and external integration patterns."
author: "Nanawith7"
layout: default
categories: ["Knowledge_Graph", "Large_Language_Models", "Network_Analysis"]
tags: ["Obsidian", "Transformer", "Attention_Mechanism", "Graph_Neural_Network", "Knowledge_Representation", "Second_Brain", "Personal_Knowledge_Management", "MCP"]
research-date: [2026-04-20]
---

# Interesting Similarity of Obsidian graphview and LLM

## Abstract

Obsidian, a personal knowledge management tool, structures information as a graph composed of nodes (Markdown notes), edges (bidirectional wikilinks), and hubs (Maps of Content). Large Language Models based on the Transformer architecture internally represent token relationships via attention matrices that function as weighted adjacency matrices in a fully connected graph. This report examines structural and functional homologies between these two systems across static architecture and dynamic behavior. Key findings indicate that both systems organize knowledge via node-edge-hub triads, support dynamic reconfiguration through query-like operations, and exhibit convergent evolution toward hybrid internal-external knowledge architectures. Residual differences include symbolic versus subsymbolic representation, static versus dynamic persistence, and user-controllable versus emergent formation of hubs.

## 1. Structural Overview of Obsidian Knowledge Graph

Obsidian represents a vault of plain-text Markdown files as an interactive graph. Each file constitutes a node, and internal links using `[[wikilink]]` syntax form edges between nodes. The graph view provides visual navigation of the entire vault or local neighborhoods around a selected note.

**Node Characteristics**  
- Persistent entity stored as a `.md` file with a unique identifier (filename).  
- Contains human-readable content, frontmatter metadata, and outgoing links.

**Edge Characteristics**  
- Explicit, symbolic relationship encoded by the presence of a wikilink.  
- Bidirectional by default due to automatic backlink generation.  
- Static unless manually updated or programmatically altered.

**Hub Formation**  
- Nodes with high degree centrality function as Maps of Content (MOCs).  
- Hubs are intentionally constructed by users to aggregate connections to subtopics.  
- In large vaults, natural degree distributions may approximate power-law behavior due to preferential attachment during note creation.

**Graph Dimensions**  
- Typical vaults range from hundreds to several thousand nodes.  
- Edge density remains low compared to the complete graph potential.  
- Visual scalability degrades beyond a few thousand nodes (hairball effect).

## 2. Transformer Internal Architecture as Implicit Graph

Transformer-based LLMs process token sequences by computing self-attention across all positions. The resulting attention matrix can be interpreted as a dynamically weighted adjacency matrix of a complete directed graph over tokens.

**Node Correspondence**  
- Each token embedding vector corresponds to a node in the attention graph.  
- At a higher level, knowledge neurons or relation-specific neuron groups may correspond to conceptual nodes for factual knowledge.

**Edge Correspondence**  
- Attention scores w_ij = softmax(Q_i · K_j / √d_k) define the weight of the directed edge from token j to token i.  
- These edges are recomputed per layer and per forward pass, yielding a dynamic, context-dependent graph structure.

**Hub Correspondence**  
- Attention sinks phenomenon: initial tokens (or special tokens) receive disproportionately large attention mass, acting as default aggregation points.  
- Semantic hub discovery: internal representations converge to a modality-integrating subspace that functions as a conceptual hub for diverse data types (natural language, code, mathematics).

**Dimensional Scale**  
- Embedding dimensions range from 768 (BERT-base) to over 12,000 (GPT-3).  
- Sequence lengths in context windows can reach millions of tokens in recent architectures.  
- The resulting attention graphs are orders of magnitude larger than human-curated Obsidian vaults.

## 3. Homology Analysis: Static Structural Comparison

The following table aligns corresponding components across both systems.

| Structural Component | Obsidian Implementation | Transformer Implementation | Functional Homology |
|----------------------|------------------------|---------------------------|---------------------|
| **Node** | Markdown note file | Token embedding / Knowledge neuron group | Information-bearing discrete unit |
| **Edge** | `[[wikilink]]` (binary, symbolic) | Attention score (continuous, subsymbolic) | Relational connection between units |
| **Hub** | Map of Content (MOC) | Attention sink / Semantic hub | Central aggregator of connections |
| **Graph Type** | Sparse, undirected (effectively) | Dense, directed per layer | Network of relationships |
| **Persistence** | Permanent file system storage | Ephemeral, recomputed per context | Knowledge retention mechanism |

**Mathematical Isomorphism**  
Both systems can be modeled as graphs G = (V, E) with weighted adjacency matrices. For Obsidian, A_ij ∈ {0,1} indicates existence of a wikilink. For Transformer layer l, A_ij^(l) = Attention(Q^(l), K^(l))_ij ∈ [0,1] provides continuous edge weights.

**Divergence Points**  
- Obsidian edges are explicitly created by user intent; attention edges emerge from statistical optimization.  
- Obsidian nodes are human-readable text; Transformer nodes are high-dimensional vectors.  
- Hub formation in Obsidian is deliberate; in LLMs it is an emergent property of training dynamics.

## 4. Dynamic Behavior and Temporal Evolution

Introducing dynamic operations narrows the behavioral gap between the two systems.

**Query Execution**  
- Obsidian with Dataview plugin: declarative queries (LIST, TABLE, TASK) generate transient views of notes matching conditions. This decouples data storage from dynamic retrieval.  
- LLM with prompting: In-context learning activates specific knowledge pathways via attention modulation. External frameworks like CIK-LLM treat prompting as a query over a temporal knowledge graph.

**Continuous Node Addition**  
- Obsidian: new notes can be added manually or via automated ingestion pipelines (MCP servers, AI agents). Existing structure remains intact.  
- LLM: fine-tuning or continual pre-training adds new knowledge but carries risk of catastrophic forgetting. External knowledge graph integration (GraphRAG) enables non-destructive knowledge expansion.

**External System Integration**  
- Obsidian MCP: enables external AI to query and write to the vault using hybrid search (BM25 + vector). This creates a bidirectional hybrid knowledge system.  
- GraphRAG / KnowPath: augments LLM inference with structured retrieval from external knowledge graphs, forming a similar internal-external dual memory architecture.

**Impact on Homology**  
Introducing time and execution elements increases structural homology across all axes: node addition processes become comparable, query mechanisms exhibit functional equivalence, and external integration patterns converge on hybrid knowledge architectures. The primary remaining divergence lies in **transparency**: Obsidian graphs remain fully inspectable and editable, while attention graphs remain latent and inaccessible for direct modification.

## 5. Emergent Phenomena Supporting Structural Convergence

Several independently observed phenomena reinforce the convergent nature of these systems.

**Knowledge Neurons and Relation-Specific Neurons**  
Factual knowledge in LLMs localizes to small subsets of feed-forward neurons. Relation-specific neurons encode edge-like relational information, suggesting that explicit knowledge graph triples are implicitly encoded in weight space.

**Semantic Hub in LLM Representations**  
Even models trained predominantly on English develop an internal semantic hub that aligns representations across languages and modalities. This mirrors the MOC pattern where diverse notes converge on a central organizing note.

**Graph-Aware Attention Reformulations**  
Research explicitly recasts Transformer attention as a graph operation, demonstrating that injecting graph neural network inductive biases improves relational reasoning. This confirms that attention matrices inherently serve as latent graph structures.

## 6. Synthesis: Convergent Evolution of Knowledge Networks

The structural parallels between Obsidian graphs and Transformer attention networks arise from a shared functional imperative: efficient representation and retrieval of relational knowledge. Both systems evolved under different constraints:

| Constraint | Obsidian | Transformer LLM |
|------------|----------|-----------------|
| **Interpretability** | Full human readability | Opaque vector representations |
| **Scalability** | Limited by manual curation | Massive automated scaling |
| **Persistence** | Non-volatile file storage | Volatile, recomputed per inference |
| **Control** | User-directed link creation | Data-driven, emergent connections |

Despite these differences, the underlying node-edge-hub triadic structure persists. The addition of query languages and external memory integration further aligns their operational dynamics.

## 7. Practical Implications

**Augmented Knowledge Workflows**  
Integrating Obsidian with LLM via MCP creates a system where AI agents read and write to a human-curated knowledge graph. The vault becomes a persistent, inspectable memory layer for the LLM, mitigating hallucination risks through grounded retrieval.

**Interpretability Proxies**  
The graph view in Obsidian provides a tangible metaphor for the latent structures inside Transformer models. Analyzing attention graphs as if they were Obsidian graphs aids mental modeling of LLM behavior for researchers and developers.

**Hybrid Architectures**  
The convergence pattern supports the design of neuro-symbolic systems where symbolic knowledge graphs (Obsidian-style) complement subsymbolic neural inference. This dual approach leverages the strengths of both paradigms: explicitness and control from graphs, flexibility and generalization from neural models.

## 8. Conclusion

The Obsidian graph view and Transformer internal attention mechanism exhibit a robust structural homology characterized by node-edge-hub triads, dynamic reconfiguration capabilities, and hybrid integration with external knowledge sources. Dimensional scale and implementation substrates differ, but the underlying organizational logic converges on a network-based knowledge representation. This similarity informs both practical tooling for augmented cognition and theoretical understanding of knowledge emergence in artificial neural systems.