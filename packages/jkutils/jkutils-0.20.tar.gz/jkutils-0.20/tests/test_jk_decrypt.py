import datetime

from jkutils.jk_decrypt import CoreCrypt, CryptoRsa


def test_encrypt():
    a = CoreCrypt()
    body = {
        "data": {
            "applyNo": "20080002857100113252001567398175",
            "businessNo": "20080002857100113252001567398175",
            "repayType": "3",
            "mobile": "18782929633",
            "contractAmount": 2005,
            "loanRate": 12.78,
            "loanPeriod": 24,
            "loadPeriodType": "2",
            "repayPeriod": "1",
            "guaranteeType": "4",
            "rateType": "4",
            "payType": "1",
            "loanPurpose": "2",
            "floatRate": 0,
            "loanBankNo": "6200586950005261991"
        },
        "mchtNo": "00000789",
        "version": "1.0",
        "reqTime": "2020-04-29 15:48:13"
    }
    new_body = a.run(body, "data", "./sn_test_encrypt.pem")
    print(new_body)
    assert new_body


def test_decrypt_public():
    """测试公钥解密"""
    res = {
        "data": "H9xvV0fFpOXzCR+kPGchBmsrh8Yei94y9l6g8cME3Q6IvPc0Ph49qtGndWGU4Vi5hrxv2gaDpqt3EPOS5Hs6cmeAJaTs5DjFVhEFB3jYXJhVKKkIX09GE8WmTpIKwZn4BV6cvZLq60cS4fXyQ/u04hl3On31N1Yjpl3Sw503UHMacb05Q47ieDOM03JTUS4WFQx8e3it9G2nLnC1TBpKXZDLSOtbaqq0qPV8To3HM8UQu8yud8dMnkb++an3j4w1ryOx5LYKZMBUXOLa+73vnZflL1VL32x775er5k5AHfdUKfITHM3tD6qOR/67Snb8cAwiVEGDzvFgewoEHLGNYBXdA/nuYC14O4UOWdDiPw+BzODG3Q7q5AVzRMPuRAoXNK20jdyuQFa5uwDq3Aw8TQAvFPbgIuYqSpknejRGpz+quLN3jVMru5keVYROoD3HuyBsqJtQK0xvXJEa+n9BHEc6ud7EUknwLQu4m+VYRsIGxRahEk4o3VtlcSXENPuJ",
        "mchtNo": "00000789",
        "version": "1.0",
        "reqTime": "2020-04-29 15:48:13",
        "randomKey": "LcxVNa/HBsrYxYR2bW+jDpJMmCLH+bJXJ2jRj724owvSq/GhIg3SMfpXJhXmgy/81xOZpEUewlKIwyaBoKOXShjASRN6MCZmsN5uHV0juGAsHxUWddqst4MNSqs7uSRRkrjYM+GX+CeOmqbSU2Yg4Q6+na+dq5CbHZQAJQKkns431/h5Sf8NrkZEnPngrT3Ynab6Y/gKu27IuuUv1/Dr/p2tmjsPQ4+wvdfnmTlMGpYFvPHPKxDwgTJQrzWFIUoq/ntv6BvQ087PHtBqM5tDZqLi3K6HZjUvf+BOoEZdSCCz6F71iUhPo/g/vL4l06Dy8q8ZJBn24jz06d4O7SsJ+g==",
        "sign": "ai4eZRai/u+OQyj8Y1SbxRzGfAQgjB6kCpXnDUsWncY="
    }
    a = CoreCrypt()
    data = a.decrypt_public("./sn_test_public.pem", res["randomKey"], res["data"], res["sign"], res)
    print(data)
    assert data


# def test_decrypt_private():
#     """测试私钥解密"""
#     res = {
#         "returnCode": "0",
#         "returnMsg": "成功",
#         "respTime": "2019-12-31 16:55:00",
#         "sign": "OGJjZjYzZTI4ZTYzNjVjZGM2NDJkZTM4OTI3MjkyZjAxY2FkMzhiYTM2ZWEwZTBiZjM4MGVmYmRhY2M0ZDIyZQ==",
#         "data": "X+KM6s3r+tJq7PiUDO7YSnBkVzXamF9BGIAueVkXSBs1XiZWNkYHeYmWNOOePk+X",
#         "randomKey": "dl8UuU15g9FNOmNf4s021ulenEmIu0MkOemxhhoFmhB6rxkfi25KnJdZ8dA4UWUBsMFLNWQsIV54l7GdPr+AtyV8M0wX3N7+iSK/SFPQchWMreSo0w6xRXBOFEUcge03pA6BkKPX2M7vcA5UNKEtSZ0P/BgqmV5VawypjFD5DscuCaflpxggyS+dtmu+aKH8EMIU3OXykZqyqvONCP5sA7HnpT6z8Z5Eiw5UvmzTln/SevC7LJxM5RUoUrvN3MnIzgUR8ugwv1rJghQcemtf0L8UHMnZrS8r1RMl2EqTEKQ80JrvUUk+hK2Hmfq6vimL39l8bgAKY20uih++njQfEg==",
#     }
#     a = CoreCrypt()
#     data = a.decrypt_private("./sn_test_encrypt.pem", res["randomKey"], res["data"], res["sign"], res)
#     print(data)
#     assert data
