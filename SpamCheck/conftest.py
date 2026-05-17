import sys
import os

# SpamCheck/ 디렉토리를 Python 모듈 경로에 추가
# → pytest가 "from app.xxx import yyy"를 찾을 수 있게 함
sys.path.insert(0, os.path.dirname(__file__))
