#! /usr/bin/env python
# -*- coding: utf-8 -*-

from open_browser import browser
import time
import pprint
import sys



def get_preparats(browser):
    get_preparats = browser.find_element_by_css_selector('#get_preparat')
    preparats_list = get_preparats.find_elements_by_css_selector('a.lekarstvo')
    return { index: x.text.split('\n') for index, x in enumerate(preparats_list) }



def input_drug_name(search_drug):
    '''
    Ввод поискового слова в строку пойска
    '''
    try:
        elem = browser.find_element_by_css_selector('.input-lg')
        elem.clear()
        elem.send_keys(search_drug)
        browser.find_element_by_css_selector('.btn-info').click()
    except Exception as e:
        print(e.message)
        browser.close()
        exit(1)


def search_all_drug_names(number_of_pagination_page=None):
    '''
    Пойск всех совпавших наименований лекарств по указанному поисковому слову
    number_of_pagination_page - will use in get_list_of_all_prices_for_drug.py
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
            # This feature will use get_list_of_all_prices_for_drug.py script
            if index == number_of_pagination_page:
                return medicaments
            if index < medicamets_paginator_size:
                updated_medicaments_form_paginator[index+2].click()
    except Exception as e:
        print(e.message)
        browser.close()
        exit(1)
    return medicaments


def main():
    search_drug = sys.argv[1]
    print(f'Search for: {search_drug }')
    input_drug_name(search_drug)
    medicaments = search_all_drug_names()

    pprint.pprint(medicaments)
    browser.close()

if __name__ == '__main__':
    main()
