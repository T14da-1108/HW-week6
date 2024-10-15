from pathlib import Path

import numpy as np
import pandas as pd
import pytest

import testlib
from .titanic_1 import male_age, nan_columns

FILE_PATH = Path(__file__).parent / 'titanic.csv'


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(male_age)
    assert testlib.is_function_docstring_exists(nan_columns)


###################
# Tests
###################


@pytest.fixture(scope='function')
def dataframe() -> pd.DataFrame:
    df = pd.read_csv(FILE_PATH, sep='\t')
    yield df


def test_male_age(dataframe: pd.DataFrame) -> None:
    np.testing.assert_allclose(male_age(dataframe), 30.)


def test_nan_columns(dataframe: pd.DataFrame) -> None:
    assert set(nan_columns(dataframe)) == {'Age', 'Cabin', 'Embarked'}
