from typing import List

CRISIS_KEYWORDS = List[str] = [
    "suicidal","sucide","kill myself"
]

SAFETY_MESSAGE = (
    ""
)
def contains_crisis_keywords(text:str)->bool:

    text_lower = text.lower()
    return any(keyword in text_lower for keyword in CRISIS_KEYWORDS)