from starlette.config import Config


class Const:
    """
    ### 시스템에서 사용되는 각종 상수를 관리한다.
    *  DB_URL : 데이터베이스 URL
    """

    config = Config(".env")  # app 디렉토리의 .env 파일 불러오기

    DB_URL = config("DB_URL")


const = Const()
