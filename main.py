class SortUnits:
    @staticmethod
    def sort(width, height, length, mass):
        volume = width * height * length
        is_bulky = volume > 1_000_000 or max(width, height, length) >= 150
        is_heavy = mass >= 20

        return "REJECTED" if is_bulky and is_heavy else "SPECIAL" if is_bulky or is_heavy else "STANDARD"
