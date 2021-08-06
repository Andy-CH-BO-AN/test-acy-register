import random

"""
locators definition

select_xxx : dropdown box
input_xxx : input
button_xxx : button

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
