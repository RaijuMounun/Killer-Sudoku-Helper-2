""" Logic module for killer sudoku helper """

def calculate_cage_possibilities(
    target_sum,
    cage_size_,
    start=1,
    current_combo=None,
    all_combos=None):
    """ Main recursive calculation function. Takes the cage sum and cage size. """

    if current_combo is None:
        current_combo = []
    if all_combos is None:
        all_combos = []

    # Combination is complete
    if len(current_combo) == int(cage_size_):
        if sum(current_combo) == int(target_sum):
            all_combos.append(tuple(current_combo))
        return

    # Make the combinations
    for i in range(start, 10):
        if sum(current_combo) + i > int(target_sum):
            break
        current_combo.append(i)
        calculate_cage_possibilities(target_sum, cage_size_, i + 1, current_combo, all_combos)
        # Backtracking: remove the last element
        current_combo.pop()

    return all_combos
