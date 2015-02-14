# -*- coding: utf-8 -*-

import pytest

from webdriverwrapper.wrapper import _WebElementWrapper


def test_returns_wrapped_element(driver):
    elm = driver.find_element_by_id('somepage')
    assert isinstance(elm, _WebElementWrapper)


def test_find_by_integer(driver):
    elms = driver.find_elements_by_text(42)
    assert len(elms) == 1


def test_find_by_str(driver):
    assert driver.contains_text('ěščřž')


def test_find_by_unicode(driver):
    # six.u is safe only with ASCII, so I need some hack.
    text = 'ěščřž'
    if hasattr(text, 'decode'):
        text = text.decode('utf8')

    assert driver.find_element_by_text(text)


def test_selenium_not_search(driver):
    elms = driver.find_elements_by_text('text')
    assert len(elms) == 2


def test_wait_for_element(driver):
    assert driver.wait_for_element(id_='somepage')


def test_wait_for_element_fail(driver):
    with pytest.raises(Exception) as excinfo:
        driver.wait_for_element(timeout=0.5, id_='nosuchelement')