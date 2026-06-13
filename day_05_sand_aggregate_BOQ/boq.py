def calculate_m20_boq(volume_m3):
    ratio_sum = 1 + 1.5 + 3
    dry_volume = volume_m3 * 1.54
    cement_m3 = (1 / ratio_sum) * dry_volume
    cement_kg = round(cement_m3 * 1440, 1)
    cement_bags = round(cement_kg / 50)
    sand_m3 = (1.5 / ratio_sum) * dry_volume
    sand_kg = round(sand_m3 * 1600, 1)
    agg_m3 = (3 / ratio_sum) * dry_volume
    agg_kg = round(agg_m3 * 1500, 1)
    return cement_bags, sand_kg, agg_kg

volume = 1
cement, sand, aggregate = calculate_m20_boq(volume)
print(f"=== M20 Concrete BOQ for {volume} m³ ===")
print(f"Cement Bags (50kg): {cement} bags")
print(f"Sand Required: {sand} kg")
print(f"Aggregate Required: {aggregate} kg")
print("Standard: IS 456:2000, Mix 1:1.5:3")