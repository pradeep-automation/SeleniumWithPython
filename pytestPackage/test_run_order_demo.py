import pytest

@pytest.mark.run(order=2)
def test_run_order_methodA(one_time_setup, set_up):
    print(f'{"Running method A": ^100}')


@pytest.mark.run(order=1)
def test_run_order_methodB(one_time_setup, set_up):
    print(f'{"Running method B": ^100}')


@pytest.mark.run(order=4)
def test_run_order_methodC(one_time_setup, set_up):
    print(f'{"Running method C": ^100}')


@pytest.mark.run(order=3)
def test_run_order_methodD(one_time_setup, set_up):
    print(f'{"Running method D": ^100}')


@pytest.mark.run(order=6)
def test_run_order_methodE(one_time_setup, set_up):
    print(f'{"Running method E": ^100}')


@pytest.mark.run(order=5)
def test_run_order_methodF(one_time_setup, set_up):
    print(f'{"Running method F": ^100}')
