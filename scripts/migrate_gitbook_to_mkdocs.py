#!/usr/bin/env python3
import os
import re
import shutil
import sys
from pathlib import Path

try:
    import requests  # optional (for sitemap)
except Exception:
    requests = None

# Directories to skip entirely while copying
SKIP_DIRS = {".git", ".github", "node_modules", ".gitbook", ".idea", ".vscode", "venv", ".venv", "build", "dist"}

# File extensions to include when copying content (recursive)
INCLUDE_EXTS = {
    ".md", ".markdown", ".txt",
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp", ".bmp", ".ico",
    ".mp4", ".mov", ".webm",
    ".pdf", ".csv", ".json", ".yaml", ".yml", ".mermaid", ".drawio"
}

def ensure_dir(p: Path):
    p.mkdir(parents=True, exist_ok=True)

def copy_file(src: Path, dst: Path):
    ensure_dir(dst.parent)
    shutil.copy2(src, dst)

def copy_tree_filtered(src_root: Path, dst_root: Path):
    for root, dirs, files in os.walk(src_root):
        root_path = Path(root)
        dirs[:] = [d for d in dirs if d not in SKIP_DIRS and not d.startswith(".")]
        for name in files:
            if name.startswith("."):
                continue
            src = root_path / name
            if src.suffix.lower() in INCLUDE_EXTS:
                rel = src.relative_to(src_root)
                if rel.as_posix() in ("README.md", "SUMMARY.md"):
                    continue
                dst = dst_root / rel
                copy_file(src, dst)

def fix_summary_links(summary_path: Path):
    text = summary_path.read_text(encoding="utf-8")
    text = re.sub(r"\((?:\./)?README\.md\)", "(index.md)", text)
    summary_path.write_text(text, encoding="utf-8")

def generate_redirects_from_sitemap(old_sitemap_url: str, out_file: Path):
    if not requests:
        print("requests not installed; skip sitemap fetch")
        return
    try:
        r = requests.get(old_sitemap_url, timeout=20)
        r.raise_for_status()
    except Exception as e:
        print(f"Failed to fetch sitemap: {e}")
        return

    redirects = []
    locs = re.findall(r"<loc>(.*?)</loc>", r.text)
    for loc in locs:
        path = re.sub(r"^https?://[^/]+", "", loc)
        new_path = path
        if not new_path.endswith('/') and '.' not in Path(new_path).name:
            new_path = new_path + ".html"
        redirects.append(f"{path}  {new_path}  301")

    cleaned = sorted(set(redirects))
    ensure_dir(out_file.parent)
    out_file.write_text("\n".join(cleaned) + "\n", encoding="utf-8")
    print(f"Wrote {len(cleaned)} redirects to {out_file}")

def main():
    if len(sys.argv) < 2:
        print("Usage: python scripts/migrate_gitbook_to_mkdocs.py /path/to/eth-infinitism-gitbook [OLD_SITEMAP_URL]")
        sys.exit(1)

    src_root = Path(sys.argv[1]).resolve()
    old_sitemap = sys.argv[2] if len(sys.argv) > 2 else None

    repo_root = Path(".").resolve()
    docs = repo_root / "docs"
    ensure_dir(docs)

    # README.md → docs/index.md
    readme_src = src_root / "README.md"
    if readme_src.exists():
        copy_file(readme_src, docs / "index.md")

    # SUMMARY.md → docs/SUMMARY.md
    summary_src = src_root / "SUMMARY.md"
    if summary_src.exists():
        dst = docs / "SUMMARY.md"
        copy_file(summary_src, dst)
        fix_summary_links(dst)

    # Copy rest of content recursively (filtered)
    copy_tree_filtered(src_root, docs)

    # Optional redirects from sitemap
    if old_sitemap:
        out = docs / "_redirects"
        generate_redirects_from_sitemap(old_sitemap, out)

    print("Migration complete. Next: verify mkdocs.yml and docs/SUMMARY.md, then run `mkdocs serve`.")

if __name__ == "__main__":
    main()
