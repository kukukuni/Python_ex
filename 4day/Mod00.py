# Mod00.py
print('name: {0}'.format(__name__))     # 시작하는 파일 자체가 main이다.
import Calc00                           # 임폴트하는 다른 파일은 파일명이 이름이다.
import Calc00 as c                      # 세가지 방법이 있고, 통일이 필요하다.
from Calc00 import *                    # from 폴더 import 파일
x = 20; y = 10;                         # from 파일 import 항목 등으로 쓸 수 있다.
Calc00.Sum(x,y)
c.Sub(x,y)
Mul(x,y)

import sys
for path in sys.path: print(path)