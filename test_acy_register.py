import pytest

from main import Register


@pytest.fixture
def register():
    flow = Register()
    flow.open()
    try:
        yield flow
    finally:
        flow.close()


def test_register_successful(register):
    register.personal_detail()
    register.about_you()
    register.investment()
    register.experience()
    register.terms_and_conditions()

    success_page = register.confirm_id()
    assert success_page.is_displayed()
