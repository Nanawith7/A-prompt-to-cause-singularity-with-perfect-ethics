#!/usr/bin/env python3
"""
Obsidian Vault Tag Normalizer (using regex library for PCRE support)
With enhanced debug logging and fuzzy matching for common delimiter variations.
"""

import os
import regex as re  # PCRE互換の正規表現ライブラリ
import yaml
import argparse
from pathlib import Path

DEBUG = True

def load_mapping(yaml_path):
    """Load canonical tag mapping from YAML file."""
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    mapping = {}
    for cluster in data['clusters']:
        canonical = cluster['canonical']
        for alias in cluster['aliases']:
            if alias == canonical:
                continue
            mapping[alias] = canonical
    return mapping

def normalize_alias_pattern(alias):
    """
    Convert an alias string into a regex pattern that matches common delimiter variations.
    Examples:
        "AI Alignment" -> "AI[ _-]+Alignment"
        "Deep Learning" -> "Deep[ _-]+Learning"
    """
    # エスケープしてから、スペース/ハイフン/アンダースコアの連続を置換
    escaped = re.escape(alias)
    pattern = re.sub(r'\\[ _-]|[ _-]', r'[ _-]+', escaped)
    return pattern

def normalize_content(content, mapping, file_path=""):
    r"""
    Replace all occurrences of alias tags with canonical tags.
    Returns (new_content, replacement_count, details)
    """
    original_content = content
    replacement_count = 0
    details = []

    # 大文字小文字を無視するフラグ
    flags = re.IGNORECASE | re.MULTILINE

    # 1. 本文中の #タグ を置換
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        # タグは # で始まり、単語境界で終わる
        pattern = r'(?<!\w)#\K' + alias_pattern + r'(?!\w)'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  Inline #{alias} -> #{canonical} ({len(matches)} occurrences)")

    # 2. フロントマター内の tags: [alias, ...] を置換（引用符の有無を考慮）
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        # リスト内の要素：前後にスペース、カンマ、括弧などがある
        pattern = r'(?<=tags:\s*\[[^\]]*?(?:,|^)\s*)"?' + alias_pattern + r'"?\s*(?=(?:,|\]))'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  FM inline {alias} -> {canonical} ({len(matches)} occurrences)")

    # 3. 複数行 YAML 形式 (tags:\n  - alias) を置換
    for alias, canonical in mapping.items():
        alias_pattern = normalize_alias_pattern(alias)
        # 行頭の - の後ろに alias がある形式
        pattern = r'(?<=^\s*-\s+)"?' + alias_pattern + r'"?\s*$'
        matches = list(re.finditer(pattern, content, flags=flags))
        if matches:
            content = re.sub(pattern, canonical, content, flags=flags)
            replacement_count += len(matches)
            details.append(f"  FM multiline {alias} -> {canonical} ({len(matches)} occurrences)")

    return content, replacement_count, details

def debug_sample_files(vault_path, max_files=5):
    """Print lines containing '#' or 'tags:' from the first few files for debugging."""
    print("\n[DEBUG] Sample file tag lines:")
    count = 0
    for md_file in Path(vault_path).rglob('*.md'):
        if count >= max_files:
            break
        print(f"\n--- {md_file} ---")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if '#' in line or 'tags:' in line.lower():
                        print(line.rstrip())
        except Exception as e:
            print(f"  [Error reading file: {e}]")
        count += 1

def process_vault(vault_path, mapping, dry_run=False):
    vault_path = Path(vault_path)
    total_files = 0
    updated_files = 0
    total_replacements = 0

    for md_file in vault_path.rglob('*.md'):
        total_files += 1
        if dry_run:
            print(f"[DRY RUN] Would process: {md_file}")
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            print(f"[ERROR] Could not read {md_file}: {e}")
            continue

        new_content, count, details = normalize_content(content, mapping, str(md_file))

        if count > 0:
            print(f"\n📄 {md_file}")
            for detail in details:
                print(detail)
            total_replacements += count
            updated_files += 1

            if not dry_run:
                try:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                except Exception as e:
                    print(f"[ERROR] Could not write {md_file}: {e}")

    print(f"\n{'='*50}")
    print(f"Total files scanned: {total_files}")
    print(f"Files updated: {updated_files}")
    print(f"Total replacements: {total_replacements}")

def main():
    parser = argparse.ArgumentParser(description='Normalize Obsidian tags based on YAML mapping.')
    parser.add_argument('vault_path', help='Path to the root of the Obsidian vault')
    parser.add_argument('--mapping', default='canonical_tag.yaml', help='Path to YAML mapping file')
    parser.add_argument('--dry-run', action='store_true', help='Show files that would be processed without changing them')
    args = parser.parse_args()

    mapping = load_mapping(args.mapping)
    print(f"Loaded {len(mapping)} alias mappings.")

    if DEBUG:
        print("\n[DEBUG] Alias -> Canonical mapping (first 10):")
        for alias, canonical in sorted(mapping.items())[:10]:
            print(f"  {alias} -> {canonical}")
        if len(mapping) > 10:
            print(f"  ... and {len(mapping) - 10} more")

        # 実際のファイル内容をサンプル表示
        debug_sample_files(args.vault_path)

    process_vault(args.vault_path, mapping, args.dry_run)

    if args.dry_run:
        print("\n[DRY RUN] No files were changed.")
    else:
        print("\nTag normalization completed. Please restart Obsidian to refresh the cache.")

if __name__ == '__main__':
    main()