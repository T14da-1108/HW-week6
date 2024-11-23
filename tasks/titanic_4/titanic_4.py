import pandas as pd


def is_lucky(ticket: str) -> bool:
    """
    Determines whether a ticket number is lucky.
    A ticket is lucky if:
    - It is a natural number (contains only digits).
    - It has an even number of digits.
    - The sum of the first half of digits equals the sum of the second half.

    :param ticket: Ticket number as a string
    :return: True if the ticket is lucky, False otherwise
    """
    # Check if the ticket consists of only digits
    if not ticket.isdigit():
        return False

    # Check if the ticket has an even number of digits
    if len(ticket) % 2 != 0:
        return False

    # Split the ticket into two halves
    mid = len(ticket) // 2
    first_half = ticket[:mid]
    second_half = ticket[mid:]

    # Calculate the sums of the digits in both halves
    if sum(map(int, first_half)) == sum(map(int, second_half)):
        return True

    return False


def dead_lucky(df: pd.DataFrame) -> float:
    """
    Compute the ratio of dead passengers with lucky tickets.

    :param df: DataFrame containing Titanic data
    :return: Ratio of dead lucky passengers
    """
    # Apply the is_lucky function to each ticket in the dataset
    df["IsLucky"] = df["Ticket"].apply(is_lucky)

    # Filter for lucky tickets
    lucky_passengers = df[df["IsLucky"]]

    # Calculate the proportion of drowned passengers among lucky ticket holders
    if not lucky_passengers.empty:
        dead_ratio = lucky_passengers["Survived"].value_counts(normalize=True).get(0, 0.0)
        return dead_ratio
    else:
        return 0.0
