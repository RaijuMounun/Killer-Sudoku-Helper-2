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

    # Kombinasyon tamamlandığında kontrol et
    if len(current_combo) == cage_size_:
        if sum(current_combo) == target_sum:
            all_combos.append(tuple(current_combo))
        return

    # Kombinasyonları oluştur
    for i in range(start, 10):
        # Kısmi toplam kontrolü
        if sum(current_combo) + i > target_sum:
            break  # Toplam hedefi aştı, devam etme
        # Sayıyı kombinasyona ekle
        current_combo.append(i)
        # Rekürsif olarak devam et
        calculate_cage_possibilities(target_sum, cage_size_, i + 1, current_combo, all_combos)
        # Backtracking: Sayıyı kombinasyondan çıkar
        current_combo.pop()

    return all_combos

# Örnek kullanım
CAGE_SUM = 12
CAGE_SIZE = 3
combinations = calculate_cage_possibilities(CAGE_SUM, CAGE_SIZE)

print(f"Kafes Toplamı: {CAGE_SUM}, Kafes Boyutu: {CAGE_SIZE}")
print("Olası Kombinasyonlar:")
for combo in combinations:
    print(combo)
