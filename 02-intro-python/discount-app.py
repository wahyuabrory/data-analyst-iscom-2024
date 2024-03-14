# -*- coding: utf-8 -*-
"""discount-app.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/17fHaYczTYD4_XxfOzkQalA2_N_v_bjke
"""

def calculate_discounted_price(original_price, discount_percentage):
    discounted_price = original_price - (original_price * discount_percentage / 100)
    return discounted_price

def main():
    original_price = int(123000)
    discount_percentage = int(23)

    discounted_price = calculate_discounted_price(original_price, discount_percentage)

    print(f"Harga Asli = Rp. {original_price:,.0f}")
    print(f"Diskon = {discount_percentage}%")
    print(f"Harga setlah diskon {discount_percentage}% discount: Rp.{discounted_price:,.0f}")


if __name__ == "__main__":
    main()