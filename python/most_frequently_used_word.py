import re
from collections import Counter


def top_3_words(text):
    return [
        key
        for key, _ in Counter(
            filter(
                lambda x: x != "",
                re.findall(
                    r"(?=.*[a-z])[a-z']+", re.sub(r"[^a-z']", " ", text.lower())
                ),
            )
        ).most_common(3)
    ]
