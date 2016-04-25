
# 미적분

미분, 적분, 극한, 급수 전개 같은 기본적인 미분적분을 심파이에서 계산하는 방법을 다룬다.
미적분 수학에 친숙하지 않다면, 그냥 넘어가도 좋다.


```python
from sympy import *
x, y, z = symbols('x y z')
init_printing(use_unicode=True)
```

## 미분

미분을 할 때는 `diff` 함수를 사용한다.


```python
diff(cos(x), x)
```




$$- \sin{\left (x \right )}$$




```python
diff(exp(x**2), x)
```




$$2 x e^{x^{2}}$$



`diff` 함수는 한번에 미분을 여러번 수행할 수 있다.
미분을 여러번 수행하려면, 변수를 미분취하고자 하는 만큼 전달하거나,
변수 뒤에 숫자를 넘겨 전달한다.
예를 들어, 다음 두가지 모두 $x^4$에 대해 3번 미분한다.


```python
diff(x**4, x, x, x)
```




$$24 x$$




```python
diff(x**4, x, 3)
```




$$24 x$$



한번에 다수 변수에 대해 미분을 취할 수도 있다.
단일 변수 미분과 동일한 구분을 사용해서 각 미분을 순서대로 전달한다.
예를 들어, 다음 각각은 $\frac{\partial^7}{\partial x\partial y^2\partial z^4} e^{x y z}$ 미분을 계산한다.


```python
expr = exp(x*y*z)
diff(expr, x,y,y,z,z,z,z)
```




$$x^{3} y^{2} \left(x^{3} y^{3} z^{3} + 14 x^{2} y^{2} z^{2} + 52 x y z + 48\right) e^{x y z}$$




```python
diff(expr, x, y, 2, z, 4)
```




$$x^{3} y^{2} \left(x^{3} y^{3} z^{3} + 14 x^{2} y^{2} z^{2} + 52 x y z + 48\right) e^{x y z}$$




```python
diff(expr, x, y, y, z, 4)
```




$$x^{3} y^{2} \left(x^{3} y^{3} z^{3} + 14 x^{2} y^{2} z^{2} + 52 x y z + 48\right) e^{x y z}$$



`diff`를 메쏘드로 호출할 수도 있다.
`diff`를 호출하는 두가지 방식은 정확히 동일하고, 편리함을 목적으로 제공된다.


```python
expr.diff(x, y, y, z, 4)
```




$$x^{3} y^{2} \left(x^{3} y^{3} z^{3} + 14 x^{2} y^{2} z^{2} + 52 x y z + 48\right) e^{x y z}$$



값을 매기지 않은 미분을 생성하려면, `Derivatives` 클래스를 사용한다.
`diff`와 동일한 구문을 갖는다.


```python
deriv = Derivative(expr, x, y, y, z, 4)
deriv
```




$$\frac{\partial^{7}}{\partial x\partial y^{2}\partial z^{4}}  e^{x y z}$$



아직 값을 매기지 않은 미분에 값을 매기려면, `doit` 메쏘드를 사용한다.


```python
deriv.doit()
```




$$x^{3} y^{2} \left(x^{3} y^{3} z^{3} + 14 x^{2} y^{2} z^{2} + 52 x y z + 48\right) e^{x y z}$$



이런 값을 매기지 않은 객체는 미분에 대한 값을 매기는 것을 지연시키거나 출판 목적으로 유용하다.
심파이가 표현식 미분을 어떻게 계산하는지 모를 때도 사용될 수 있다.(예를 들어, 정의되지 않는 함수를 포함하고 있는 경우, [Solving Differential Equations](http://docs.sympy.org/latest/tutorial/solvers.html#tutorial-dsolve)에 기술되어 있다)

## 적분

적분을 계산하는데 `integrate` 함수를 사용한다.
두가지 유형의 적분이 존재한다: 부정적분과 정적분.
부정적분, 즉 역도함수, 원시함수를 계산하려면, 표현식 다음에 변수를 전달만하면 된다.


```python
integrate(cos(x), x)
```




$$\sin{\left (x \right )}$$



심파이가 적분 상수를 포함하지 않음에 주목한다.
포함시키려면, 본인 스스로 포함을 시키거나 미분방정식으로 문제를 다시 바꾸어 표현해서 `dsolve` 함수로 푸는데, 이 경우에 상수가 추가되어 있다. [Solving Differential Equations](http://docs.sympy.org/latest/tutorial/solvers.html#tutorial-dsolve)을 참고한다.

> 빠른 도움말
> 심파이에서 $\infty$ 는 `oo`(영문 소문자 `o` 두번) 로 표기된다. `oo`가 $\infty$ 처럼 보이고, 타이핑하기 쉽기 때문이다.

정적분을 계산하려면, 인자를 `(integration_variable, lower_limit, upper_limit)` 순서로 넘긴다.
예를 들어, 다음을 계산하는데,

$\int_0^\infty e^{-x}\,dx$

다음과 같이 작성한다.


```python
integrate(exp(-x), (x, 0, oo))
```




$$1$$



부정적분과 마찬가지로, 극한 튜플을 다수 넘겨서 다중적분을 계산할 수도 있다.
예를 들어,

$ \int_{-\infty}^{\infty}\int_{-\infty}^{\infty} e^{- x^{2} - y^{2}}\, dx\, dy,$

다음과 같이 계산한다.


```python
integrate(exp(-x**2 - y**2), (x, -oo, oo), (y, -oo, oo))
```




$$\pi$$



`integrate` 함수가 적분을 계산할 수 없는 경우, 값 매김할 수 없는 `integral` 객체를 반환한다.


```python
expr = integrate(x**x, x)
print(expr)
```

    Integral(x**x, x)



```python
expr
```




$$\int x^{x}\, dx$$



`Derivative` 와 마찬가지로, `Integral`을 사용해서 값 매김할 수 없는 적분을 생성할 수 있다.
나중에 해당 적분에 값 매김을 하려면, `doit`을 호출한다.


```python
expr = Integral(log(x)**2, x)
expr
```




$$\int \log^{2}{\left (x \right )}\, dx$$




```python
expr.doit()
```




$$x \log^{2}{\left (x \right )} - 2 x \log{\left (x \right )} + 2 x$$



`integrate` 함수는 정적분과 부정적분을 항상 계산하는데 이바지하는 강력한 알고리즘을 사용한다.
휴리스틱 패턴 매칭 알고리즘, [Risch algorithm](http://en.wikipedia.org/wiki/Risch_algorithm) 부분 구현, 특수 함수, 특히 정적분에 대한 적분을 계산하는데 유용한 [Meijer G-functions](http://en.wikipedia.org/wiki/Meijer_g-function)를 이용한 알고리즘이 포함된다. `integrate` 함수의 강력함을 보여주는 사례가 다음에 나와 있다.


```python
integ = Integral((x**4 + x**2*exp(x) - x**2 - 2*x*exp(x) - 2*x - 
                  exp(x))*exp(x)/((x - 1)**2*(x + 1)**2*(exp(x) + 1)), x)
integ
```




$$\int \frac{\left(x^{4} + x^{2} e^{x} - x^{2} - 2 x e^{x} - 2 x - e^{x}\right) e^{x}}{\left(x - 1\right)^{2} \left(x + 1\right)^{2} \left(e^{x} + 1\right)}\, dx$$




```python
integ.doit()
```




$$\log{\left (e^{x} + 1 \right )} + \frac{e^{x}}{x^{2} - 1}$$




```python
integ = Integral(sin(x**2), x)
integ
```




$$\int \sin{\left (x^{2} \right )}\, dx$$




```python
integ.doit()
```




$$\frac{3 \sqrt{2} \sqrt{\pi} S\left(\frac{\sqrt{2} x}{\sqrt{\pi}}\right)}{8 \Gamma{\left(\frac{7}{4} \right)}} \Gamma{\left(\frac{3}{4} \right)}$$




```python
integ = Integral(x**y*exp(-x), (x, 0, oo))
integ
```




$$\int_{0}^{\infty} x^{y} e^{- x}\, dx$$




```python
integ.doit()
```




$$\begin{cases} \Gamma{\left(y + 1 \right)} & \text{for}\: - \Re{y} < 1 \\\int_{0}^{\infty} x^{y} e^{- x}\, dx & \text{otherwise} \end{cases}$$



마지막 예제는 `Piecewise` 표현식을 반환한다. 왜냐하면, $\Re(y) > 1$이 아닌 경우 적분이 수렴하지 않기 때문이다.

## 극한

심파이는 `limit` 함수로 기호극한을 계산할 수 있다. 

$\lim_{x\to x_0} f(x)$

계산하는 구문은 `limit(f(x), x, x0)`와 같이 적는다.


```python
limit(sin(x)/x, x, 0)
```




$$1$$



값매김 점이 특이점인 경우, `subs` 대신에 `limit`을 사용한다.
심파이가 $\infty$를 표현하는 객체가 있지만, 값매김에 무한을 사용하게 되면 신뢰성에 문제가 생길 수 있다.
이유는 증가율 같은 것을 추적하지 못하기 때문이다. 또한, $\infty - \infty$ 와 
$\frac{\infty}{\infty}$ 경우 $\mathrm{nan}$ (not-a-number, 숫자 아님)을 반환한다. 예를 들어, 


```python
expr = x**2 / exp(x)
expr.subs(x, oo)
```




$$\mathrm{NaN}$$




```python
limit(expr, x, oo)
```




$$0$$



`Derivative`와 `Integral`과 마찬가지로, `limit`는 값매김하지 않는 대응되는 클래스가 있는데, `Limit`이다. 값매김을 수행하려면, `doit`을 사용한다.


```python
expr = Limit((cos(x) - 1)/x, x, 0)
expr
```




$$\lim_{x \to 0^+}\left(\frac{1}{x} \left(\cos{\left (x \right )} - 1\right)\right)$$




```python
expr.doit()
```




$$0$$



한쪽에서 접근하는 극한에 값을 매기려면, `+` 혹은 `-` 부호를 넘겨준다. 예를 들어,

$\lim_{x\to 0^+}\frac{1}{x},$

다음과 같이 작성해서 계산한다.


```python
limit(1/x, x, 0, '+')
```




$$\infty$$



반면에, 


```python
limit(1/x, x, 0, '-')
```




$$-\infty$$



## 수열 전개

심파이로 특정 점 주변에 함수에 대해 점근적 수열 전개를 해서 계산할 수 있다.
$x = x_0$ 점 주변에 $x^n$차항으로 $f(x)$ 전개해서 계산하려면, `f(x).series(x, x0, n)`을 사용한다.
`x0`와 `n`은 생략될 수 있는데, 생략한 경우, 기본디폴트값으로 `x0=0`, `n=6` 값이 사용된다.


```python
expr = exp(sin(x))
expr.series(x, 0, 4)
```




$$1 + x + \frac{x^{2}}{2} + \mathcal{O}\left(x^{4}\right)$$



마지막에 $O\left (x^4\right )$ 항은 $x=0$ 에서 란다우(Landau) 항을 나타낸다.
(컴퓨터 과학의 빅오(Big O) 표기법과 혼동하지 말자. 일반적으로 $x = \infty$ 로 갈 때 란다우 항을 표현한다.)
$x^4$ 보다 크거나 같은 거듭제곱항을 갖는 모든 $x$ 항이 빠지게 됨을 의미한다.
거듭제곱항은 `series` 외부에서 생성되고 조작되는데, 자동으로 고차 거듭제곱항을 흡수하는 성질이 있다.


```python
x + x**3 + x**6 + O(x**4)
```




$$x + x^{3} + \mathcal{O}\left(x^{4}\right)$$




```python
x*O(1)
```




$$\mathcal{O}\left(x\right)$$



거듭제곱 항을 원치 않는 경우, `remove0` 메쏘드를 사용한다.


```python
expr.series(x, 0, 4).removeO()
```




$$\frac{x^{2}}{2} + x + 1$$



`o` 표기법은 0이 아닌 임의 극한점에도 사용가능하다.


```python
exp(x - 6).series(x, x0=6)
```




$$-5 + \frac{1}{2} \left(x - 6\right)^{2} + \frac{1}{6} \left(x - 6\right)^{3} + \frac{1}{24} \left(x - 6\right)^{4} + \frac{1}{120} \left(x - 6\right)^{5} + x + \mathcal{O}\left(\left(x - 6\right)^{6}; x\rightarrow6\right)$$



## 유한 차분

지금까지 해석적 미분과 원시함수형태 표현식을 살펴봤다.
닫힌 형식 표기법이 존재하지 않는 곡선, 혹은 함수값을 알지 못하는 곡선에 대한 미분을 추정하는 표현식을 다루고자 하면 어떨까?
한가지 접근법은 유한차분을 사용하는 것이다.

`Derivative` 인스턴스에 `as_finite_diff` 방법을 사용해서 임의 거듭제곱항에 근사값을 생성한다.


```python
f = Function('f')
dfdx = f(x).diff(x)
as_finite_diff(dfdx)
```




$$- f{\left (x - \frac{1}{2} \right )} + f{\left (x + \frac{1}{2} \right )}$$



1차 미분으로 `x` 주변에서 근사했는데, 1 간격크기를 사용해서 동일거리에 값 매김되는 최소점을 사용했다.
임의 간격크기를 사용할 수도 있다(기호 표현식을 포함하는 것도 가능).


```python
f = Function('f')
d2fdx2 = f(x).diff(x, 2)
h = Symbol('h')
as_finite_diff(d2fdx2, [-3*h, -h, 2*h])
```




$$\frac{1}{5 h^{2}} f{\left (- 3 h \right )} - \frac{1}{3 h^{2}} f{\left (- h \right )} + \frac{2}{15 h^{2}} f{\left (2 h \right )}$$



가중치를 값매김하는데만 관심이 있다면, 수작업으로 다음과 같이 계산할 수도 있다:


```python
finite_diff_weights(2,[-3,-1,2],0)[-1][-1]
```




$$\left [ \frac{1}{5}, \quad - \frac{1}{3}, \quad \frac{2}{15}\right ]$$



`finite_diff_weights`에서 반환되는 마지막 요소만 필요하다는데 주목한다.
이런 이유는 `finite_diff_weights`가 차수가 낮은 미분과 더 적은 점을 사용해서 가중치를 생성하기 때문이다. (좀더 자세한 정보는 `finite_diff_weights` 문서를 참고한다.)

`finite_diff_weights`를 직접적으로 사용하는 것이 복잡해 보이고, `Derivative` 인스턴스에서 동작하는 `as_finite_diff` 함수가 유연하지 못한 경우, 거듭제곱항과 x_list, y_list, x0를 인자로 받는 `apply_finite_diff`를 사용한다.


```python
x_list = [-3, 1, 2]
y_list = symbols('a b c')
apply_finite_diff(1, x_list, y_list, 0)
```




$$- \frac{3 a}{20} - \frac{b}{4} + \frac{2 c}{5}$$


