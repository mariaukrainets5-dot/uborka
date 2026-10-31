#!/usr/bin/env python3
"""Wraps index.html (Artifact format, no document tags) into docs/index.html for GitHub Pages."""
from pathlib import Path

HEAD = """<!doctype html>
<html lang="ru">
<head>
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<meta name="description" content="Убери дом красиво, пока не прилетела злая ведьма Камчильда.">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-title" content="Гладильда">
<meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
<meta name="theme-color" content="#241433">
"""
root = Path(__file__).parent
page = (root / "index.html").read_text(encoding="utf-8")
head, body = page.split('<canvas id="cv"', 1)
(root / "docs").mkdir(exist_ok=True)
(root / "docs" / "index.html").write_text(
    HEAD + head + '</head>\n<body>\n<canvas id="cv"' + body + "</body>\n</html>\n", encoding="utf-8"
)
