#!/usr/bin/env python3
import re, ast
src = open('scripts/gen_svc/t8_quantum.py').read()
lines = src.split('\n')
out = []
for ln in lines:
    s = ln.strip()
    if s.startswith('p="') and s.endswith('",'):
        indent = ln[:len(ln) - len(ln.lstrip())]
        body = s[len('p="'):-2]  # strip p=" and trailing ",
        out.append(f'{indent}p("{body}"),')
    elif s.startswith('p="') and s.endswith('"'):
        indent = ln[:len(ln) - len(ln.lstrip())]
        body = s[len('p="'):-1]
        out.append(f'{indent}p("{body}"),')
    else:
        out.append(ln)
src = '\n'.join(out)
open('scripts/gen_svc/t8_quantum.py', 'w').write(src)
try:
    ast.parse(src)
    print('SYNTAX OK')
except SyntaxError as e:
    print('ERR', e.lineno, e.msg)
