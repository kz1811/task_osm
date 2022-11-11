

Задание: Написать DDT тесты  API https://nominatim.openstreetmap.org/

Две папки проекта: framework и tests_project.

Тестовые данные содержатся в папке  получаются в формате json, содержащем тестовые данные в виде списка внутри элемента ключа
tests, внутри каждого теста test_data и expected - ожидаемые результаты. Данные передаются в тесты через фикстуры в conftest.

### Для первого запуска:

в файле tests_project/config/config.json:
* прописать пути тестовых данных
* обозначить параметр "identified" как "true" или "false"

Параметр identified определяет, подтверждаются ли запросы электронной почтой. 
При значении "false" со стороны API будут накладываться ограничения, например, на количество запросов (1 в секунду).

Адрес почты прописывается в файле teat_data.py, значение EMAIL.

### Возможности:

* Запросы к /search c дополнительными параметрами, например:
  * q или параметры структурированного запроса (street, city, county, state, country, postalcode) (обязательные)
  * format = [ json | jsonv2 | xml ] -- определяет формат вывода
  * accept-language = < language > -- определяет язык, на котором придет ответ (display_name, например)
  * extratags = [ 0 | 1 ], addressdetails = [ 0 | 1 ], namedetails = [ 0 | 1 ] -- добавляют дополнительные данные в вывод
  * countrycodes = < country_codes,  > -- определяет страны, в рамках которых будет происходить поиск
  * exclude_place_ids = < ids, > -- определяет id, которые не будут выводиться в результате поиска
  * limit = < int > -- задает ограничение на  вывод данных (по умолчанию 10)
  * email -- автоматически подставляется исходя из параметра в конфиге

* Запросы к /reverse c дополнительными параметрами
  * lat, lon -- широта и долгота
  * zoom = [ 1 - 18 ] -- величина, определяющая, насколько масштабный объект необходим (18 - строение, 1 - страна)
  * accept-language
  * email

### Тесты

1. Тест /search:
* Отправить запрос с тестовыми данными на адрес API /search
* Ожидаемый результат:
  * формат ответа соответствует указанному во входном параметре, если он был указан
  * данные ответа соответствуют ожидаемым результатам
2. Тест /reverse:
* Отправить запрос с тестовыми данными на адрес API /reverse
* Ожидаемый результат:
  * формат ответа соответствует указанному во входном параметре, если он был указан
  * данные ответа соответствуют ожидаемым результатам