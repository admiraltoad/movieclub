from difflib import SequenceMatcher

def similar(a, b):
    """Compares two strings for simularities and returns a ratio."""
    return SequenceMatcher(None, a, b).ratio()
