#!/usr/bin/env python

"""Tests for `pypackage_test` package."""

import pytest


from pypackage_test import pypackage_test


@pytest.fixture
def read_file_ex(tmpdir):
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    file = tmpdir.join('test_read_file.txt')
    with open(file,'w') as f: 
        f.write("libs;version\n\tlib1;1\n")
    yield file

def test_read_file(read_file_ex):
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    test_df = pypackage_test.read_file(read_file_ex)
    test_columns= list(test_df.columns)
    assert 'libs' in test_columns
    assert test_df.loc[0][1]==1
