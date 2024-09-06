import math

def hitung_volume_kerucut(diameter, tinggi):
    jari_jari = diameter / 2
    return (1/3) * math.pi * jari_jari ** 2 * tinggi

diameter = 5
tinggi = 4
print("Volume kerucut adalah", hitung_volume_kerucut(diameter, tinggi))
