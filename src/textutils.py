from __future__ import annotations

import re

EMAIL_RE = re.compile(r^[^@s]+@[^@s]+.[^@s]+)


def normalize_email(s: str) -> str:
    s = (s or '').strip().lower()
    return s


def is_valid_email(s: str) -> bool:
    return bool(EMAIL_RE.match((s or '').strip()))
