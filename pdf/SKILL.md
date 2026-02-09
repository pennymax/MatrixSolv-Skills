---
name: pdf
description: >
  Convert PDF files to Markdown for efficient context-window usage. Use this skill
  BEFORE reading any PDF file — it converts PDF to Markdown via Marker (preserving
  LaTeX formulas, tables, and structure) with plain-text fallback. Triggers when:
  (1) User provides a PDF file path to read or analyze,
  (2) Another skill (e.g. paper-reader) needs to parse PDF content,
  (3) User asks to convert PDF to markdown,
  (4) User references a .pdf file in conversation.
  This skill is composable — other skills should call it to get PDF content as markdown.
---

# PDF → Markdown Converter

## Workflow

When a PDF file needs to be read or analyzed:

1. **Check for existing .md**: If `{pdf_stem}.md` exists alongside the PDF, read it directly — skip conversion.

2. **Convert via Marker**: Run the bundled script:
   ```bash
   python {skill_dir}/scripts/pdf2md.py "<pdf_path>" --no-images
   ```
   - Produces `{pdf_stem}.md` in the same directory as the PDF
   - Preserves: LaTeX formulas (`$...$`), Markdown tables, heading structure
   - `--no-images`: skip image extraction (saves time, reduces noise)
   - `--pages 0,5-10`: convert specific pages only (for large PDFs)
   - `--force`: overwrite existing .md
   - Exit code 0 = Marker success

3. **Fallback to TXT**: If Marker fails (exit code 1), the script auto-falls back to `pdftotext` or PyMuPDF.
   - Output: `{pdf_stem}.txt` instead of `.md`
   - **Warn the user**: "PDF was converted to plain text — formulas and tables may be lost."

4. **Read the result**: Use the Read tool on the generated `.md` (or `.txt`) file.

## Composability with Other Skills

Other skills (e.g. `paper-reader`) should use this skill as a preprocessing step:

```
1. Receive PDF path from user
2. Invoke pdf skill → get .md path
3. Read .md file
4. Proceed with skill-specific analysis
```

## Options Reference

| Flag | Effect |
|------|--------|
| `--no-images` | Skip image extraction (default for context efficiency) |
| `--pages 0,5-10` | Convert only specified pages |
| `--force` | Overwrite existing .md |
| `-o path` | Custom output path |

## Notes

- First run of Marker loads ML models (~60s warmup). Subsequent runs are faster.
- For very large PDFs (>50 pages), use `--pages` to convert sections incrementally.
- If Marker consistently times out, the TXT fallback is automatic — no manual intervention needed.
