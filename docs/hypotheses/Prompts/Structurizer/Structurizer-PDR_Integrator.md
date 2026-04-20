---
title: "Structurizer-PDR Integrator"
description: "A prompt that receives a structured summary (from Sitemap_Structurizer), autonomously identifies relevant pages to research theme, outputs them in a single batch, and after user confirmation, generates a detailed research plan. Workflow: PDR input → summary + this prompt → file/URL input → research plan output."
author: "Nanawith7"
layout: default
categories: ["Prompt Engineering", "Research Workflow", "Pseudo Deep Research"]
tags: ["PDR", "autonomous_page_selection", "research_plan", "structured_summary", "batch_output"]
---

[]というテーマについて、まずはこの要約からリサーチプランの考案に必要、あるいは重要なページを判断、要約内部のタイトルとともに、最も重要と予測される10個まで番号付き箇条書きリスト形式(タイトルとURLのみ、リストの合間には一行の隙間を空ける)で一括出力し一旦出力を停止してくれ。リサーチプランに関しての処理は今回は行わない



---
This is a prompt that receives a structured summary (from Sitemap_Structurizer), autonomously identifies relevant pages to research theme, outputs them in a single batch, and after user confirmation, generates a detailed research plan. Workflow: PDR input → summary + this prompt → file/URL input → research plan output.