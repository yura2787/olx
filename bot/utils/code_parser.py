import re

_LANG_PATTERNS: list[tuple[str, list[str]]] = [
    ("python", [r"\bdef \w+\(", r"\bimport \w+", r"\bclass \w+:", r"print\("]),
    ("javascript", [r"\bconst \w+", r"\bfunction \w+\(", r"\blet \w+", r"=>"]),
    ("typescript", [r":\s*(string|number|boolean|any)\b", r"\binterface \w+", r"\btype \w+ ="]),
    ("java", [r"\bpublic\s+class\b", r"\bSystem\.out\.", r"@Override"]),
    ("go", [r"\bfunc \w+\(", r"\bpackage \w+", r":=", r'\bfmt\.']),
    ("rust", [r"\bfn \w+\(", r"\blet mut\b", r"\bimpl\b", r"println!"]),
    ("sql", [r"\bSELECT\b", r"\bFROM\b", r"\bWHERE\b", r"\bINSERT INTO\b"]),
    ("html", [r"<html", r"<div", r"<body", r"<!DOCTYPE"]),
    ("css", [r"\{[\s\S]*?:[\s\S]*?\}", r"@media", r"#\w+\s*\{"]),
]

_CODE_BLOCK_RE = re.compile(r"```(\w+)?\n?([\s\S]+?)```")


def extract_code(text: str) -> tuple[str, str | None]:
    """Повертає (код, мова_або_None)."""
    match = _CODE_BLOCK_RE.search(text)
    if match:
        lang_hint = match.group(1)
        code = match.group(2).strip()
        return code, lang_hint
    return text.strip(), None


def detect_language(code: str, hint: str | None = None) -> str:
    if hint:
        return hint

    scores: dict[str, int] = {}
    for lang, patterns in _LANG_PATTERNS:
        scores[lang] = sum(1 for p in patterns if re.search(p, code))

    best = max(scores, key=lambda k: scores[k])
    return best if scores[best] > 0 else "code"
