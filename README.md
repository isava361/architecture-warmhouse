# Project_template

Это шаблон для решения проектной работы. Структура этого файла повторяет структуру заданий. Заполняйте его по мере работы над решением.

# Задание 1. Анализ и планирование

<aside>

Чтобы составить документ с описанием текущей архитектуры приложения, можно часть информации взять из описания компании и условия задания. Это нормально.

</aside

### 1. Описание функциональности монолитного приложения

**Управление отоплением:**

- Пользователи могут управлять отоплением в доме
- Система поддерживает изменение текущего состояния устройства через Patch запрос
- Система хранит данные о конфигурации приборов в БД

**Мониторинг температуры:**

- Пользователи могут мониторить температуру в доме через приложение
- Система поддерживает запрос текущей температуры по ID датчика
- Система обеспечивает получение аггрегированных данных по температуре для произвольной локации

**Регистрация датчиков:**

- Датчики регистрируются только сотрудниками компании
- Самостоятельно купленные датчики зарегистрировать нельзя

### 2. Анализ архитектуры монолитного приложения

1. Монолит реализован на Go
2. База данных - PosreSQL
3. Взаимодействие между компонентами реализовано через REST-API
4. Монолит управляет маршрутами внутри приложения исходя из адреса запроса
5. Существует интеграция с внешним API

### 3. Определение доменов и границы контекстов

Домен:
 Управление датчиками
 Контекст: Подключение-отключение датчиков

Домен: Управление отоплением
 Контекст: Включение-выключение отопления

Домен:
 Определение температуры
 	Контекст: Просмотр температуры через веб-интерфейс

### **4. Проблемы монолитного решения**

- Невозможность самостоятельно зарегистрировать устройство, только через выезд сотрудника. В связи с ростом компании на целую область, невозможно подключить всех.
- Сложно добавлять новые типы датчиков, нужно дополнительное тестирование, усложнение решения
- Сложно развертывать, требует остановки всего приложения
- Если произошла ошибка в компоненте, упадет все приложение


### 5. Визуализация контекста системы — диаграмма С4

[Ссылка на диаграмму контекста](https://editor.plantuml.com/uml/TPBBRi8m44Nt-OffLbHgoQQhhb0fQXTGeI3Mo2JJnAhjYUm9Zx_lc01rNojFFFQzTuup2QmyzzPahDaWhAnymYjPX2avnWF3irQDLpRBc3fWWYqnauLQUwnOayko6-qgqzVOUmCjSnSUYyAh_RZHtFRRFg2lefRZSKMsA7MbV4rl6ZiqnVJXVccKu_LYNbWL6BriRQPaEtBnHXUpPKlqWTmeIjr1lfObbtMkTnX0E-0MeINfti5Uj4AC6IqzII1Kh5q3ojKG487HTkWLzrxgrbFVjEdKgklosukV73LqH97DaoEpyswC892SO0Y3VVHD3eQZp6D5RdKgHgTMx7pJYp8BScI4LhI7T_ANz2OcJoSmH1-dcjD1hXQRsO57AtI1V8WcGnKTbfvskXPSjM85v8H5xFrGoKeqPyffM04UJj7-uMh9QVub9bgRCc6OAfROwFZO5t0qFEALs9CURYTtliPwGG7-T_u9kbh-c4y0)



# Задание 2. Проектирование микросервисной архитектуры

В этом задании вам нужно предоставить только диаграммы в модели C4. Мы не просим вас отдельно описывать получившиеся микросервисы и то, как вы определили взаимодействия между компонентами To-Be системы. Если вы правильно подготовите диаграммы C4, они и так это покажут.

**Диаграмма контейнеров (Containers)**

[Диаграмма контейнеров](https://editor.plantuml.com/uml/ZLPDSzem4BtpArHEP8Q6IqyzDO5-JTEMOfWUCy8Me47MkfASXEdqltTNIBQCIGWNIxRslVruk-A3TToukbG39vqIB2jnoxv0ATWKj1DFZiqatnfU3WOEAkQ0hS4vA5aXZSYT13qOl94wLtKXQgFOphdAlfzC37-ytagtgzUr5IOdBEskSoWd2vbpKy0FAIgX9jDtR-UAQxVwVZSfkNN2uAlxAPGLQBAeoBV1N1WBUaHGOpPSuME8pplv82oJchcTO3l0hsFsY5YMt2HA0ufP7r4X7cIEXztEGBtTCLvLmwj1Ta32SlJ9uDcRgaB897vyGIJuO1imdeFu2PiNHKGSDqI8L0d3NMtG3U7oQoG83FUtKEk2cyF8unDyXsjuzNV0y4Sfvr8BC_hCdNZaXp5h5iEmQfp144AS6WlXAyFpFKCNlMF8teNCXBPWldFDjpwBnpqBBrXsj1lwBtv9uHQUpeYjfD98lHtZfeG7N36kYnYyehtrWFOwSbfMSCSPQCQLYbzxRktvPizzddcEKNsZBJdX5vwTsuFEiMuQAupLHZ-u5ru_mbneRYGaCOOthugof3CKY2-p3QPzZvT2YL8uSsXvcbSl4u2M3YYBh37eeT_KRaVfm0Vg7tk5GesmRFHD7785V7zrgL0-2fAd4GK1SMMzB7k44bnbu8aazXMMR4xhi-3Ol6MjlKS8_uZDpSXW9ixhJOEJc-0_mlr8jYzcARNpdUm3EOMVhTiwp6ux9PYXwjRSUlIuziWs97yd_IhdrBJHYhHA5dEmpeZirzqPnYWdJzXewo9VAwLB-Bv7ZkZ7xho8xLkChw5sJOS5acra-TUCeOzFBd3SpB-6UcUjLIRKvksQvcC3Xiad5ZeO1WrLXIRRhLm8TJyBCpaPeJYTRPYlyKpxjHrd6UBYXLC1TZI33KED6g-xnSTiYRPesKx1qzarJSPE4a1YUcAHY1o_56H7SiOHvYLcNuEHLYVDFkeviJ_clEDzsz9jHzFHBylbFEk5-lmGcovMiwwBcDl6yCnOMeW_jR1u7yw2d-tOwKRQjtskkQ8FRPWzXyztoMiCJwgyyjhBqku9FX-5jOgNHpzdFzVKL6JU2trCrV8Aw4wQq4JHNvH7fKGirV5Q2iIHzcJ2PMTXcm6Me2GOBrucSIQbTgsIqqv-fY72G7UGW-hPnviN3pp8ef7pnk2_kqJGdT0nvzseq_zE5-F_BTOMyhrmD40-u77yS_SV)

**Диаграмма компонентов (Components)**

[Диаграмма компонентов](https://editor.plantuml.com/uml/hLTBSzis4BxhLw0woJEEVUcffzYIqsJYP5H9dXuz40bB68402u2IDPtyz-v200a-8AQTwY2-WE_RDtO_6akrhGeniTmAHjO5F9BFgc1ahgHbxvOiEDrfMamcLfN4Ah9Lrgg2v5opp78b9vDVkCn4bRDA2xAtjZI_tTzhUhhRSRkljfLXEaCiQUyoLTolU4PrhhvpLZ9nF__rmr9GQL--FTyNr5YcuTNhN1MbahYZHDacIwQDaZE4kYNJ5xXCuVhCZymGBedTCx9NyFMMd03Be9X8gPKWnccKioFFOB7TQrNjzeIMvVHciZu3OJ7xf67jGra2PAG_l40Ik90tfHq7yYCspVE0U5iJ0LB9DBML1Z6OpUvgWjT7LScSwlFCmIDwYsfwy_U4m0yjJhbaUlOxjUn4pxUalfdwkreMqC2hAS4FpZ4qEn2GqCa5v6r8hcofrJj2VL4RiiHxr6zzsO2wvGuSV5HK4fnakToH4_YGu8O56yHTR6Th9etIYqS7XhTaGItTKiCGFzmxR6ELHjGSNXAwLPK5WN6BmQLBPUnEi_KVpptf3_JjG9qtQ0RAVyL7tE9k73GrPvc1ToN40SG4119ruGbG7QoBaD-ef3iNJbve_u9uWmpQHhCTnnW57MxXeL17r8RAF4I1m6UlqbtWD1TzbIHKY5fXxtGdce_sjcXFCYyLQD8NCNn16J_1-uVb5wSovAbN-JgorwiF_5WPC94nv5djU3QA4_iyGCnNBmkCniNZ-7ONKl2n00lsaLPFwmsP2mxxdF6RiBq0_t3_AoQQT4dPRzxt3jYk_PiYduT6q0HMmf1pSAr9xQwNzQs7vlgNsrfMGwE5OkHI5rucvUWOF2e9rtH7EUCST-dPhm8ParHpTLdZ7yOhWV4hwm8Gyh-Rj7vTbBQ1usSIjy0roETAU4FQ964Sf6qkLsD04bCLmyIN8XHM8F-AqToG3HEiO5P3qTPmObwAriquOPpuNQwVJlqqV9Jz0NqRybwqypuDqdPpClc7SdHSMPSKxQXyv2ukKtkJAlRoCh5mIBrkRlQNj8E-FhS6LdU2A2al-FG4xH5q4pvs8aX_28w4PnDrx0YEC_KncHOkKTrQ1VHIMPBLCogWlT9GI-JCrCWtMXpstDrbL3JsS6Sfxe2J8JkuhgzVBMgEfbmqj5VhX9BSasyQ3mmLYIv5sWt_MvdeKaR-wRFzbqBH9UZuwzeHVmKb2cuke7ao18O3tmB2sGL7q97dq9j3xQyoR9zp0erXMTbq3KbQ0apwLyKCZW2r-_h7MzgGQTcxXMJ4_rUCC9xXrx4ZZuHSwEPtadtGmvqwDxIcdSA39_H3PVVOeSC5ei3D3z3nXWoRVMNdJ2Xwk1bhhDqHZNCL1082KM7SFDMR2QIo_Ctp0ERtwF5gZiVxtAZe207-noGCR4_leLM5jF4JqxePLDPCl7tOuY1Ppoy4Jz2Twr7zI8ReQ2LtShqk_F0QpPemnXe_Y8OrpTTcy5i3BapcBa29UYDWarPGjnAZSKBZ0rpxURDPhWDH2BEE0R6JH1qIzed2336QvZ4sLDneHmRphRjLcHAz_M6sMxf2K8-7hXX6qs4WlzZgfUF-U8OVrUDFjZKgEp2iC9EFiBmgn3y0)


**Диаграмма кода (Code)**

Добавьте одну диаграмму или несколько.

# Задание 3. Разработка ER-диаграммы

[ER-диаграмма](https://editor.plantuml.com/uml/TLJDJjj04BxxAKQS4_NEYGZCZqIJoZ7gqLgy4xBg_bYxQsW4bIXNU8xUgTG_qT9Ni5-XJzBPnU0GWW_PMUURRx_vPjPRpZFhQoKJzq7eYbccG0gDVb4X6Eld9acyy19XgWW8-qOXf1di27P2s2H1JNylOEF8eTq0vg2c0CuJ0C7f1nKJajQAENTcB2_cpCrfFwkbB3HJI75faNda1VF9fvxmq9JC2wCZgUmsFN4ufeXHP5bAtC5JKM9Cup5SbsIDKHJ1S0ZDx-Q--TvyQw-WkMslswls1dGTH0SJYj9m3B1fEfvEiW6CjlEZKHwYlL4ssalXt-KNmYg2XHp9ZkDAllhQXSGitJkOvccMxi0Rc8mF3yPf27PtkoZDiadsp0Q8FCuN3b6ls9AZH8NUBcA1_d7Nr_XGyqELNYWa8QeA0WacokWv15aULOMMH5eSmBnMWXF_02fpHlrxg4dN2aFEAPFB4gObQcQ5YGfSjtcrCyyLiJAqiJVr_K6-lLzCnkJ3DCsBF7txhZiypY9wjD74vczxIMtwsVnelj9wrzuqVzhhvXV15j8m7lqZOlnOsOY_8-njSnywAGT0tVqSNW6UKXL3RWMjGR0hIFwnHFxg78wD5pEnD8iwl5YigtVPxdXfQ3qsV17c3HalPfAT1EfuHUYvk1WEpNa_tDsp2UPCkrLKDylBYAV42xC6KXhjcI3Ou-kEg9-PWAgiuNM9Buvxwcj4SPpHHw6dUedQ1BhPgoITLPqWYoMIxov9jb3pyCtv3m00)

# Задание 4. Создание и документирование API

### 1. Тип API

Для синхронного взаимодействия - REST API.
Почему:
	1. Уже используется в монолите
	2. Простота взаимодействия
 	3. Статус коды и имподентность
Для ассинхронного взаимодействия - Kafka
Почему:
	1. Больше пропускная способность сообщений чем у Rabbit MQ
 	2. Долгое хранение
  	3. Можно подписаться на один топик несколькими консьюмерами

### 2. Документация API

Здесь приложите ссылки на документацию API для микросервисов, которые вы спроектировали в первой части проектной работы. Для документирования используйте Swagger/OpenAPI или AsyncAPI.

# Задание 5. Работа с docker и docker-compose

Перейдите в apps.

Там находится приложение-монолит для работы с датчиками температуры. В README.md описано как запустить решение.

Вам нужно:

1) сделать простое приложение temperature-api на любом удобном для вас языке программирования, которое при запросе /temperature?location= будет отдавать рандомное значение температуры.

Locations - название комнаты, sensorId - идентификатор названия комнаты

```
	// If no location is provided, use a default based on sensor ID
	if location == "" {
		switch sensorID {
		case "1":
			location = "Living Room"
		case "2":
			location = "Bedroom"
		case "3":
			location = "Kitchen"
		default:
			location = "Unknown"
		}
	}

	// If no sensor ID is provided, generate one based on location
	if sensorID == "" {
		switch location {
		case "Living Room":
			sensorID = "1"
		case "Bedroom":
			sensorID = "2"
		case "Kitchen":
			sensorID = "3"
		default:
			sensorID = "0"
		}
	}
```

2) Приложение следует упаковать в Docker и добавить в docker-compose. Порт по умолчанию должен быть 8081

3) Кроме того для smart_home приложения требуется база данных - добавьте в docker-compose файл настройки для запуска postgres с указанием скрипта инициализации ./smart_home/init.sql

Для проверки можно использовать Postman коллекцию smarthome-api.postman_collection.json и вызвать:

- Create Sensor
- Get All Sensors

Должно при каждом вызове отображаться разное значение температуры

Ревьюер будет проверять точно так же.
