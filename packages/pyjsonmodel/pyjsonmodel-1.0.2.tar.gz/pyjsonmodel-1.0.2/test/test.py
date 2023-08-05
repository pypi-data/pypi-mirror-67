import sys
sys.path.append(".")
from jsonModel import loads, dumps


class GModel:
    sss = None


class ZModel:
    aaa = None


class TestModel:
    name = None
    age = None
    girlFriends = None
    zzz = None
    testList = None

    # 这里指定属性类型
    __doc__ = {
        "girlFriends": GModel,
        "zzz": ZModel
    }


if __name__ == '__main__':
    data = '[{"testList":[1, 2, 3],"name":"jack","age":13,"girlFriends":[{"sss":"111"},{"sss":"222"}],"zzz":{"aaa":"aaa"}},{"testList":[1, 2, 3],"name":"jone","age":21,"girlFriends":[{"sss":"111"},{"sss":"222"}],"zzz":{"aaa":"aaa"}}]'

    res = loads(data, TestModel)
    for r in res:
        print(r.testList)
        print(r.name)
        print(r.age)
        print([i.sss for i in r.girlFriends])
        print(r.zzz.aaa)
    jsonStr = dumps(res)
    print(jsonStr)







