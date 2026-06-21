import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXTENSIONS = {'.md'}
# 简单规则：检测常见项目特化关键词与绝对路径
PATTERNS = [
    r'PEMFC|质子|燃料电池|催化层|nature11115',
    r'[A-Za-z]:\\[^ \n]+',  # 绝对 Windows 路径
    r'\d{4}-\d{2}-\d{2}.*\.(pdf|docx)',  # 项目具体文件名模式，较宽松
]

def iter_files(root):
    for dirpath, _, filenames in os.walk(root):
        for filename in filenames:
            ext = os.path.splitext(filename)[1].lower()
            if ext in EXTENSIONS:
                yield os.path.join(dirpath, filename)

def main():
    issues = []
    for path in iter_files(ROOT):
        try:
            with open(path, 'r', encoding='utf-8') as f:
                lines = f.readlines()
        except Exception as e:
            issues.append((path, 0, f'无法读取文件: {e}'))
            continue
        for idx, line in enumerate(lines, start=1):
            for pattern in PATTERNS:
                if re.search(pattern, line):
                    issues.append((path, idx, line.strip()))
                    break
    if issues:
        print('发现疑似特化内容：')
        for path, idx, text in issues:
            print(f'{path}:{idx}: {text}')
        raise SystemExit(1)
    print('校验通过：未发现明显特化内容。')

if __name__ == '__main__':
    main()
