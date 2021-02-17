#!/usr/bin/env python

"""Tests for `pypackage_test` package."""

import pytest


from pypackage_test import pypackage_test


@pytest.fixture
def response():
    """Sample pytest fixture.

    See more at: http://doc.pytest.org/en/latest/fixture.html
    """
    # import requests
    # return requests.get('https://github.com/audreyr/cookiecutter-pypackage')


def test_read_file():
    """Sample pytest test function with the pytest fixture as an argument."""
    # from bs4 import BeautifulSoup
    test_df = pypackage_test.read_file('tests/test_read_file.txt')
    test_columns= list(test_df.columns)
    assert 'libs' in test_columns
    assert test_df.loc[0][1]==1
