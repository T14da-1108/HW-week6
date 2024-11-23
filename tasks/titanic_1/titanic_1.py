import typing as tp
import pandas as pd


def male_age(df: pd.DataFrame) -> float:
    """
    Return mean age of survived men, embarked in Southampton with fare > 30.
    Only considers passengers with known ages.

    :param df: Titanic dataframe
    :return: Mean age of the filtered group
    """
    return (
        df.loc[
            (df["Survived"] == 1) &
            (df["Sex"] == "male") &
            (df["Embarked"] == "S") &
            (df["Fare"] > 30) &
            (df["Age"].notna()),  # Filter out rows where Age is NaN
            "Age",
        ]
        .mean()
    )


def nan_columns(df: pd.DataFrame) -> tp.Iterable[str]:
    """
    Return list of columns containing NaN values.

    :param df: Titanic dataframe
    :return: List of column names with missing data
    """
    return df.columns[df.isna().any()].tolist()
