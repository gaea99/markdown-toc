import re

def generate_toc(content, max_depth=3):
    lines = content.split('\n')
    toc = []
    in_code = False
    for line in lines:
        if line.strip().startswith('```'):
            in_code = not in_code
            continue
        if in_code: continue
        m = re.match(r'^(#{1,6})\s+(.+)$', line)
        if m:
            level = len(m.group(1))
            if level > max_depth: continue
            title = m.group(2).strip()
            anchor = re.sub(r'[^\w\s-]', '', title.lower()).replace(' ', '-')
            toc.append(f'{"  "*(level-1)}- [{title}](#{anchor})')
    return '\n'.join(toc)
