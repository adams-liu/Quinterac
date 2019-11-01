import pytest

counter = 0

def sum(num1, num2):
    """"It returns sum of two numbers"""
    return num1 + num2


def one(num1):
    """"It returns sum of two numbers"""
    return num1

def test_sum():
    assert sum(1, 2) == 3



def test_one():
    assert one(1) == 1


def test_two():
    assert one(1) == 1

