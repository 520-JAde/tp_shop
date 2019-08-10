import pytest
from common.base import open_mobile
from common.base import Base


@pytest.fixture ()
def open_m():
    driver = open_mobile ()  # 打开手机
    return driver
