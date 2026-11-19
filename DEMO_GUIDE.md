# BugRepro demo run sheet

## Before presenting

1. Open `index.html` in Chrome or another modern browser.
2. Add your Gemini API key in the key field. It is used in page memory and is not included in the demo ZIP.
3. Upload `demo/billing-bug-project.zip` (the intentionally buggy version).
4. Paste the report and traceback from `demo/BUG_REPORT.md`.
5. Leave **Foundation MVP** selected and click **Run Bug Triage**.

## Explain the result

- The app reads the ZIP locally and indexes Python functions/classes.
- Gemini receives the traceback and Python source and returns likely stack frames, suspect code, a root-cause explanation, and a suggested diff.
- Foundation MVP does not execute generated tests, so reproduction status is **not run**.
- The suspected defect is division by zero when the participant count is zero.
- For the fixed version, see `demo/billing-bug-project-fixed.zip`. Its `calculate_split` function raises a clear `ValueError` before division.

## Demo files

- `demo/billing-bug-project.zip`: intentionally buggy project to upload.
- `demo/billing-bug-project-fixed.zip`: corrected project copy.
- `demo/BUG_REPORT.md`: report and traceback to paste.
