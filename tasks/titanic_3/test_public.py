import typing as tp
from pathlib import Path

import numpy as np
import pandas as pd
import pytest

from tools.testlib import testlib
from .titanic_3 import mean_price, max_size_group

FILE_PATH = Path(__file__).parent / 'titanic.csv'


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(mean_price)
    assert testlib.is_function_docstring_exists(max_size_group)


###################
# Tests
###################

@pytest.fixture(scope='function')
def dataframe() -> pd.DataFrame:
    df = pd.read_csv(FILE_PATH, sep='\t')
    yield df


def test_mean_price(dataframe: pd.DataFrame) -> None:
    np.testing.assert_allclose(
        mean_price(dataframe, dataframe['Ticket'].unique()),
        dataframe['Fare'].mean()
    )

    for i, row in dataframe.iterrows():
        np.testing.assert_allclose(mean_price(dataframe, [row['Ticket']]), row['Fare'])

    value = 26.0
    tickets = dataframe[np.isclose(dataframe['Fare'], value)]['Ticket']
    assert mean_price(dataframe, tickets) == pytest.approx(value)


@pytest.mark.parametrize('columns,expected_result', [
    (['Survived', 'Sex'], (0, 'male')),
    (['Survived', 'Sex', 'Cabin'], (0, 'male', 'D26')),
    (['Embarked', 'Pclass'], ('S', 3)),
    (['Age'], (21.00,)),
])
def test_max_size_group(columns: list[str], expected_result: tuple[tp.Any], dataframe: pd.DataFrame) -> None:
    assert max_size_group(dataframe, columns) == expected_result
