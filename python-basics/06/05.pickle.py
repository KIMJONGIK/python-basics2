# pickle 모듈
# 객체를 직렬화, 역직렬화 하는 모듈

import pickle


def test_pickle_dump():
    # 직렬화 해제
    with open("thieves.bin", "wb") as f:    # 파일 모드는 반드시 binary여야 한다.
        try:
            pickle.dump({"name": '홍길동', "age": 25}, f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 덤프하지 못했습니다.")
        else:
            print("데이터를 덤프했습니다.")


def test_pickle_load():
    # 역직렬화 예제
    with open("thieves.bin", "rb") as f:
        try:
            thief = pickle.load(f)
        except Exception as e:
            print(e, type(e))
            print("데이터를 로드하지 못했습니다.")
        else:
            print("데이터를 로드했습니다.")
            print(thief, type(thief))


if __name__=="__main__":
        test_pickle_dump()