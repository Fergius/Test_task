import pytest
import requests
from requests.auth import HTTPBasicAuth

url = 'http://rest.test.ivi.ru/v2/character'



def test_reset_collection():
    """
    Сбрасывает коллекцию в первоначальный вид

    Возвращаемого значения нет, так как тест на идентичность результата будет сравниваться с большим json объектом
    """

    character = requests.post("http://rest.test.ivi.ru/v2/reset", auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))


def test_get_one_word_name_1():
    """
    Проверяет отправку запроса с одним словом в параметре name

    Возвращает json объект
    """

    payload = {'name': 'Bastion'}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {
        "result": {
            "education": "Inapplicable",
            "height": 190,
            "identity": "Secret",
            "name": "Bastion",
            "other_aliases": "Template, Sebastion Gilberti, Nimrod, Master Mold",
            "universe": "Marvel Universe",
            "weight": 168.75
        }
    }

def test_get_few_words_name():
    """
    Проверяет отправку запроса с двумя или более словами в параметре name

    Возвращает json объект
    """

    payload = {'name': 'Baron Zemo (Heinrich Zemo)'}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {
        "result": {
            "education": "College graduate",
            "height": 177,
            "identity": "Publicly known",
            "name": "Baron Zemo (Heinrich Zemo)",
            "other_aliases": "Iron Cross, Citizen V, Mark Evanier, Phoenix",
            "universe": "Marvel Universe",
            "weight": 82.35000000000001
        }
    }

def test_character_with_empty_name():
    """
    Проверяет отправку запроса с пустым параметром name

    Возвращает ошибку такого имени нет
    """

    payload = {'name': ''}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"error":"No such name"}

def test_character_with_wrong_name():
    """
    Проверяет отправку запроса с неверно заполненным параметром name

    Возвращает ошибку такого имени нет
    """

    payload = {'name': 'Bastiin'}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"error":"No such name"}

def test_character_changed_case_name():
    """
    Проверяет отправку запроса с неверно введенным регистром в параметре name


    Возвращает ошибку такого имени нет
    """

    payload = {'name': 'BASTION'}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"error":"No such name"}

def test_character_without_plus_in_name():
    """
    Проверяет отправку запроса с двумя словами в параметре name без использования '+'

    Возвращает ошибку такого имени нет
    """

    payload = {'name': 'BaronStrucker'}

    character = requests.get( url, payload,
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"error":"No such name"}

def test_delete_character():
    """
    Проверяет удаление персонажа из базы


    Возвращает, что данный герой удален
    """

    character = requests.delete( 'http://rest.test.ivi.ru/v2/character?name=Selene',
                              auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"result":"Hero Selene is deleted"}

def test_deleting_delete_character():
    """
    Проверка удаления уже удаленного персонажа до этого


    Возвращает ошибку такого имени нет
    """

    character = requests.delete( 'http://rest.test.ivi.ru/v2/character?name=Selene',
                                 auth=HTTPBasicAuth( 'mail@mail.com', 'APZrVp83vFNk5F'))

    assert (character.json()) == {"error":"No such name"}



