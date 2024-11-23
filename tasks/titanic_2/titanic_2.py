import pandas as pd


def class_distribution(df: pd.DataFrame) -> pd.Series:
    """
    Return Pclass distribution.
    :param df: Titanic dataframe
    :return: Series with class ratios, sorted by class ascending.
    """
    # Calculate the proportion of passengers in each class
    class_counts = df["Pclass"].value_counts(normalize=True).sort_index()
    return class_counts


def families_count(df: pd.DataFrame, k: int) -> int:
    """
    Compute the number of families with more than k members.
    A family is defined as a group of passengers with the same surname.
    The surname is extracted as the part of the Name field before the first comma.

    :param df: Titanic dataframe
    :param k: Minimum number of family members
    :return: Number of families with more than k members
    """
    # Extract surname from the Name column
    df["Surname"] = df["Name"].str.split(",").str[0]

    # Count passengers in each family
    family_sizes = df["Surname"].value_counts()

    # Count families with more than k members
    families_with_k_members = (family_sizes > k).sum()

    return families_with_k_members
