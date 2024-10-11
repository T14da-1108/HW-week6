import typing as tp

import pandas as pd


def mean_price(df: pd.DataFrame, tickets: tp.Iterable[str]) -> float:  # type: ignore
    """
    Return mean price for specific tickets list
    :param df: dataframe,
    :param tickets: list of tickets,
    :return: mean fare for this tickets
    """
    pass


def max_size_group(df: pd.DataFrame, columns: list[str]) -> tp.Iterable[tp.Any]:  # type: ignore
    """
    For given set of columns compute most common combination of values of these columns
    :param df: dataframe,
    :param columns: columns for grouping,
    :return: list of most common combination
    """
    pass
