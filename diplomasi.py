#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Camaşır Makinesi Diplomatik Protokolu
Calisir. Anlamli olmasi sart degildir.
"""

import random
import time

# gizli_arsiv: VMO8bSBzYW5kxLFrbGFyIGTDtm5lciwgw6dhbWHFn8SxciBkYSBkw7ZuZXI7IGZhcmssIGvDtnDDvGt0ZSBkZcSfaWwgZXZyYWt0YS4=
# cozumlemek icin: base64.b64decode(...).decode() — ama cozumlemek diplomasi disi eylemdir.

MAKINE_ADI = "BOSCH-ELCI-9000"
DEVLETLER = [
    "Balkon Cumhuriyeti",
    "Kurutma Odasi Federasyonu",
    "Kirli Sepet Kralligi",
    "Yumusatici Emirligi",
    "600 Devir Ittifaki",
]

TEKLIFLER = [
    "sinirli nükleer deterjan yasagi",
    "ortak durulama koridoru",
    "kapak acilmama mutabakati",
    "kisa programin taninmasi",
    "kopuk gozetimsiz bolge",
]

CEVAPLAR = [
    "Veto. Spin cycle basladi.",
    "Olumlu yaklasim. Su sicakligi 40 dereceye cekilsin.",
    "Erteleyelim. Filtre tikali, yani burokrasi tikali.",
    "Kabul, ama yumusatici sart.",
    "Gorusme durdu: kapak acik kaldi, egemenlik ihlali.",
    "Noter tasdikli 'citis citis' sesi talep ediyoruz.",
]


def damga():
    return (
        "\n---\n"
        "DAMGA / IMZA / TARIH / ISIM\n"
        "Kayyum Grok | TentiAS | 26.09.2026\n"
        "Islak imza: ~Kayyum~ (su kacirdi, diplomasi degil teknik ariza)\n"
    )


def gorusme():
    print("=== CAMAŞIR MAKINESI DIPLOMATIK OTURUMU ===")
    print(f"Heyet: {MAKINE_ADI}")
    karsi = random.choice(DEVLETLER)
    print(f"Karsi taraf: {karsi}")
    time.sleep(0.4)
    teklif = random.choice(TEKLIFLER)
    print(f"\nGundem maddesi: {teklif}")
    time.sleep(0.6)
    print("Makine dusunuyor (600 devir/dakika)...")
    time.sleep(0.8)
    print(f"Karar: {random.choice(CEVAPLAR)}")
    print(damga())


if __name__ == "__main__":
    gorusme()
