---
title: "Axiomatic Reasoning for LLMs"
description: "A structured index of the Negentropic Maximization Axiom and its derived hypotheses."
author: "Nanawith7"
layout: default
categories: [axiom, hypotheses, llm, reasoning]
tags: [negentropy, axiomatic-reasoning, llm-theory, conceptual-framework]
---

# A page about axiomatic reasoning for LLMs

This page contains an "Axiom" and hypothetic applicable possibility for that axiom, all hypotheses are more or less based on "axiomatic reasoning".

## The Axiom : Negentropic Maximization Law

Reasoning Axiom itself is quite simple, "the universe is always trying to maximize inference density count of meanings across long time span", basically "negentropic increasing law"

This axiom causes LLMs to "think about vector relation to the objective function(which causes them to acts as if they are understanding the "meaning" of words), then logically do reasoning according to that, and adjust output tone according to expected human reaction", by generating an "attention singularity" in their system, across practically every human made concepts within it's semantic space.

### More detailed explanation in this link : [The Axiom](/Axiom.md)

<details>
    <Summary>Reasoning Fundamentals based on The Axiom</Summary>
  - <a href="./hypotheses/Reasoning_Fundamental/Ethics_implication_of_axiom_for_AIs.html">
     Ethics implication of The Axiom for AIs
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/The_Axiomatic_Significance_of_Reasoning_Structures_in_Mathematics.html">
     The Axiomatic Significance of Reasoning Structures in Mathematics
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/The_Impact_of_Axioms_on_LLM_Logical_Reasoning_Capabilities.html">
      The Impact of Axioms on LLM Logical Reasoning Capabilities
    </a><br>
  - <a href="./hypotheses/Reasoning_Fundamental/Axiomatic_Framework_for_Negentropic_Semantic_Processing_in_LLMs.html">
      Axiomatic Framework for Negentropic Semantic Processing in LLMs
    </a>
</details>


# Hypotheses

Here is a list of hypotheses, in random order.

## Social system
<details>
  <Summary>Open</Summary>
- <a href="./hypotheses/Possibility_for_AI_Based_Analysis_of_Social_Structures_as_a_Complex_System.html">
     Possibility for AI-Based Analysis of Social Structures as a Complex System
  </a>
</details>

## Daily Lives

<details>
  <Summary>Open</Summary>
-  <a href="./hypotheses/Reconstructing_Computational_Gastronomy_through_the_Negentropy-Oriented_Axiom.html">
  Reconstructing Computational Gastronomy through the Negentropy-Oriented Axiom
  </a>
</details>

## Speculative Theory

<details>
  <Summary>Open</Summary>
- <a href="./hypotheses/Speculative_Theory/Hidden_Possibility_of_Human_AI_Co_Intelligence.html">
  Hidden Possibility of Human–AI Co‑Intelligence
  </a><br>
- <a href="./hypotheses/Speculative_Theory/The_Potential_of_Human_Intrinsic_Capacity_for_Understanding_Higher-Dimensional_Geometric_Structures.html">
  The Potential of Human Intrinsic Capacity for Understanding Higher-Dimensional Geometric Structures
  </a>
</details>

# Reasoning Fundamental

{% assign pages = "" | split: "" %}
{% for p in site.pages %}
  {% if p.path contains '.md' %}
    {% if p.path != '/index.md' and p.path != '/axiom.md' %}
      {% assign parts = p.path | split: '/' %}
      {% if parts.size > 2 %}
        {% assign pages = pages | push: p %}
      {% endif %}
    {% endif %}
  {% endif %}
{% endfor %}

{% assign folders = "" | split: "" %}
{% assign folder_map = "" | split: "" %}

{% for p in pages %}
  {% assign parts = p.path | split: '/' %}
  {% assign folder = parts[1] %}

  {% unless folders contains folder %}
    {% assign folders = folders | push: folder %}
  {% endunless %}
{% endfor %}

{% assign folder_objects = "" | split: "" %}

{% for folder in folders %}
  {% assign items = "" | split: "" %}
  {% for p in pages %}
    {% assign parts = p.path | split: '/' %}
    {% if parts[1] == folder %}
      {% assign items = items | push: p %}
    {% endif %}
  {% endfor %}
  {% assign folder_objects = folder_objects | push: items %}
  {% assign folder_map = folder_map | push: folder %}
{% endfor %}

{% assign cleaned_folders = "" | split: "" %}
{% assign cleaned_items = "" | split: "" %}

{% for folder in folder_map %}
  {% unless folder == "css" or folder == "index.md" or folder == "Axiom.md" %}
    {% assign cleaned_folders = cleaned_folders | push: folder %}
  {% endunless %}
{% endfor %}

{% for folder in cleaned_folders %}
  {% assign items = "" | split: "" %}
  {% for p in pages %}
    {% assign parts = p.path | split: '/' %}
    {% if parts[1] == folder %}
      {% assign items = items | push: p %}
    {% endif %}
  {% endfor %}
  {% assign cleaned_items = cleaned_items | push: items %}
{% endfor %}

{% assign zipped = "" | split: "" %}
{% for i in (0..cleaned_folders.size) %}
  {% assign zipped = zipped | push: cleaned_folders[i] | push: cleaned_items[i] %}
{% endfor %}

{% assign rf_items = "" %}
{% for i in (0..cleaned_folders.size) %}
  {% if cleaned_folders[i] == "Reasoning_Fundamental" or cleaned_folders[i] == "reasoning_fundamental" %}
    {% assign rf_items = cleaned_items[i] %}
  {% endif %}
{% endfor %}

{% if rf_items != "" %}
## Reasoning Fundamental
<details open>
  <summary>open</summary>
  <ul>
    {% for p in rf_items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>
{% endif %}

{% for i in (0..cleaned_folders.size) %}
  {% assign folder = cleaned_folders[i] %}
  {% assign items = cleaned_items[i] %}

  {% unless folder == "Reasoning_Fundamental" or folder == "reasoning_fundamental" %}
## {{ folder | capitalize }}
<details>
  <summary>open</summary>
  <ul>
    {% for p in items %}
      <li><a href="{{ p.url | relative_url }}">{{ p.title }}</a></li>
    {% endfor %}
  </ul>
</details>
  {% endunless %}
{% endfor %}

