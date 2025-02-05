from copy import deepcopy

TEST_CASES = [
    {
        "expected": 15,
        "payload": {
            "retailer": "Walgreens",
            "purchaseDate": "2022-01-02",
            "purchaseTime": "08:13",
            "total": "2.65",
            "items": [
                {"shortDescription": "Pepsi - 12-oz", "price": "1.25"},
                {"shortDescription": "Dasani", "price": "1.40"},
            ],
        },
    },
    {
        "expected": 28,
        "payload": {
            "retailer": "Target",
            "purchaseDate": "2022-01-01",
            "purchaseTime": "13:01",
            "total": "35.35",
            "items": [
                {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
                {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
                {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
                {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
                {"shortDescription": "   Klarbrunn 12-PK 12 FL OZ  ", "price": "12.00"},
            ],
        },
    },
    {
        "expected": 109,
        "payload": {
            "retailer": "M&M Corner Market",
            "purchaseDate": "2022-03-20",
            "purchaseTime": "14:33",
            "total": "9.00",
            "items": [
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25" },
                {"shortDescription": "Gatorade", "price": "2.25"},
                {"shortDescription": "Gatorade", "price": "2.25"},
            ],
        },
    },
]


RECEIPTS_WITH_INCOMPLETE_DATA = [{k: v for k, v in deepcopy(TEST_CASES[0]["payload"]).items()} for _ in range(6)]
del(RECEIPTS_WITH_INCOMPLETE_DATA[0]["retailer"])
del(RECEIPTS_WITH_INCOMPLETE_DATA[1]["purchaseDate"])
del(RECEIPTS_WITH_INCOMPLETE_DATA[2]["purchaseTime"])
del(RECEIPTS_WITH_INCOMPLETE_DATA[3]["total"])
del(RECEIPTS_WITH_INCOMPLETE_DATA[4]["items"][0]["shortDescription"])
del(RECEIPTS_WITH_INCOMPLETE_DATA[5]["items"][0]["price"])


RECEIPTS_WITH_BAD_DATA = [{k: v for k, v in deepcopy(TEST_CASES[0]["payload"]).items()} for _ in range(6)]
RECEIPTS_WITH_BAD_DATA[0]["retailer"] = "*"
RECEIPTS_WITH_BAD_DATA[1]["purchaseDate"] = "*"
RECEIPTS_WITH_BAD_DATA[2]["purchaseTime"] = "*"
RECEIPTS_WITH_BAD_DATA[3]["total"] = "*"
RECEIPTS_WITH_BAD_DATA[4]["items"][0]["shortDescription"] = "*"
RECEIPTS_WITH_BAD_DATA[5]["items"][0]["price"] = "*"
