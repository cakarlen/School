from math import pi, sqrt

def main():
    diameter = float(input("Enter your diameter: "))
    chip_area = float(input("Enter your chip area: "))

    wafer_area = pi * ((diameter / 2) ** 2)
    total_chips = int(diameter * pi * ((diameter / (4 * chip_area)) - (1 / (sqrt(2 * chip_area)))))

    print()
    print("Diameter:", diameter, "\nChip area:", chip_area, "\nChips cut:", total_chips,
          "\nWafer area:", round(wafer_area, 2))



main()