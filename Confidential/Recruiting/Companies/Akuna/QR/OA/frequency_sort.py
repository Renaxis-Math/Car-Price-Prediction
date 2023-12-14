def itemSort(items):
    freq_count = Counter(items)
    
    return items.sort(key = lambda x: (freq_counter[x], x))