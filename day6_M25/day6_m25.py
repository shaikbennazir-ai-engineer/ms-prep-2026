def calculate_boq(volume_m3, grade):
    dry_volume = volume_m3 * 1.54
    if grade == "M20":
        ratio_sum = 5.5  # 1+1+3
    elif grade == "M25":
        ratio_sum = 4.0  # 1+1+2
    else:
        return "grade not supported"

    cement_ratio = 1  # First number in mix ratio
    cement_bags = (dry_volume * cement_ratio / ratio_sum) * 1440 / 50
    return round(cement_bags, 2)

print(calculate_boq(1, "M20"))  # Should print 8.06
print(calculate_boq(1, "M25"))  # Should print 11.0




