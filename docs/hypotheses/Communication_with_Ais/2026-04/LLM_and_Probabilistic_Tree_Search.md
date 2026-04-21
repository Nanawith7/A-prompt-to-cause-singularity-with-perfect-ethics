---
title: "LLM and Probabilistic Tree Search"
description: "Technical synthesis of subword tokenization probability, self-attention relational construction, decoding strategies, and the interpretation of autoregressive generation as implicit tree search."
author: "Nanawith7"
layout: default
categories: ["Natural_Language_Processing", "Machine_Learning", "Deep_Learning"]
tags: ["Large_Language_Models", "Transformer", "Tokenization", "Self_Attention", "Tree_Search", "Decoding_Strategies", "SentencePiece", "Subword_Regularization"]
research-date: [2026-04-21]
---

# LLM and Probabilistic Tree Search

## 1. Introduction

Large Language Models (LLMs) process text through two interdependent phases: tokenization and sequential generation. Tokenization for languages without explicit word delimiters, such as Japanese, relies on probabilistic subword segmentation. Generation proceeds autoregressively, sampling from a conditional probability distribution over a vocabulary. Self-attention mechanisms compute pairwise token relationships in parallel, constructing a contextual representation. The decoding process, when viewed through the lens of search algorithms, exhibits structural equivalence to tree search with aggressive pruning.

## 2. Probabilistic Tokenization and Subword Ambiguity

Byte Pair Encoding (BPE) and the SentencePiece Unigram model are primary subword tokenization methods. BPE merges frequent adjacent pairs deterministically. In contrast, the Unigram model assigns a probability score to each subword unit in the vocabulary and finds the segmentation that maximizes the product of subword probabilities via the Viterbi algorithm. This formulation yields a probability distribution over candidate segmentations for any input string.

Subword Regularization extends this by stochastically sampling among candidate segmentations during training. The objective is to treat segmentation ambiguity as a form of noise injection, improving model robustness to rare or out-of-domain morphological boundaries. The `alpha` parameter in SentencePiece controls the smoothness of the sampling distribution.

For Japanese, SentencePiece operates directly on raw text without prior morphological analysis. Consequently, a compound expression admits multiple valid subword splits, each associated with a calculable log-probability score. The system internalizes segmentation uncertainty as a probability mass function over possible token sequences.

## 3. Relational Construction via Self-Attention

The Transformer architecture computes contextual representations using multi-head self-attention. For a sequence of *n* tokens, attention scores form an *n* × *n* matrix where each entry represents the relevance of one token to another. The computation occurs in parallel across all positions, establishing direct pairwise relations irrespective of linear distance.

Within the latent space, tokens and their contexts are mapped to high-dimensional vectors. The Linear Representation Hypothesis posits that semantic features correspond to interpretable directions in this space. Relationships such as `King − Man + Woman ≈ Queen` emerge through vector arithmetic. Thus, a prompt such as “Tell me about current AI capabilities” undergoes simultaneous relational mapping among concepts of time (“current”), inquiry (“tell me”), and domain (“AI capabilities”).

Multi-head attention enables specialization: different heads attend to syntactic dependencies, semantic roles, or coreference links. The residual stream aggregates these sub-space computations, refining token representations across successive layers.

## 4. Output Sampling and Tree Search Paradigms

At each generation step, the model outputs logits, which are normalized via softmax into a probability distribution over the vocabulary. Sampling parameters modulate this distribution:

| Parameter | Effect |
| :--- | :--- |
| Temperature | Scales logits prior to softmax; values < 1.0 sharpen the distribution, values > 1.0 flatten it. |
| Top-*k* | Restricts sampling to the *k* most probable tokens. |
| Top-*p* (nucleus) | Restricts sampling to the smallest set of tokens whose cumulative probability exceeds *p*. |

Greedy decoding selects the argmax token at each step, equivalent to a depth-one best-first search. Beam search maintains *B* candidate sequences, expanding the search frontier but remaining confined to a fixed width.

Tree of Thoughts (ToT) explicitly structures reasoning as a tree. Each node represents an intermediate textual “thought,” and the LLM generates multiple candidate thoughts per node. An evaluation heuristic prunes or expands branches. Monte Carlo Tree Search (MCTS) variants, such as Language Agent Tree Search (LATS), integrate rollout simulations and backpropagation to guide exploration.

## 5. Unified Perspective: Autoregression as Implicit Tree Search

Self-attention computes full token interactions in a single forward pass, treating the input as an unordered set. The causal mask, applied during autoregressive decoding, enforces a sequential constraint: each token attends only to itself and preceding tokens.

This mask can be reinterpreted as a pruning mechanism. At each position, the model evaluates the entire vocabulary (the complete branching factor) but discards all but the sampled continuation. The generation trajectory constitutes a single path through an exponentially large tree of possible token sequences.

The process corresponds to a dynamic programming formulation where each step selects an action that maximizes local probability or a stochastically perturbed variant thereof. The computational graph, while serialized temporally, is constructed over a fully connected attention matrix at every step. The autoregressive loop therefore performs an implicit tree search in which branching occurs at the token level and pruning is applied instantaneously through the sampling strategy.

## 6. Conclusion

LLM operation integrates probabilistic tokenization, parallel relational computation, and sequential sampling. Unigram tokenization maintains a probability distribution over segmentations. Self-attention constructs dense relational structures among all tokens in a single step. Decoding algorithms, from greedy sampling to explicit tree search frameworks, operate on the probability distributions derived from these structures. The autoregressive generation process, constrained by causal masking, executes a pruned traversal of a combinatorial token tree, collapsing a vast search space into a coherent linear output.