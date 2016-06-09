---
layout: page
title: 기호 수학(Symbolic Math) 
---


> ## 선수 지식과 참고자료 {.prereq}
>
> - 수학 기본 지식 -- 대수, 미적분, 선형대수
> - 데이터과학과 기계학습을 학습하기 위한 투철한 열정
>
> ### xwMOOC 오픈 교재
> 
> - [컴퓨터 과학 언플러그드](http://unplugged.xwmooc.org)  
> - [리보그](http://reeborg.xwmooc.org)  
>      - [러플](http://rur-ple.xwmooc.org)  
> - [파이썬 거북이](http://swcarpentry.github.io/python-novice-turtles/index-kr.html)  
> - [정보과학을 위한 파이썬](http://python.xwmooc.org)  
> - [소프트웨어 카펜트리 5.3](http://statkclee.github.io/swcarpentry-version-5-3-new/)
>     - [소프트웨어 카펜트리 5.2](http://swcarpentry.xwmooc.org)
> - [통계적 사고](http://think-stat.xwmooc.org/)
> - [IoT 오픈 하드웨어(라즈베리 파이)](http://raspberry-pi.xwmooc.org/)
>     - [$100 오픈 컴퓨터](http://computer.xwmooc.org/)   
>     - [$100 오픈 슈퍼컴퓨터](http://computers.xwmooc.org/)
> - [R 데이터과학](http://data-science.xwmooc.org/)
> - [R 팩키지](http://r-pkgs.xwmooc.org/)


## 학습 목차

1. [수학의 역사](01-math-history.html)
1. [심파이 설치](02-sympy-install.html)
1. 심파이 사용지침서 [^sympy-tutorial]
    

|   한국어(Korean)      |    영어(English)            |
|------------------------|---------------------------|
| [소개](11-intro.html) |[Introduction](http://docs.sympy.org/latest/tutorial/intro.html)|
| [Gotcha](12-gotcha.html) |[Gotchas](http://docs.sympy.org/latest/tutorial/gotchas.html)|
| [기본 연산](13-operations.html) |[Basic Operations](http://docs.sympy.org/latest/tutorial/basic_operations.html)|
| [간략화](14-simplification.html) |[Simplification](http://docs.sympy.org/latest/tutorial/simplification.html)|
| [미적분](15-calculus.html) |[Calculus](http://docs.sympy.org/latest/tutorial/calculus.html)|
| [문제풀이](16-solver.html) |[Solver](http://docs.sympy.org/latest/tutorial/solvers.html)|
| [행렬](17-matrix.html) |[Matrices](http://docs.sympy.org/latest/tutorial/matrices.html)|

[^sympy-tutorial]: [SymPy Tutorial](http://docs.sympy.org/latest/tutorial/)

컴퓨터를 단순 계산이 아닌 대수(algebra), 기호 수학(symbolic math) 작업을 수행하는데,
파이썬 심파이를 사용한다. 파이썬 심파이를 명령라인 인터페이스만 활용할 경우 여러가지 불편함이 있고,
생각보다 생산성이 높지 않아 최근에 개발된 [쥬피터 노트북](http://jupyter.org/)을 사용한다.

과학 컴퓨팅을 위해 다양한 파이썬 팩키지와 개발환경을 통합해서 설정을 이미 맞춰놓은 
[아나콘다](https://www.continuum.io/)를 [다운로드](https://www.continuum.io/downloads) 받아 
클릭만하면 바로 과학 컴퓨팅 분석 작업 혹은 응용프로그램 개발에 착수할 수 있다.


> ## 이제는 웹에서도 수학을 유창하게 말할 수 있어요 !!! {.callout}
>
> 2차 방정식 $a x^2 + b x + c = 0$ 에 대한 해답은 ...
>
> $$x = \frac{-b \pm \sqrt{b^2 - 4 a c}}{2 a}$$ 



