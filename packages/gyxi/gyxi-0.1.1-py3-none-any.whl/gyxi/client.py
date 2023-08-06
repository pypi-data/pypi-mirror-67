from dataclasses import dataclass
from typing import Any, Mapping
from enum import Enum
from http import HTTPStatus

import requests


class GyxiRegion(Enum):
    """Gyxi region"""

    west_europe = "westeurope"
    north_europe = "northeurope"
    germany = "germany"
    france = "france"
    uk = "uk"
    norway = "norway"


class GyxiAction(Enum):
    """Gyxi action"""

    save = "save"
    batch = "batch"
    get = "get"
    delete = "delete"
    lst = "list"


class GyxiClient:
    __database_id: str
    __region: GyxiRegion

    def __init__(self, config: Mapping[str, Any]):
        assert 'database_id' in config
        assert 'region' in config
        assert isinstance(config['region'], GyxiRegion)

        self.__database_id = config["database_id"]
        self.__region = config["region"]


    def save(self, data_type: str, partition: str, id: str, content: Any):
        """
        Saves a single item in Gyxi

        :param data_type: The data type. It is likely that it corresponds
            to a class. It is an advantage, but not a requirement, that items of the same type have the same properties.

        :param partition: Partition, usually by the primary foreign key on this item. If not partitioned, set a static value, such as "all"

        :param id: The unique id of this item. Must be unique within the partition.

        :param content: The actual item
        """

        endpoint = self.__get_endpoint(GyxiAction.save, data_type, partition, id)
        response = requests.post(endpoint, json=content)

        if not response.ok:
            raise Exception(f"Error when saving in Gyxi {response.text}")

    def save_batch(self, data_type: str, partition: str, content: Mapping[str, Any]):
        """
        Saves up to 100 items in one call, which is far faster than saving 100 individual items. Useful for data migrations.

        :param data_type: The type name of the data being saved

        :param partition: The partition of the items being saved. All items must be part of the same partition.

        :param content: A dictionary with all the items. The key is the id of each item and the value is the full content.
        """

        endpoint = self.__get_endpoint(GyxiAction.batch, data_type, partition, id)
        response = requests.post(endpoint, json=content)

        if not response.ok:
            raise Exception(
                f"Error {response.status_code} when batch saving in Gyxi: {response.text}"
            )

    def get(self, data_type: str, partition: str, id: str):
        """
        Gets a single item very efficiently.

        :param data_type: The name of the data type

        :param partition: The partition where the item is located

        :param id: The id of the item

        :return: The deserialized item or null/default if the item was not found.
        """

        endpoint = self.__get_endpoint(GyxiAction.get, data_type, partition, id)
        response = requests.get(endpoint)

        if response.status_code == HTTPStatus.NOT_FOUND:
            return None

        if not response.ok:
            raise Exception(f"Error when getting from Gyxi: {response.text}")

        return response.json()

    def list(self, data_type: str, partition: str):
        """
        Gets up to 100 items.

        Returns a continuation token to get the next 100 items

        :param data_type: The name of the data type

        :param partition: The partition where the item is located
        """

        endpoint = self.__get_endpoint(GyxiAction.lst, data_type, partition)
        response = requests.get(endpoint)

        if not response.ok:
            raise Exception(f"Error when getting from Gyxi: {response.text}")

        return response.json()

    def delete(self, data_type: str, partition: str, id: str):
        """
        Deletes a single item.

        :param data_type: The name of the data type

        :param partition: The partition where the item is located

        :param id: The id of the item

        :return: The deserialized item or null/default if the item was not found.
        """
        endpoint = self.__get_endpoint(GyxiAction.delete, data_type, partition, id)
        response = requests.delete(endpoint)

        if response.status_code == HTTPStatus.NOT_FOUND:
            return

        if not response.ok:
            raise Exception(f"Error when deleteing in Gyxi: {response.text}")

    def __get_endpoint(
        self, action: GyxiAction, data_type: str, partition: str, id: str = ""
    ):
        return f"https://{action.value}-{self.__region.value}.gyxi.com/{self.__database_id}/{data_type}/{partition}/{id}"
