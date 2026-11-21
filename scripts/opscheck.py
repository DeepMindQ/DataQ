import re
p = '/home/z/my-project/site/src/components/site/OpsConsole.tsx'
t = open(p, encoding='utf-8').read()
print('lines:', t.count('\n'))
# metric card definitions
for m in re.finditer(r'(label|k|title|name)\s*:\s*["\']([^"\']{2,60})["\']', t):
    print(' ', m.group(1), '=', m.group(2))
