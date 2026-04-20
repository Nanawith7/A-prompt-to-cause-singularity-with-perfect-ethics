#!/usr/bin/env python3
"""
Obsidian Vault Tag Normalizer (Flexible canonicalization + unconditional rewrite)

- Parses YAML frontmatter to get raw tag strings.
- Applies flexible matching (case-insensitive, delimiter-normalized) against alias mapping
  and also against canonical names themselves.
- Replaces tags with canonical names if matched.
- Formats all tags to lower_snake_case, wrapped in double quotes.
- Unconditionally rewrites frontmatter tags: line.
- Does NOT modify inline #tags in body text.
"""

import os
import sys
import regex as re
import yaml
import argparse
from pathlib import Path

# ----------------------------------------------------------------------
# Logging setup
# ----------------------------------------------------------------------
class Tee:
    def __init__(self, file_path, mode='w'):
        self.file = open(file_path, mode, encoding='utf-8')
        self.stdout = sys.stdout

    def write(self, message):
        self.stdout.write(message)
        self.file.write(message)

    def flush(self):
        self.stdout.flush()
        self.file.flush()

    def close(self):
        self.file.close()

log_tee = None

def log_print(*args, **kwargs):
    print(*args, **kwargs)

# ----------------------------------------------------------------------
DEBUG = True

def normalize_tag_string(s):
    """Convert any tag string to a normalized form for flexible comparison."""
    if not isinstance(s, str):
        s = str(s)
    s = s.strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1]
    s = re.sub(r'[ _-]+', '_', s)
    return s.lower()

def load_mapping(yaml_path):
    with open(yaml_path, 'r', encoding='utf-8') as f:
        data = yaml.safe_load(f)
    alias_to_canonical = {}
    canonical_norms = {}
    for cluster in data['clusters']:
        canonical = cluster['canonical']
        norm_canonical = normalize_tag_string(canonical)
        canonical_norms[norm_canonical] = canonical
        for alias in cluster['aliases']:
            norm_alias = normalize_tag_string(alias)
            if norm_alias == norm_canonical:
                continue
            alias_to_canonical[norm_alias] = canonical
    return alias_to_canonical, canonical_norms

def canonicalize_tag(raw_tag, alias_to_canonical, canonical_norms):
    norm = normalize_tag_string(raw_tag)
    if norm in alias_to_canonical:
        return alias_to_canonical[norm]
    if norm in canonical_norms:
        return canonical_norms[norm]
    return None

def format_tag_for_output(s):
    s = str(s).strip()
    if (s.startswith('"') and s.endswith('"')) or (s.startswith("'") and s.endswith("'")):
        s = s[1:-1]
    s = re.sub(r'\s+', '_', s)
    return f'"{s}"'

def format_all_frontmatter_tags(content, alias_to_canonical, canonical_norms):
    frontmatter_pattern = r'^---\s*\n(.*?)\n---\s*\n'
    match = re.search(frontmatter_pattern, content, flags=re.DOTALL)
    if not match:
        return content, False, "No frontmatter found"

    fm_text = match.group(1)
    try:
        fm_data = yaml.safe_load(fm_text)
        if fm_data is None:
            fm_data = {}
    except yaml.YAMLError as e:
        return content, False, f"YAML parse error: {e}"

    if 'tags' not in fm_data:
        return content, False, "No 'tags' field in frontmatter"

    tags = fm_data['tags']
    if isinstance(tags, str):
        tags = [tags]
    if not isinstance(tags, list):
        return content, False, f"Tags field is not a list: {type(tags)}"

    new_tags = []
    for raw_tag in tags:
        if raw_tag is None:
            continue
        canonical = canonicalize_tag(raw_tag, alias_to_canonical, canonical_norms)
        if canonical:
            new_tags.append(format_tag_for_output(canonical))
        else:
            new_tags.append(format_tag_for_output(raw_tag))

    replacement_line = 'tags: [' + ', '.join(new_tags) + ']'
    tags_line_pattern = r'^tags:\s*.*?(?=\n\S|\n---|$)'
    new_fm_text = re.sub(tags_line_pattern, replacement_line, fm_text, flags=re.MULTILINE | re.DOTALL)

    new_content = content[:match.start(1)] + new_fm_text + content[match.end(1):]
    return new_content, True, f"Replaced tags line with: {replacement_line}"

def normalize_content(content, alias_to_canonical, canonical_norms, file_path=""):
    # フロントマターのタグ行のみを正規化（本文中の #タグ は一切変更しない）
    content, fm_changed, fm_msg = format_all_frontmatter_tags(content, alias_to_canonical, canonical_norms)
    return content, fm_changed, fm_msg

def debug_sample_files(vault_path, max_files=5):
    log_print("\n[DEBUG] Sample file tag lines:")
    count = 0
    for md_file in Path(vault_path).rglob('*.md'):
        if count >= max_files:
            break
        log_print(f"\n--- {md_file} ---")
        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
                for line in lines:
                    if 'tags:' in line.lower():
                        log_print(line.rstrip())
        except Exception as e:
            log_print(f"  [Error reading file: {e}]")
        count += 1

def process_vault(vault_path, alias_to_canonical, canonical_norms, dry_run=False):
    vault_path = Path(vault_path)
    total_files = 0
    updated_files = 0

    for md_file in vault_path.rglob('*.md'):
        total_files += 1
        if dry_run:
            log_print(f"[DRY RUN] Would process: {md_file}")
            continue

        try:
            with open(md_file, 'r', encoding='utf-8') as f:
                content = f.read()
        except Exception as e:
            log_print(f"[ERROR] Could not read {md_file}: {e}")
            continue

        new_content, fm_changed, fm_msg = normalize_content(content, alias_to_canonical, canonical_norms, str(md_file))

        if fm_changed:
            log_print(f"\n📄 {md_file}")
            log_print(f"  FM action: {fm_msg}")
            updated_files += 1

            if not dry_run:
                try:
                    with open(md_file, 'w', encoding='utf-8') as f:
                        f.write(new_content)
                except Exception as e:
                    log_print(f"[ERROR] Could not write {md_file}: {e}")

    log_print(f"\n{'='*50}")
    log_print(f"Total files scanned: {total_files}")
    log_print(f"Files updated: {updated_files}")

def main():
    global log_tee
    parser = argparse.ArgumentParser(description='Normalize Obsidian tags.')
    parser.add_argument('vault_path', help='Path to Obsidian vault')
    parser.add_argument('--mapping', default='canonical_tag.yaml', help='YAML mapping file')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    log_file_path = Path(args.vault_path) / 'log.txt'
    log_tee = Tee(str(log_file_path), 'w')
    sys.stdout = log_tee

    try:
        alias_to_canonical, canonical_norms = load_mapping(args.mapping)
        log_print(f"Loaded {len(alias_to_canonical)} alias mappings and {len(canonical_norms)} canonical norms.")

        if DEBUG:
            log_print("\n[DEBUG] Alias -> Canonical (first 10):")
            for alias, canonical in list(alias_to_canonical.items())[:10]:
                log_print(f"  {alias} -> {canonical}")
            debug_sample_files(args.vault_path)

        process_vault(args.vault_path, alias_to_canonical, canonical_norms, args.dry_run)

        if args.dry_run:
            log_print("\n[DRY RUN] No files were changed.")
        else:
            log_print("\nTag normalization completed. Restart Obsidian to refresh cache.")
    finally:
        sys.stdout = sys.__stdout__
        log_tee.close()
        print(f"Log saved to {log_file_path}")

if __name__ == '__main__':
    main()