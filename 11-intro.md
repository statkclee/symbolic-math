
### 기호 계산(Symbolic Computation)이란 무엇인가?

기호계산은 수학 객체 계산을 기호적으로 처리한다. 수학객체를 근사적이 아닌 정확하게 표현되고,
평가되지 않는 변수를 갖는 수학 표현식은 기호적 형태로 그대로 남겨있다는 것을 의미한다.

예제를 살펴보자. 제곱근을 계산하는데 파이썬 내장함수를 사용한다. 이런 경우 다음과 같이 코드를 작성하고 명령어를 전달한다.


```python
import math
math.sqrt(9)
```




    3.0



9 는 완전 제곱수라 정답으로 3이 출력된다. 하지만, 완전제곱수가 아닌 경우를 살펴보자.


```python
math.sqrt(8)
```




    2.8284271247461903



조금더 나가면, $\sqrt{8} = \sqrt{4*2} = 2\sqrt{2}$가 된다.


```python
from sympy import *
init_printing(use_unicode=True)
sympy.sqrt(3)
```




$$\sqrt{3}$$


