#!/usr/bin/env python3
"""PDF → Markdown converter using Marker, with TXT fallback.

Usage:
    python pdf2md.py <input.pdf> [--output <output.md>] [--pages 0,5-10]
                                 [--no-images] [--force]

Exit codes: 0=marker success, 1=fallback to txt, 2=total failure
"""
import argparse
import subprocess
import sys
import tempfile
from pathlib import Path


def convert_with_marker(pdf: Path, output: Path, *,
                        pages: str | None = None,
                        no_images: bool = False,
                        timeout: int = 600) -> bool:
    """Run marker_single, return True on success."""
    cmd = ["marker_single", str(pdf)]
    if pages:
        cmd += ["--page_range", pages]
    if no_images:
        cmd += ["--disable_image_extraction"]

    with tempfile.TemporaryDirectory() as tmpdir:
        cmd += ["--output_dir", tmpdir]
        try:
            r = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        except FileNotFoundError:
            print("ERROR: marker_single not found", file=sys.stderr)
            return False
        except subprocess.TimeoutExpired:
            print(f"ERROR: marker_single timed out ({timeout}s)", file=sys.stderr)
            return False

        if r.returncode != 0:
            print(f"ERROR: marker_single exit {r.returncode}", file=sys.stderr)
            if r.stderr:
                print(r.stderr[:500], file=sys.stderr)
            return False

        # marker outputs to tmpdir/<stem>/<stem>.md
        md_files = list(Path(tmpdir).rglob("*.md"))
        if not md_files:
            print("ERROR: marker produced no .md output", file=sys.stderr)
            return False

        md_content = md_files[0].read_text(encoding="utf-8")
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(md_content, encoding="utf-8")
    return True


def convert_with_pdftotext(pdf: Path, output: Path) -> bool:
    """Fallback: extract plain text via pdftotext or Python."""
    # Try pdftotext (poppler)
    try:
        r = subprocess.run(["pdftotext", "-layout", str(pdf), "-"],
                           capture_output=True, text=True, timeout=60)
        if r.returncode == 0 and r.stdout.strip():
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(r.stdout, encoding="utf-8")
            return True
    except (FileNotFoundError, subprocess.TimeoutExpired):
        pass

    # Try PyMuPDF
    try:
        import fitz  # type: ignore
        doc = fitz.open(str(pdf))
        text = "\n\n".join(page.get_text() for page in doc)
        doc.close()
        if text.strip():
            output.parent.mkdir(parents=True, exist_ok=True)
            output.write_text(text, encoding="utf-8")
            return True
    except ImportError:
        pass

    return False


def main():
    parser = argparse.ArgumentParser(description="PDF → Markdown (Marker + TXT fallback)")
    parser.add_argument("pdf", help="Input PDF path")
    parser.add_argument("--output", "-o", help="Output path (default: same dir, .md extension)")
    parser.add_argument("--pages", help="Page range, e.g. '0,5-10,20'")
    parser.add_argument("--no-images", action="store_true", help="Skip image extraction")
    parser.add_argument("--force", action="store_true", help="Overwrite existing output")
    args = parser.parse_args()

    pdf = Path(args.pdf).resolve()
    if not pdf.exists():
        print(f"ERROR: {pdf} not found", file=sys.stderr)
        sys.exit(2)

    output = Path(args.output) if args.output else pdf.with_suffix(".md")
    output = output.resolve()

    if output.exists() and not args.force:
        print(f"OK: {output} already exists (use --force to overwrite)")
        sys.exit(0)

    # Try Marker first
    print(f"Converting: {pdf.name} → {output.name}")
    if convert_with_marker(pdf, output, pages=args.pages, no_images=args.no_images):
        lines = output.read_text().count("\n")
        print(f"OK: Marker success ({lines} lines)")
        sys.exit(0)

    # Fallback to TXT
    print("WARN: Marker failed, falling back to plain text extraction", file=sys.stderr)
    txt_output = output.with_suffix(".txt") if output.suffix == ".md" else output
    if convert_with_pdftotext(pdf, txt_output):
        lines = txt_output.read_text().count("\n")
        print(f"OK: TXT fallback ({lines} lines) → {txt_output.name}")
        print("WARN: Plain text lacks formulas/tables. Consider fixing Marker.", file=sys.stderr)
        sys.exit(1)

    print("ERROR: All conversion methods failed", file=sys.stderr)
    sys.exit(2)


if __name__ == "__main__":
    main()
