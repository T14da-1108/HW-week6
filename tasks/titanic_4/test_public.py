from pathlib import Path

import pandas as pd
import pytest

import testlib
from .titanic_4 import dead_lucky

FILE_PATH = Path(__file__).parent / 'titanic.csv'


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(dead_lucky)


###################
# Tests
###################

@pytest.fixture(scope='function')
def dataframe() -> pd.DataFrame:
    df = pd.read_csv(FILE_PATH, sep='\t')
    yield df


def test_dead_lucky(dataframe: pd.DataFrame) -> None:
    assert dead_lucky(dataframe) == pytest.approx(0.75)
