#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    num_abs = 0
    if number >= 0:
        num_abs += number
    else:
        num_abs -= number
    return num_abs


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    noms = ""
    for char in prefixes:
        noms += char + suffixe + " "
    return noms


def prime_integer_summation() -> int:
    quant_num = 0
    somme = 0
    i = 1
    num = 2
    while quant_num < 100:
        for i in range(1,)
            if (num % i) ==0:
                num += 1
                break
            else:
                somme += num
                quant_num += 1
                num += 1
    return somme


def factorial(number: int) -> int:
    facto_num = 1
    for i in range(1,number):
        facto_num *= i
    return facto_num


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    return []


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
