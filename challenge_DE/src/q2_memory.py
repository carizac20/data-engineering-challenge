import emoji
import json
from typing import List, Tuple
from collections import Counter


def q2_memory(file_path: str) -> List[Tuple[str, int]]:

    emoji_counts = Counter()

    # read line by line to be more memory efficient
    with open(file_path, 'r', encoding='utf-8') as file:
        for line in file:
            content = json.loads(line).get('content', '')

            for emoji_data in emoji.emoji_list(content):
                emoji_char = emoji_data['emoji']
                emoji_counts[emoji_char] += 1

    return emoji_counts.most_common(10)

