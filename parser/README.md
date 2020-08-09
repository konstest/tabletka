# TABLETKA.TOMSK.RU python parser
### Docker command for starting selenium worker:
`docker run -d --rm -h tabletka --name tabletka --dns=127.0.0.1 --add-host=tabletka.online:78.140.7.18 -e VNC_NO_PASSWORD=1 -p 4444:4444 -p 5911:5900 -v /dev/shm:/dev/shm selenium/standalone-firefox-debug:3.14`
### VNCviewer to show how brower works:
`vncviewer localhost:5911`
### Getting all medicaments by name:
`python3 get_list_of_medicaments.py мирамистин`
### Getting all the prices and addresses for specific drag:
`python3 get_list_of_all_prices_for_drug.py --number_of_pagination_page 0 --position_in_drugs_form 6 --drug_name ['МИРАМИСТИН','ЛЕК. ФОРМА:ФЛАКОН','КОЛИЧЕСТВО И ДОЗИРОВКА: 0,01% - 500 МЛ']`
