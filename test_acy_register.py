import pytest
import main


class TestRegister:
    def test_register_successful(self):
        main.Register().main()
        main.Register().personal_detail()
        main.Register().about_you()
        main.Register().investment()
        main.Register().experience()
        main.Register().terms_and_conditions()
        main.Register().confirm_id()
