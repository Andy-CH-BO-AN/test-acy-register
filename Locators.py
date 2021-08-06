import random

"""
locators definition

select_xxx: dropdown box
input_xxx: input
button_xxx: button
click_xxx: radio button
url_xxx: direct to the url page
title: page title

"""


class PersonalDetail:
    country_list = ['China', 'Taiwan']
    select_language_box = '/html/body/div[1]/div[1]/div[1]/div[2]/div[2]/div[2]/div[1]'
    select_language_name = '//*[@id="gatsby-focus-wrapper"]/div[1]/div[2]/div[2]/div[2]/div[2]/div/*/p[text() = ' \
                           '"English"] '
    select_language_confirm = '/html/body/div[1]/div[1]/div[1]/div[2]/div[3]/a'
    select_account_type_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[1]/div/div '
    select_account_type_personal = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                   '2]/div/div/form/div[1]/div/div/div[2]/div/li[1] '
    select_country_name_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[2]/div/div/div/div/div[1]/div '
    select_country = f'//*[@id="liWrapper"]/*[text()="{random.choice(country_list)}"]'
    select_title_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                       '3]/div/div/div[1] '
    # css selector
    select_title = f'li[data-testid="title{random.randint(0, 4)}"]'
    input_first_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[4]/div/input '
    input_middle_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                        '2]/div/div/form/div[5]/div/input '
    input_last_name = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                      '2]/div/div/form/div[6]/div/input '
    input_email = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                  '7]/div/input '
    select_country_code_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                              '2]/div/div/form/div[8]/div[1]/div/div[1]/div '
    # css selector
    select_country_code = f'li[data-testid="undefined{random.randint(0, 241)}"]'
    input_phone_number = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                         '2]/div/div/form/div[8]/div[1]/div/div[2]/div/div/input '
    button_get_otp_code = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                          '2]/div/div/form/div[8]/div[2]/div/div/div[1]/button '
    input_otp_code = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                     '8]/div[2]/div/div/div[2]/div/div/input '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/button '


class AboutYou:
    select_gender_box = '//*[@id="gatsby-focus-wrapper"]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                        '2]/div/div/form/div[3]/div/div/div[1] '
    # css selector
    select_gender = f'li[data-testid="gender{random.randint(0, 1)}"]'
    select_birth_year_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div[4]/div/div[3]/div '
    # css selector
    select_birth_year = f'li[data-testid="birthyear{random.randint(0, 79)}"]'
    select_birth_month_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                             '2]/div/div/form/div[4]/div/div[2]/div/div/div/div[1] '
    # css selector
    select_birth_month = f'li[data-testid="birthmonth{random.randint(0, 11)}"]'
    select_birth_day_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                           '2]/div/div/form/div[4]/div/div[1]/div/div/div/div[1] '
    # css selector
    select_birth_day = f'li[data-testid="birthday{random.randint(0, 27)}"]'
    input_photo_id_number = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div[5]/div/input '
    input_residential_address = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                '2]/div/div/form/div[6]/div/input '
    input_city = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                 '7]/div/input '
    input_state = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                  '8]/div/input '
    input_zip_code = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/div[' \
                     '9]/div/input '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[10]/button[2] '
    button_back_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[10]/button[1] '


class Investment:
    select_employment_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div[1]/div/div/div[1] '
    # css selector
    select_employment = f'li[data-testid="employment{random.randint(0, 3)}"]'

    select_occupation_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div[2]/div/div/div[1] '
    # css selector
    select_occupation = f'li[data-testid="occupation{random.randint(0, 8)}"]'

    select_industry_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                          '2]/div/div/form/div[3]/div/div/div[1] '
    # css selector
    select_industry = f'li[data-testid="industry{random.randint(0, 18)}"]'

    select_annual_income_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                               '2]/div/div/form/div[4]/div/div/div[1] '
    # css selector
    select_annual_income = f'li[data-testid="annualIncome{random.randint(0, 3)}"]'

    select_total_amount_of_investment_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[' \
                                            '2]/div/div/div[2]/div/div/form/div[5]/div/div/div[1] '
    # css selector
    select_total_amount_of_investment = f'li[data-testid="totalInvestmentsSavings{random.randint(0, 3)}"]'

    select_trading_platform_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                  '2]/div/div/form/div[6]/div/div/div[1] '
    # css selector
    select_trading_platform = f'li[data-testid="platform{random.randint(0, 1)}"]'

    select_funding_currency_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                                  '2]/div/div/form/div[7]/div/div/div[1] '
    # css selector
    select_funding_currency = f'li[data-testid="fundingCurrency{random.randint(0, 6)}"]'

    select_account_types_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                               '2]/div/div/form/div[8]/div/div/div[1] '
    # css selector
    select_account_types = f'li[data-testid="accountType{random.randint(0, 1)}"]'

    url_account_type = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div/div/form/p/a'

    select_leverage_box = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                          '2]/div/div/form/div[9]/div/div/div[1] '
    # css selector
    select_leverage = f'li[data-testid="leverage{random.randint(0, 5)}"]'

    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[10]/button[2] '
    button_back_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/div[10]/button[1] '


class Experience:
    click_first_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[1]/div[1]/fieldset/div/label[{random.randint(1, 3)}] '
    click_second_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                            f'3]/div[1]/div[2]/fieldset/div/label[{random.randint(1, 2)}] '
    click_third_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[1]/div[3]/fieldset/div/label[{random.randint(1, 2)}] '
    click_fourth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                            f'3]/div[1]/div[4]/fieldset/div/label[{random.randint(1, 4)}] '
    click_fifth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[1]/div[5]/fieldset/div/label[{random.randint(1, 2)}] '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                       '3]/div[1]/div[6]/button[2] '
    button_back_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[3]/div[' \
                       '1]/div[6]/button[1] '
    click_sixth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[2]/div[1]/fieldset/div/label[{random.randint(1, 3)}] '
    click_seventh_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                             f'3]/div[2]/div[2]/fieldset/div/label[{random.randint(1, 2)}] '
    # /html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[3]/div[2]/div[3]/fieldset/div/label[1]/span[1]/span[1]/input
    # /html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[3]/div[2]/div[3]/fieldset/div/label[2]/span[1]/span[1]/input
    click_eighth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                            f'3]/div[2]/div[3]/fieldset/div/label[{random.randint(1, 3)}] '
    click_ninth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[2]/div[4]/fieldset/div/label[{random.randint(1, 3)}] '
    click_tenth_question = f'/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                           f'3]/div[2]/div[5]/fieldset/div/label[{random.randint(1, 2)}] '
    button_second_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                              '3]/div[2]/div[6]/button[2] '
    button_second_back_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div/form/div[' \
                              '3]/div[2]/div[6]/button[1] '


class TermsAndConditions:
    title = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[1]/div/h5[1]'

    click_first_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                            '2]/div/form/div[1]/label[1]/span[1]/span[1]/input '
    url_first_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                          '2]/div/form/div[1]/label[1]/span[2]/a '
    click_second_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                             '2]/div/form/div[1]/label[2]/span[1]/span[1]/input '
    url_second_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                           '2]/div/form/div[1]/label[2]/span[2]/a '
    click_third_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                            '2]/div/form/div[1]/label[3]/span[1]/span[1]/input '
    url_third_condition = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                          '2]/div/form/div[1]/label[3]/span[2]/a '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                       '2]/div/form/div[2]/button[2] '
    button_back_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[2]/div[' \
                       '2]/div/form/div[2]/button[1] '


class ConfirmID:
    test_image_path = 'TestImages/ID.jpg'
    content_id_front = '//*[@id="confirmId"]/div/div[1]/div/p'
    upload_id_front = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                      '2]/div/div/form/div/div[1]/div/div[1]/input '
    upload_id_back = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                     '2]/div/div/form/div/div[2]/div/div[1]/input '
    upload_address = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                     '2]/div/div/form/div/div[3]/div/div[1]/input '
    upload_other_document = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                            '2]/div/div/form/div/div[4]/div/div[1]/input '
    button_next_page = '/html/body/div[1]/div[1]/div/div/div[1]/div/div/div/div/div[2]/div/div/div[' \
                       '2]/div/div/form/button '


class ExecuteJavascript:
    scroll_down_the_page = 'window.scrollTo(0, document.body.scrollHeight);'
