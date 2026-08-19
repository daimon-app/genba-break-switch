#!/usr/bin/env python3
"""Static QA for the Kirikae Switch free public beta."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from urllib.parse import unquote, urlparse

ROOT = Path(__file__).resolve().parents[2]
OUTPUT = ROOT / "docs" / "qa" / "2026-08-19_sales_ready_static_result.json"

HTML_FILES = [
    "index.html",
    "start.html",
    "faq.html",
    "install.html",
    "terms.html",
    "privacy.html",
    "commerce.html",
    "support.html",
]
REQUIRED_FILES = HTML_FILES + ["site.css", "manifest.json", "service-worker.js"]
EXPECTED_CACHE = [
    "./",
    "./index.html",
    "./start.html",
    "./faq.html",
    "./install.html",
    "./terms.html",
    "./privacy.html",
    "./commerce.html",
    "./support.html",
    "./site.css",
    "./manifest.json",
    "./icons/icon-192.png",
    "./icons/icon-512.png",
]


def result(case_id: str, status: str, detail: str) -> dict[str, str]:
    return {"id": case_id, "status": status, "detail": detail}


def local_target(href: str) -> str | None:
    href = unquote(href.strip())
    if not href or href.startswith(("#", "mailto:", "tel:", "data:", "javascript:")):
        return None
    parsed = urlparse(href)
    if parsed.scheme or parsed.netloc:
        return None
    target = parsed.path or "index.html"
    return target.lstrip("/")


def main() -> int:
    results: list[dict[str, str]] = []
    failures = 0

    missing = [file for file in REQUIRED_FILES if not (ROOT / file).is_file()]
    if missing:
        results.append(result("Q-01", "FAIL", f"Required files missing: {', '.join(missing)}"))
        failures += 1
    else:
        results.append(result("Q-01", "PASS", "All required HTML, CSS, manifest, and service-worker files exist."))

    try:
        manifest = json.loads((ROOT / "manifest.json").read_text(encoding="utf-8"))
        name_ok = manifest.get("name") == "切り替えスイッチ" and manifest.get("short_name") == "切り替え"
        index_text = (ROOT / "index.html").read_text(encoding="utf-8")
        brand_ok = name_ok and "<title>切り替えスイッチ</title>" in index_text and 'apple-mobile-web-app-title" content="切り替えスイッチ"' in index_text
        if brand_ok:
            results.append(result("Q-02", "PASS", "title, Apple Web App title, manifest name, and manifest short_name are aligned."))
        else:
            results.append(result("Q-02", "FAIL", "Public brand identifiers are not fully aligned."))
            failures += 1
    except (OSError, json.JSONDecodeError) as exc:
        results.append(result("Q-02", "FAIL", f"Manifest cannot be parsed: {exc}"))
        failures += 1

    page_texts: dict[str, str] = {}
    link_errors: list[str] = []
    for file in HTML_FILES:
        text = (ROOT / file).read_text(encoding="utf-8")
        page_texts[file] = text
        for href in re.findall(r'''\bhref=["']([^"']+)["']''', text, re.IGNORECASE):
            target = local_target(href)
            if target and not (ROOT / target).is_file():
                link_errors.append(f"{file} -> {href}")
    if link_errors:
        results.append(result("Q-04", "FAIL", "Broken local links: " + "; ".join(link_errors)))
        failures += 1
    else:
        results.append(result("Q-04", "PASS", "All local links in public HTML pages resolve to existing files."))

    start_ok = 'href="index.html">無料で試す' in page_texts["start.html"] and "FREE PUBLIC BETA" in page_texts["start.html"]
    no_form = not any(re.search(r"<form\b", text, re.IGNORECASE) for text in page_texts.values())
    commerce_ok = "現在、購入できる有償商品はありません。" in page_texts["commerce.html"]
    if start_ok and no_form and commerce_ok:
        results.append(result("Q-03/Q-12", "PASS", "Free-beta LP links to the app; no local form is present; commerce page states that paid sales are not active."))
    else:
        detail = f"start_ok={start_ok}; no_local_form={no_form}; commerce_status={commerce_ok}"
        results.append(result("Q-03/Q-12", "FAIL", detail))
        failures += 1

    prohibited_promises = [
        "OSアラームを提供します",
        "必ず通知します",
        "バックグラウンドでも鳴ります",
        "熱中症を防ぎます",
        "安全を保証します",
        "集中力を回復します",
        "ストレスを治します",
    ]
    offending = []
    for phrase in prohibited_promises:
        sources = [file for file, text in page_texts.items() if phrase in text]
        if sources:
            offending.append(f"{phrase} ({', '.join(sources)})")
    required_limits = [
        "端末標準のタイマー／アラームを併用してください",
        "安全管理や体調判断は、代わりません。",
        "現在は無料公開ベータです。",
    ]
    missing_limits = [phrase for phrase in required_limits if not any(phrase in text for text in page_texts.values())]
    if not offending and not missing_limits:
        results.append(result("Q-05", "PASS", "No prohibited implementation promises found; key limitations are displayed."))
    else:
        results.append(result("Q-05", "FAIL", f"Offending={offending}; missing_limitations={missing_limits}"))
        failures += 1

    sw_text = (ROOT / "service-worker.js").read_text(encoding="utf-8")
    missing_cache = []
    for asset in EXPECTED_CACHE:
        if asset not in sw_text:
            missing_cache.append(asset)
        elif asset != "./":
            normalized = asset.removeprefix("./")
            if not (ROOT / normalized).is_file():
                missing_cache.append(f"{asset} (missing file)")
    no_push = all(token not in sw_text and token not in page_texts["index.html"] for token in ["PushManager", "showNotification", "Notification.requestPermission"])
    if not missing_cache and "kirikae-v9" in sw_text and no_push:
        results.append(result("Q-06", "PASS", "Service worker cache includes public pages and core assets; no unimplemented push API is claimed by code."))
    else:
        results.append(result("Q-06", "FAIL", f"missing_cache={missing_cache}; cache_version={'kirikae-v9' in sw_text}; no_push_api={no_push}"))
        failures += 1

    home_links_ok = 'href="start.html">使い方・無料公開ベータ' in page_texts["index.html"] and 'href="faq.html">FAQ・安全上の注意' in page_texts["index.html"]
    if home_links_ok:
        results.append(result("Q-07", "PASS", "PWA home contains direct links to the LP and FAQ/safety guidance."))
    else:
        results.append(result("Q-07", "FAIL", "PWA home is missing required LP or FAQ guidance links."))
        failures += 1

    privacy_required = ["GitHub Pages", "IPアドレス", "ローカルストレージ", "GitHub Issues"]
    privacy_missing = [phrase for phrase in privacy_required if phrase not in page_texts["privacy.html"]]
    if not privacy_missing:
        results.append(result("Q-04-Privacy", "PASS", "Privacy page documents local storage, GitHub Pages, IP logging, and public Issues."))
    else:
        results.append(result("Q-04-Privacy", "FAIL", f"Missing privacy disclosures: {privacy_missing}"))
        failures += 1

    overall = "PASS" if failures == 0 else "FAIL"
    payload = {
        "scope": "static QA only; browser and mobile device checks are recorded separately",
        "overall": overall,
        "failure_count": failures,
        "results": results,
    }
    OUTPUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if failures == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
