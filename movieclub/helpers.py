from difflib import SequenceMatcher
from collections import Counter

def similar(a, b):
    """Compares two strings for simularities and returns a ratio."""
    return SequenceMatcher(None, a, b).ratio()

def create_counter(values, sample_size_min=3):
    """Creates a collection counter and returns a sorted dictionary with results above the minimum sample size."""
    temp_values = dict(Counter(values))
    # trim results with a low sample size
    temp_values = dict({k: v for k, v in temp_values.items() if v >= sample_size_min})
    return dict(sorted(temp_values.items(), key= lambda item: item[1], reverse=True))
