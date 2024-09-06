import math

def hitung_volume_tabung(jari_jari, tinggi):
    return math.pi * jari_jari ** 2 * tinggi

jari_jari = 3
tinggi = 5
print("Volume tabung adalah", hitung_volume_tabung(jari_jari, tinggi))
