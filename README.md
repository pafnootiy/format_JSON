# Форматирование файлов фомата .JSON

Скрипт `main_format_json.py` позволяет форматировать файлы формата .json и приводить их к более читаемом у виду

## Как установить

- Для работы со скриптом необходим [Python](https://www.python.org/downloads/) версии 3.7+ и менеджер пакетов `pip`.


## Пример запуска

Запустите скрипт и в увидите в консоли преобразованную базу данных:
```
$ python main_format_json.py  
[
    {
        "active": true,
        "address": "ул. Волкова, д. 92",
        "construction_year": 2010,
        "created_at": "2019-06-16 11:05:08+00:00",
        "description": "Рядом с домом находятся 2 детских сада, детская площадка, магазины продовольственных и прочих товаров, автобусная остановка (автобус идет через город к районной больнице), почта, развлекательный центр. Квартира после капитального ремонта: полы - ламинат, в санузле (раздельный) - плитка, окна - пластиковые стеклопакеты, лоджия застекленная, полностью заменены межкомнатные двери (МДФ), входные (железные утепленные с двойным замком), системы электро- и водоснабжения (в том числе приборы учета энергоресурсов), сантехника, стены и потолки оклеены обоями (на кухне и в туалете - моющимися), в ванной комнате - панели. Окна спальни выходят на запад, кухни и гостиной (в том числе лоджии) - на восток.",
        "floor": "2",
        "has_balcony": true,
        "living_area": null,
        "owner": "Аксенов Трофим Харлампьевич",
        "owners_phonenumber": "+7 701 064 3693",
        "price": 1250000,
        "rooms_number": 2,
        "town": "Никольск",
        "town_district": "Никольский район"
    }
```



## Цель проекта

Код написан в ходе выполнения индивидуального проекта Форматирование JSON.
