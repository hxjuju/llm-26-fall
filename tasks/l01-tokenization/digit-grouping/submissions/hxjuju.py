import re

PREDICTIONS = {
    "3.14159": ["3", ".", "141", "59"],
    "Room 101": ["Room ", "101"],
    "2024-09-16": ["202", "4", "-", "09", "-", "16"],
}


def solve(text: str) -> list[str]:
    chunks = []
    for run in re.findall(r"\d+|\D+", text):
        if run[0].isdecimal():
            chunks.extend(run[i:i + 3] for i in range(0, len(run), 3))
        else:
            chunks.append(run)
    return chunks


MY_CASES = [
    ("１２３４", ["１２３", "４"]),
    ("007\n\n42", ["007", "\n\n", "42"]),
]
NOTES = """当 k = 1 时，需要 10 个；当 k = 3 时，需要 10 + 100 + 1000 = 1110 个；当 k = 4 时，需要 11110 个。字符串 123456789012 分别需要 12、4 和 3 个 token。较大的分组会缩短序列，但每增加一位数字，词表大约会扩大十倍，而罕见的长分组只有很少的训练样本。预分词上限只限制块长度，如果某个合并从未被学到，BPE 仍可能将 739 这样的块拆成 7 和 39。"""
