# app/utils.py

def overlap_distance(a: list, b: list) -> int:
    """Calculate number of matching elements at the same position."""
    return sum(1 for x, y in zip(a, b) if x == y)
