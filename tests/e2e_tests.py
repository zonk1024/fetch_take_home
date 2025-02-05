#!/usr/bin/env python3


# stdlib
from json import dumps

# 3rd party
import requests

# internal
from test_data import TEST_CASES


DOMAIN = "127.0.0.1"
PORT = 8000


def test_post(payload):
    url = f"http://{DOMAIN}:{PORT}/receipts/process"

    try:
        response = requests.post(url, json=payload)
    except:
        print(f"Failed to POST {url} with payload: {dumps(payload)}")
        raise

    try:
        data = response.json()
    except:
        print(f"Failed to parse JSON out of response from POST to {url}")
        raise

    try:
        return data["id"]
    except:
        print(f"Failed to find \"id\" in response from POST to {url}:")
        print(dumps(data, sort_keys=True, indent=4))
        raise


def test_get(_id):
    url = f"http://{DOMAIN}:{PORT}/receipts/{_id}/points"

    try:
        response = requests.get(url)
    except:
        print(f"Failed to GET {url}")
        raise

    try:
        data = response.json()
    except:
        print(f"Failed to parse JSON out of response from POST to {url}")
        raise

    try:
        return data["points"]
    except:
        print(f"Failed to find \"points\" in response from GET {url}:")
        print(dumps(data, sort_keys=True, indent=4))
        raise


if __name__ == "__main__":
    err = 0

    for i, test_case in enumerate(TEST_CASES):
        payload = test_case["payload"]
        expected = test_case["expected"]

        _id = test_post(payload)
        print(f"Running test case #{i + 1}... ", end="", flush=True)

        points = test_get(_id)

        if points == expected:
            print("pass!")
        else:
            print("fail!")
            err += 1

    exit(err)
