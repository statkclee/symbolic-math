---
layout: page
title: 기호 수학(Symbolic Math) 
subtitle: 파이썬 심파이(Sympy)와 함께하는 수학여행
minutes: 10
---

> ## 학습목표 {.objectives}
>
> * 심파이를 설치한다.


### 파이썬 심파이 설치

심파이(Sympy)를 설치하는 다양한 방법이 존재한다. 우분투 운영체제에서 파이썬을 설치하는 방법은 
먼저 `python-pip` 팩키지 설치 관리자를 설치하고 `pip install` 명령어를 통해 `sympy`를 설치한다.

~~~ {.python}
vagrant@vagrant-ubuntu-trusty-64:~$ sudo apt-get install python-pip
vagrant@vagrant-ubuntu-trusty-64:~$ sudo pip install sympy
vagrant@vagrant-ubuntu-trusty-64:~$ python
~~~

`sympy`가 정상적으로 설치가 되었는지 확인하기 위해서 파이썬 명령라인 인터페이스에 
[심파이 사전준비](http://docs.sympy.org/dev/tutorial/preliminaries.html) 예제를 실행한다.

수학문제는 $\int e^x cos(x) dx$ 적분을 계산하는 것이다.
정답은 손으로 계산하면 다음과 같은 결과가 도출되어야 한다.

$\int e^x cos(x) dx = \frac{e^x}{2} sin(x) +  \frac{e^x}{2} cos(x)$

상기 수식을 심파이 구문으로 `Integral(cos(x)*exp(x), x)` 와 같이 입력하고,
`Eq` 함수에 인자로 구문과 더불어 `.doit()` 메쏘드를 실행한다.


~~~ {.output}
Python 2.7.6 (default, Jun 22 2015, 17:58:13)
[GCC 4.8.2] on linux2
Type "help", "copyright", "credits" or "license" for more information.
>>> from sympy import *
>>> x = symbols('x')
>>> a = Integral(cos(x)*exp(x), x)
>>> a
Integral(exp(x)*cos(x), x)
>>> Eq(a, a.doit())
Eq(Integral(exp(x)*cos(x), x), exp(x)*sin(x)/2 + exp(x)*cos(x)/2)
~~~

### 쥬피터 노트북에서 심파이 

`init_printing(use_latex='mathjax')` 설정을 쥬피터 노트북을 통해 설정하게 되면 위와 같은 텍스트 출력수식이 아닌 
수학책에 나오는 수식이 표현된다.

~~~ {.python}
init_printing(use_latex='mathjax')
from sympy import *
x = symbols('x')
a = Integral(cos(x)*exp(x), x)
a
Eq(a, a.doit())
~~~

$\int e^x cos(x) dx = \frac{e^x}{2} sin(x) +  \frac{e^x}{2} cos(x)$


