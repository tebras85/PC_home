import pytest

@pytest.fixture
def mask_acc():
    return '**4444'

@pytest.fixture
def mask_acc_zero():
    return "не корректно введены данные!!!"