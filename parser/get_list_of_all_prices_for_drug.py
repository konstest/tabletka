#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import pprint
import sys
import argparse



#def get_prices_by_apteki(browser):
##    prices_by_apteki = browser.find_element_by_css_selector('#get_preparat')
#    prices_by_apteki = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div[3]')
##    prices_by_apteki = browser.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[1]/div[3]/div[1]')
#
##    prices_list = prices_by_apteki.find_elements_by_css_selector('a.lekarstvo')
#    return { index: x.text.split('\n') for index, x in enumerate(prices_by_apteki) }


def parse_args():
    '''
    python3 tabletka/get_list_of_all_prices_for_drug.py \
        --number_of_pagination_page 0 \
        --position_in_drugs_form 6 \
        --drug_name ['МИРАМИСТИН','ЛЕК. ФОРМА:ФЛАКОН','КОЛИЧЕСТВО И ДОЗИРОВКА: 0,01% - 500 МЛ']
    '''
    parser = argparse.ArgumentParser()
    parser.add_argument('-n', '--number_of_pagination_page',
                        dest='number_of_pagination_page',
                        type=int,
                        required=True,
                        help='1 .. 8')
    parser.add_argument('-p', '--position_in_drugs_form',
                        dest='position_in_drugs_form',
                        type=int,
                        required=True,
                        default=1,
                        help='1 .. xxx')
    drug_help = f"['NAME OF DRUG','LEK. FORMA:FLAKON','COUNT AND DOZA: 0,01 - 500 ML']"
    parser.add_argument('-d', '--drug_name',
                        dest='drug_name',
                        type=str,
                        required=True,
                        default=drug_help,
                        help=drug_help)
    args = parser.parse_args()
    return args




'''
Ввод поискового слова в строку пойска
'''
try:
    args = parse_args()
    print(f'Args:\n\t{args}')
    exit()
    from open_browser import browser
    elem = browser.find_element_by_css_selector('.input-lg')
    elem.clear()
    elem.send_keys(search_drug)
    browser.find_element_by_css_selector('.btn-info').click()
except Exception as e:
    print(e.message)
    browser.close()
    exit(1)



'''
Пойск всех совпавших наименований лекарств с указанным поисковым словом
'''
try:
    medicaments_form_paginator_xpath = '/html/body/div[3]/div/div[1]/div[2]/ul/li/a'
    # Попытка 0(Обход кнопок пагинатора в цикле):
    medicaments = {}
    medicaments_form_paginator = browser.find_elements_by_xpath(medicaments_form_paginator_xpath)
    medicamets_paginator_size = len(medicaments_form_paginator[1:-1])
    i = 1
    for index in range(medicamets_paginator_size):
        medicaments.update({index+1: get_preparats(browser)})
        updated_medicaments_form_paginator = browser.find_elements_by_xpath(medicaments_form_paginator_xpath)
        if index < medicamets_paginator_size:
            updated_medicaments_form_paginator[index+2].click()
except Exception as e:
    print(e.message)
    browser.close()
    exit(1)


pprint.pprint(medicaments)
browser.close()
