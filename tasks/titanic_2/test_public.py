from pathlib import Path

import pandas as pd
import pytest
from pandas.testing import assert_series_equal

import testlib
from .titanic_2 import class_distribution, families_count

FILE_PATH = Path(__file__).parent / 'titanic.csv'


###################
# Structure asserts
###################

def test_docs() -> None:
    assert testlib.is_function_docstring_exists(class_distribution)
    assert testlib.is_function_docstring_exists(families_count)


###################
# Tests
###################

@pytest.fixture(scope='function')
def dataframe() -> pd.DataFrame:
    df = pd.read_csv(FILE_PATH, sep='\t')
    yield df


def test_class_distribution(dataframe: pd.DataFrame) -> None:
    class_distr_ans = pd.Series(data=[0.192308, 0.192308, 0.615385], index=[1, 2, 3], name='Pclass')
    assert_series_equal(class_distribution(dataframe).sort_index(), class_distr_ans,
                        check_index_type=False, check_names=False)  # added for new Pandas stuff


@pytest.mark.parametrize('count_members,count_families', [
    (0, 141),
    (1, 13),
    (2, 1),
    (3, 1),
    (4, 0),
])
def test_families_count(count_members: int, count_families: int, dataframe: pd.DataFrame) -> None:
    assert families_count(dataframe, count_members) == count_families
