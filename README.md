# BugRepro

BugRepro is a small, browser-based Python bug triage demo for a college project. Open `index.html` in a modern browser, add a Gemini API key, upload a small Python project ZIP, and paste a bug description or traceback. An optional terminal screenshot can also be attached.

## What it does

1. Reads Python files from the ZIP in your browser and lists functions and classes using a lightweight source scan.
2. Sends the bug report, optional screenshot, and Python source to Gemini to identify stack frames, likely suspect functions, a possible cause, and a suggested patch.
3. Shows a triage report. The default Foundation MVP does not run generated tests. The optional Advanced Loop uses Pyodide in the browser to try a generated pytest case.

## Run it

No build step is required. Open `index.html` directly or serve this folder with any static web server. Internet access is needed for the CDN libraries and Gemini API. The sample project button loads a small zero-division example.

## Notes

- The Gemini key is held in page memory and is not saved by this demo. Gemini requests include the bug report and uploaded Python source (and screenshot, if attached).
- ZIP uploads are limited to 10 MB, 500 archive entries, and 1 MB/100 Python source files to keep the demo responsive.
- This is a triage aid: review any suggested cause or patch before applying it. MVP reproduction status is explicitly “not run.”
- The browser test runner is a learning/demo sandbox, not a security boundary for running untrusted projects.
