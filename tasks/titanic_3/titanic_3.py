import typing as tp
import pandas as pd


def mean_price(df: pd.DataFrame, tickets: tp.Iterable[str]) -> float:
    """
    Return mean price for specific tickets list.

    :param df: DataFrame containing Titanic data
    :param tickets: List of ticket numbers
    :return: Mean fare for the specified tickets
    """
    # Filter rows where Ticket is in the provided list
    filtered_fares = df[df['Ticket'].isin(tickets)]['Fare']

    # Calculate and return the mean of the Fare column
    return filtered_fares.mean()


def max_size_group(df: pd.DataFrame, columns: list[str]) -> tp.Iterable[tp.Any]:
    """
    For a given set of columns, compute the most common combination of values of these columns.

    :param df: DataFrame containing Titanic data
    :param columns: List of columns for grouping
    :return: Tuple representing the most common combination of values
    """
    # Group by the specified columns and count the occurrences
    group_counts = df.groupby(columns).size()

    # Find the combination with the maximum size
    max_group = group_counts.idxmax()

    # Return the most common combination as a tuple
    return max_group
