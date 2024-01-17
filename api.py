# Позитивные тесты

import json.decoder

import requests


class PetFriends:
    def __init__(self):
        self.base_url = 'https://petfriends.skillfactory.ru'
        """ Метод сохраняет базовый URL сайта дома питомца под названием 'self' """

    def get_api_key(self, email, password):
        """ Метод делает запрос к API сервера и возвращает уникальный ключ пользователя,
        найденного по указанным им email и паролем """

        headers = {
            'email': email,
            'password': password,
        }
        res = requests.get(self.base_url+'/api/key', headers=headers)
        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

    def get_list_of_pets(self, auth_key, filter):
        """ Метод делает запрос к API сервера и возвращает статус запроса и результат со списком
        найденных питомцев, совпадающих с фильтром """
        headers = {'auth_key': auth_key['key']}
        filter = {'filter': filter}

        res = requests.get(self.base_url+'/api/pets', headers=headers, params=filter)

        status = res.status_code
        try:
            result = res.json()
        except:
            result = res.text
        return status, result

  def add_new_pet(self, auth_key: json, name: str, animal_type: str,
                    age: str, pet_photo: str) -> json:
        '''Добавляет информацию о новом питомце'''

        data = {
            'name': name,
            'animal_type': animal_type,
            'age': age,
            'pet_photo': (pet_photo, open(pet_photo, 'rb'), 'image/jpeg')
            }
        headers = {'auth_key'}
        res = requests.post(self.base_url + 'api/pets', headers=headers, data=data)
        status = res.status_code
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        print(result)
        return status, result
# Негативные тесты

  def test_create_pet(auth_key, name=' ', animal_type=' ', age = 2):
    ''' Метод проверяет статус ключа 4хх '''
    _, auth_key = pf.get_api_key(unvalid_email, valid_password)
    my_pet = pf.get_list_of_pets(auth_key, 'my_pet')

    if len(my_pet['pets']) > 0:
        status, result = pf.create_pet_simple(auth_key, my_pet['pets'][0]['id'], name, animal_type, age)

        assert status == 401 or 402 or 403 or 404
        assert result[name] == 'name'
    else:
        raise Exception('Вы не авторизовались')


  def test_succesful_add_new_pet(name=' ', animal_type=' ', age=' ', pet_photo=' '):
    ''' Метод проверяет, что пользователь не смог добавить нового питомца '''
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    assert status == 401 or 402 or 403 or 404
    assert result['name'] == name


  def test_succesful_set_photo(pet_id='pet_id', pet_photo='kitty.jpg'):
    ''' Метод проверяет, что пользователь не смог изменить фотографию питомца '''
    _, auth_key = pf.get_api_key(valid_email, unvalid_password)
    status, result, my_pet = pf.get_list_of_pets(auth_key, pet_id, pet_photo)

    status, _ = pf.set_photo(auth_key, pet_id, pet_photo)

    assert status == 401 or 402 or 403 or 404
    assert my_pet in my_pet.values()
  
