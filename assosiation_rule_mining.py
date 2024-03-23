import itertools
def get_all_subsets(set):
    all_subsets = []
    for r in range(1, len(set)):
        subsets = itertools.combinations(set, r)
        all_subsets.extend(subsets)
    return all_subsets

def get_ass_rules(frequent_itemset, minconf):
    assosiation_rules = {}
    for key, value in frequent_itemset.items():
        freq_set = set(key)
        support_of_set = value
        subsets = get_all_subsets(freq_set)
        for subset in subsets:
            subset = tuple(sorted(subset))
            support_of_subset = frequent_itemset.get(subset)
            confidence = support_of_set / support_of_subset
            if confidence >= minconf:
                target = freq_set - set(subset)
                assosiation_rules[subset] = (target, confidence)
    return assosiation_rules