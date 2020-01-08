def solution(string,markers):
    parts = string.split('\n')   # or string.splitlines()
    for s in markers:
        parts = [v.split(s)[0].rstrip() for v in parts]
    return '\n'.join(parts)