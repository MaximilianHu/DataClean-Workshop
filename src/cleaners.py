def trim_lines(lines):
    return [ (s or '').strip() for s in lines ]


def unique_lines(lines):
    seen = set()
    out = []
    for s in lines:
        if s not in seen:
            seen.add(s)
            out.append(s)
    return out
