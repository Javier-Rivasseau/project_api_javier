'''Module for retrieving facts about numbers using an external API.

This module contains a function, get_number_fact, that allows you to

retrieve interesting facts about a given number.'''

import requests
def get_number_fact(number: int) -> str:
    """_summary_

    Args:
        number (int): The number to retrieve a fact tor.

    Returns:
        str: A fact about the number
        
    """
    url = "http://numbersapi.com/" + str(number)
    response = requests.get(url, timeout= 10)
    if response.status_code == 200:
        fact = response.text
        return fact
    return "An error occurred."