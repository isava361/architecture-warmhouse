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
 Управление отоплением и умными устройствами
 	Контекст: Управление датчиками и отоплением внутри дома

Домен: 
 Инсталляция и настройка оборудования
	Контекст: Процесс выезда и подключение датчиков, с привлечением специалиста

Домен:
 Мониторинг и телеметрия
 	Контекст: Сбор, агрегация и анализ данных: температуры, состояния устройств, метрики работы датчиков

Домен:
 Добавление новых домов и поддержка
 	Контекст: Регистрация новых домов и учёт готовности (есть ли в доме датчики/реле), планирование установки, техническая поддержка 

Домен:
 Идентификация и доступ
 	Контекст: Аутентификация/авторизация пользователей и устройств

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

[Диаграмма компонентов](https://editor.plantuml.com/uml/hLXBSzis4BxhLw0-oJEETUcffzYIqsJYP5HJdXuz40bB68402u2oFPtyz-w200cIWkXcueFvMdpx_e3LHsEfjdKfPfPRmKXMmYFvh4f6bafQzch9YjETfkLiPbL5h29RPQqgIS4roorNSZRxZSjSr0MhjI1xQolpnsAXwSlrZjjzlQqDqpbYINkTgtBnm7Eg2_MTiug9nVBt3sj1fNtyThyegR5CmwkdfIeh9N55XRRDramR9US8TKKk7k5o0TTxVcI6S4didf6zWgzNv0Mm39g9AhKIn3YF2dRaEGZRlLRrRazeLLrSph8tK5ZEFscGlQagW8pyXnUe12xaMMcd0_KZDYsAW7ZLAWAaYcbgQmrcC9jVjmgURbKj2whVvWuUqNkgBYx_dH7umuXJBfcU_qajUw5lLwIzkV1thItWWNTJGXvSOcX-862XimkKzo6vifLMhmZrHMt86k_HlwnPWBuL3XnoLDOIacIvt94No2711Ijs4dUrdMTC6gLNjmuCRycAMhgbXY5-k7VOnYgDg0My97IhQWi6unA3ecjbx4wpxA_xaVK7-doWBXiq1-U_uYCkSJSEcfetcKDs9TG1r0GK4dNb2L03hCR8RrJIdIidRxH_GNn0JiP6int76WKVhk2XL4VqXieYL870P-_ITT1f6d-L95I8rc6VT6UQh_Q-QNUog1HuCZOnV44RFy7xc_KNvpBqgNVvFBBtQmnyMni8aJ7aNkruFeaJvpn0B1yULrYDgzlfvQwau6C94HmZFTnb6x8K7DQvu7Tbsm3_SFyVcEZQ9HM_vJWx63lKuC4G9h4w4Reb9DEaLhTYutXXWFxdibwSC4o1Vbopmika7OCGHoHmpdUqC-vgrv3Zli-Pf9ghHiO_JFU-yP9jouUE7xQfbuiQDUXuJwkMA8Fw76btIhksYykohykn2bXYwlAquePsWeGh9KOBGpPCi99P3JIjOOziQEfoMc7SwaDTxsxsD7pKxm5z6pfTz3iz3T9FyxbsJsE0xSt-tMqrK9TkHnXiq7qk2DLngkMd8-awhb_ojzmLVMfjCdwZfay8dehTiF778lsEQhV14zA32atQ2mNp0gSjE9pumemW_PuwKVjTIRCZPDIqksxQk0HrzlYueQrpP7oYSdu2RanRhKCkofrxayIrv-ukfw8BfzlPSGNiK_d1dK77JDRgwAYiKtkMmvJaNlccI-0f0XkgI6Vnbr7OK6MKZx6sdo6neO91ljx9G4EKg3UuWAES8J2g-0CfxAkmFHvv0KG4-rATus6-871ChMhxBlG1mK4zHkm6c30U69BlgTmnj7d4SWcIIyOQalPFpGoEF6s1Z7ifdQfqT8PCDr5XPy8yJK7diQESXsuR4b1I-yaQ6X3nAPa-IVIf-DtAccAO2kGlOhRvJMttE2711IhJpMymSGHEcNzbRxbGz70vDTYu0nFEjL3w24I5SVFiQ2QJol9dhmSmlqUFPrajNkT6TQSGu7_Cmi1yznf6XIQ6UFJFkWXaJ3n_sE8vePqV2PvdTcv6y2CnecEOt5R_jF8_7aIpFdIfyJy419dkQpTuPu0h674P8UgPG4nwJTPhr2u9NGvGzlDciyw2eb3sWm1cdYmIyOdA7Z6wetmSg7ZGYGBcHoUhSYL6wyDilNRKruxdZlwZiWlAcrWz3j8V_uOowSVVR6jKVc38gREF85wNuZy0)

**Диаграмма кода (Code)**

[Диаграмма кода](https://editor.plantuml.com/uml/dLJDRjim3BxxAOHSvhP8i5rzMRt4-HcwPB0Tx5WeDfC8aoL3ajC6GvzeZx1RdwoKOoToawtRVAAfZn-fZwHkjQ7AL0Ntz7ScIgfeGJWJOFOb4AdCLdg66GuaAH17fh80CfGAo8ZH3O8zxntf__FdPPngJPOQ5FdX4NB3ye0ibxEHjQ6WZ0SaCOg9ZNMKY7sGAfzIlNNzwuhpEIt0zMKAg84yD04PeP6o0j2D6V6Cvla8TYm37xCThAl6dsGWg6BIrqZMsFMPa8Qjzxu8oDnQBAE6IN7bFNdD7UxamNL-3z4jxGyr7CaEZdEggh9_frlQxhJXgUtKyqyGLV7yonuMCeUEVfokkWxikQbqIv3KVnsAooeYaJO9WBYeRbcjEDDR7yzIu520KVjQGdY4h3BWqu24sIlrZiZpEnianqABibk3HRFClSsEyWhL67D9pOcvxUARVRcXTL5jSKDKhwD5lHDWGA5WdxKK1tsaY1vBrT9yh7FeID0L1qprIKeELBmra1YxsO3o7K7SAVjhJUeDTQ-qaldU_MSw1khKzVIVQrilREz3ZyX-d_JU3mRNlTC214G-27qHqymrQJ7768kxFiC599F2K8R8nlEAxpGs0IcLpAiCBYS-Ja50SbZZk_OxHWU83-86p4MwJdS2eY03jaDEpuwBku-sSqaqJnOn6k4mNOPfRKx2E9n4Q0m60zi59wvPGniPHvDPaaPnP9k-cD_DvZPaCHutLXJ7oDQ6EtDRf_qsIuVJ-yMyBY6zJwClNqy9Rq7a-Dg_0000)

# Задание 3. Разработка ER-диаграммы

[ER-диаграмма](https://editor.plantuml.com/uml/TLJDJjj04BxxAKQS4_NEYGWCHA99vHZrQ2tU2LbrVwpTDJI2IfGhF4VlLEgVQEahsA_G9-diOd08u4DsTlFDvs--cVMMyypwMid4VH2wOfOfa4AZNrO8nlg5IH8ll4IOAGB2lb48QGOxWXqJDabGqzzBs3XqQ3U0EQWfWBC4G73wGSM4fBLYpfqQoui5SmlQpsif2yqKKbnQP1vvmNpogISyC2NpmkX8AhjDJnnUKyGeigmaxk29A36cyHYk9DLhkTOOHH4CXz3yRkwQxystzXAQc_QglMolGTT1U_2YA0t709kbazaq6y1eEpySvI7Q6sMZlHJ-NNmXh29Oo97iAAvahwzTICpIlV4iJxDq1zx0T78mdgGXsDtjeZJBfjaJDo3oE5yuHBtcJeuI5NgxZ7NwXrrVwdtfzrLweP24g2e899Wee_KGP7bK5LeIQN40Yre9Jlm3gCmfjV6-9bqh33adJAvAc9MecHKcAd3TvjK6FLNKnLq_M1bwsrlyVfnlxnVJ2RaoI_CYJz--wwJ40KMFDbhQ_6qlg6a_cn_DLrfls-lcJtlL_2BOKXh6evj4Z1yh6_6tXBrfxa9VvG2erv_34U09rJJaLj0QvBk2YZcIo5yTpednOYvM1bI7W-LBrQ-Q7syIhKU6ByFq8UF5NBBZG1tl3JtdvyEXEUidldismPngjuxg1dmLyPXuRbw0b4Px9WZsSDmHzHCKK9Krl2xnsUiUknnH7EVqfUYfdgCsWQxxEabdLIV8OedakqkIBTGyV8Z-0m00)

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
	4. Стандарт в индустрии

### 2. Документация API

[REST-API](https://github.com/isava361/architecture-warmhouse/blob/warmhouse/apps/kafka.yaml)
[Kafka](https://github.com/isava361/architecture-warmhouse/blob/warmhouse/apps/swagger.yaml)

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
