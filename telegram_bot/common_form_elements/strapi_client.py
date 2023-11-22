import logging
import os
from aiogram import types
import requests


class StrapiClient:
    TOKEN = os.getenv("STRAPI_TOKEN")
    HOST = os.getenv("STRAPI_HOST")
    CLIENTS_URL = "api/clients"
    JSON_INPUTS_URL = "api/json-inputs"

    def __init__(self, token=None, host=None):
        self.logger = logging.getLogger("StrapiClient")
        self.logger.setLevel(logging.INFO)
        self.TOKEN = token if token is not None else os.getenv("STRAPI_TOKEN")
        self.HOST = host if host is not None else os.getenv("STRAPI_HOST")

    def __send_post_request(self, url: str, data: dict, headers: dict | None = None):
        if headers is None:
            headers = {"Authorization": f"Bearer {self.TOKEN}"}
        else:
            headers.update({"Authorization": f"Bearer {self.TOKEN}"})
        return requests.post(
            url=url,
            json=data,
            headers=headers
        )

    def __send_put_request(self, url: str, data: dict, headers: dict | None = None):
        if headers is None:
            headers = {"Authorization": f"Bearer {self.TOKEN}"}
        else:
            headers.update({"Authorization": f"Bearer {self.TOKEN}"})
        return requests.put(
            url=url,
            json=data,
            headers=headers
        )

    def __send_get_request(self, url: str, headers: dict | None = None):
        if headers is None:
            headers = {"Authorization": f"Bearer {self.TOKEN}"}
        else:
            headers.update({"Authorization": f"Bearer {self.TOKEN}"})
        return requests.get(
            url=url,
            headers=headers
        )

    @staticmethod
    def __get_client_data_from_message(message: types.Message):
        return {
            "data": {
                "tg_id": message.from_user.id,
                "tg_username": message.from_user.username,
                "firstname": message.from_user.first_name if message.from_user.first_name is not None else "",
                "lastname": message.from_user.last_name if message.from_user.last_name is not None else "",
                "tg_language_code": message.from_user.language_code if message.from_user.language_code is not None else "",
            }
        }

    def save_client_to_strapi(self, message: types.Message):
        try:
            url = self.HOST + self.CLIENTS_URL
            data = self.__get_client_data_from_message(message)
            result = self.__send_post_request(url, data)
            if result.status_code != 200:
                response_string = str(result.content, encoding="utf-8")
                if "This attribute must be unique" not in response_string:
                    raise Exception(response_string)
            return result
        except Exception as e:
            self.logger.error(f"Failed to save user {message.from_user.id} - {message.from_user.username} | Error {e}")

    def find_client(self, tg_id):
        """Find a client by tg_id."""
        try:
            url = f"{self.HOST}{self.CLIENTS_URL}?filters[$and][0][tg_id][$eq]={tg_id}"
            response = self.__send_get_request(url)
            if response.status_code == 200 and response.json():
                return response.json()['data'][0]
            return None
        except Exception as e:
            self.logger.error(f"Failed find client with tg_id: {tg_id} | Error {e}")

    def create_json_input(self, json_data, client_id):
        """Create a new json_input and link it to the client."""
        try:
            url = f"{self.HOST}{self.JSON_INPUTS_URL}"
            payload = {
                "data": {
                    "data": json_data,
                    "client": client_id,
                }
            }
            headers = {"Content-Type": "application/json"}
            response = self.__send_post_request(url, payload, headers=headers)
            if response.status_code in (200, 201) and response.json():
                return response.json()
            else:
                self.logger.error(f"Failed to create json_input: {response.content}")
            return response
        except Exception as e:
            self.logger.error(f"Failed to save json: {json_data} of client_id: {client_id} | Error {e}")

    def update_json_input_by_id(self, id_, json_data):
        """Update json_input json_data by its id"""
        try:
            url = f"{self.HOST}{self.JSON_INPUTS_URL}/{id_}"
            payload = {
                "data": {
                    "data": json_data,
                }
            }
            headers = {"Content-Type": "application/json"}
            response = self.__send_put_request(url, payload, headers=headers)
            if response.status_code in (200, 201) and response.json():
                return response.json()
            else:
                self.logger.error(f"Failed to update json_input: {response.content}")
            return response
        except Exception as e:
            self.logger.error(f"Failed to update json_input with json_data:: {json_data} of json_input_id: {id_} | Error {e}")
