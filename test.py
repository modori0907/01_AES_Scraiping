AES = [
    {"AES_NO": 1, "host_name": "AES#1", "IP_ADDRESS": "aes1.aura8.avaya.tsuzuki.co.jp", "ID": "cust", "PW": "Tdtcpw!7726"},
    {"AES_NO": 2, "host_name": "AES#2", "IP_ADDRESS": "aes1.aura8.avaya.tsuzuki.co.jp", "ID": "cust", "PW": "Tdtcpw!7726"},
]

# print(AES[0]["IP_ADDRESS"])

test_list = [1,2,3,4,5,6,7,8,9,0]


def split_list(l, n):
    """
    リストをサブリストに分割する
    :param l: リスト
    :param n: サブリストの要素数
    :return:
    """
    for idx in range(0, len(l), n): # range(スタート、ストップ、ステップ)
        yield l[idx:idx + n]
        print(l)

resutlt = split_list(test_list,2)
print(resutlt)

