import pandas as pd
import random
import math

DF_F = pd.read_csv("source/firstnames_fr_2021.csv", sep=",")
DF_L = pd.read_csv("source/lastnames_fr_2000.csv", sep=",")


def get_first_name(sexe=0, annee=(), dpt=(), coeff=1.0, nb=1):
    """
        return a list for first names

        sexe: 1 for men, 2 for women, 0 for both
        annee: tuple of str for the years you want the firstnames occur
            if annee is empty, it checks all the years
        dpt: tuple of str for the french department you want the firstnames occur
            if dpt is empty, it check all departments
        coeff: from 0.0 to 1.0
            if 1.0 the random choices use the real occurrences in data
            if 0.0 every first names have the same chance to be chosen, despite their occurrences in data
        nb: the number of first names to generate
    """
    df_temp = DF_F

    if sexe:
        df_temp = df_temp[df_temp["sexe"] == sexe]

    if annee:
        df_temp = df_temp[df_temp["annais"].isin(annee)]

    if dpt:
        df_temp = df_temp[df_temp["dpt"].isin(dpt)]

    df_temp = df_temp[["preusuel", "nombre"]].groupby(['preusuel'], as_index=False).sum()
    firstn_list = df_temp["preusuel"].tolist()

    if coeff:
        pop = [math.ceil(item * coeff) for item in df_temp["nombre"].tolist()]
        return random.choices(firstn_list, pop, k=nb)
    else:
        return random.choices(firstn_list, k=nb)


def get_last_name(dpt=(), coeff=1.0, nb=1):
    """
        return a list for last names

        dpt: tuple of str for the french department you want the last names occur
            if dpt is empty, it check all departments
        coeff: from 0.0 to 1.0
            if 1.0 the random choices use the real occurrences in data
            if 0.0 every last names have the same chance to be chosen, despite their occurrences in data
        nb: the number of last names to generate
    """
    df_temp = DF_L

    if dpt:
        df_temp = df_temp[df_temp["DEP"].isin(dpt)]

    df_temp = df_temp[["NOM", "NB"]].groupby(['NOM'], as_index=False).sum()
    lastn_list = df_temp["NOM"].tolist()

    if coeff:
        pop = [math.ceil(item * coeff) for item in df_temp["NB"].tolist()]
        return random.choices(lastn_list, pop, k=nb)
    else:
        return random.choices(lastn_list, k=nb)


def main():
    print(get_first_name(sexe=1, annee=("2020", "2021"), nb=5))
    print(get_first_name(sexe=1, annee=("2020", "2021"), coeff=0, nb=5))
    print(get_last_name(dpt=("2A", "2B"), nb=5))


if __name__ == "__main__":
    main()
