import logging
import os
from aiogram import types
import requests


class StrapiClient:
    TOKEN = os.getenv("STRAPI_TOKEN")
    HOST = os.getenv("STRAPI_HOST")
    CLIENTS_URL = "api/clients"

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
                raise Exception(str(result.content, encoding="utf-8"))
            return result
        except Exception as e:
            self.logger.error(f"Failed to save user {message.from_user.id} - {message.from_user.username} | Error {e}")
