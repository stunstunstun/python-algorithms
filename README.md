
## awesome-algorithms

이 공간은 Problem Solving 이하 PS 스터디를 위한 공간입니다.

## Get Started

#### Install Python

파이썬은 공식 사이트인 [python.org](https://www.python.org/)에서 다운로드할 수 있다. 설치가 매우 간단하며 OSX 사용자라면 이미 파이썬이 설치되어 있을 것이다. 

가능하면 가장 최신의 버전의 python3를 설치하는 것을 권장한다. 설치 후 커맨드 라인에서 아래와 같이 입력하면, 파이썬 Interpeter를 통해 프로그래밍할 수 있는 환경이 갖추어진다.

```
$ python3
Python 3.6.1 (v3.6.1:69c0db5050, Mar 21 2017, 01:21:04)
[GCC 4.2.1 (Apple Inc. build 5666) (dot 3)] on darwin
Type "help", "copyright", "credits" or "license" for more information.
>>>
```

#### IDLE과 PyCharm IDE

Interpreter 언어인 파이썬은 위와 같은 Interactive 모드를 통해 별도의 도구 없이 한 줄 한 줄 프로그래밍 하도록 도와준다. 

이 REPL은 매우 유용하지만 앞으로 파이썬 코드를 파일에 작성하고자 한다면 JetBrain의 [PyCharm IDE](https://www.jetbrains.com/pycharm/)를 사용하는 것을 추천한다.

> 파이썬에는 파일에 작성하기 위한 기본 도구인 IDLE를 포함하고 있다.

자 뻔한 과정은 생략하고 아래와 같이 Hello World를 출력하는 첫 파이썬 프로그램을 작성해보자.

```
$ echo "print('Hello World!')" > hello_world.py
```

파일에 작성된 코드 역시 파이썬 Interpreter에 의해서 실행되며 방법은 아래와 같다. 정상적으로 출력이 된다면 우리는 파이썬 프로그래밍을 위한 모든 준비를 마쳤다!

```
$ python3 hello_world.py
Hello World!
```

## TDD로 Python 시작하기

만약 파이썬이 처음이라면 TDD를 통해 프로젝트를 구성하고 파이썬을 더욱 멋지게 활용할 수 있는 아래의 글을 참고하도록 하자. 프로젝트의 소스코드는 현재 지금의 Repo 되시겠다. 도움이 될 듯하다면 ★ Star를 누르는 센스도 잊지 말자!

- [시작하기](https://www.holaxprogramming.com/2017/06/15/python-get-started/)
- [unittest와 함께하는 파이썬 테스트](https://www.holaxprogramming.com/2017/06/17/python-with-test/)
- [파이썬 프로젝트의 구조](https://www.holaxprogramming.com/2017/06/28/python-project-structures/)
- [파이썬 실행 환경을 지탱하는 도구들](https://www.holaxprogramming.com/2017/07/15/python-virtual-environments/)

## Run

```
$ python3 -m unittest
```

## How to prepare coding interviews

- [Google](https://careers.google.com/how-we-hire/interview/)
- [Facebook](https://www.facebook.com/notes/facebook-engineering/get-that-job-at-facebook/10150964382448920/)

## PS Sites

- [Hacker Rank](https://www.hackerrank.com/dashboard)
- [LeetCode](https://leetcode.com/)
- [Codility](https://codility.com/programmers/)
- [Kaggle](https://www.kaggle.com/)
- [Visualgo](https://visualgo.net/en)
- [Algorithm Visualizer](http://algo-visualizer.jasonpark.me/#path=backtracking/knight's_tour/basic)

## Contents

- [Testing](#testing)
  - [Time Complexity](#time-complexity)
  - [Big-O Notations](#big-o-notations)
  - [Space Complexity](#space-complexity)
- [Algorithm Solving Strategies](#algorithm-solving-strategies)
	- [Divide and Conquer](#divide-and-conquer)
	- [Dynamic Programming](#dynamic-programming)
	- [Greedy Method](#greedy-method)
	- [Combinatorial Search](#combinatorial-search)
	- [Combinatorial Optimization](#combinatorial-optimization)
- [Algorithms](#algorithms)
	- [Numerical Analysis](#numerical-analysis)
	- [Number Theory](#number-theory)
	- [Computational Geometry](#computational-geometry)
- [Data Structures](#data-structures)
	- [Bitmask](#bitmask)
	- [Dynamic Array](#dynamic-array)
	- [Linked List](#linked-list)
	- [Queue](#queue)
	- [Stack](#stack)
	- [String](#string)
	- [Tree](#tree)
	- [Graph](#graph)

## Testing

#### Time Complexity와 Space Complexity

알고리듬을 테스트하면서 가장 고려할 요소는 Time Complexity와 Space complexity이다.

#### Time Complexity

<img src='https://i1.wp.com/texblog.org/Wordpress/wp-content/uploads/2014/06/big-o-example-latex.png' width='400' />

Time Complexity(시간 복잡도)는 문제를 해결하는데 걸리는 시간과 입력의 함수 관계를 표현한다. 얼마나 많은 데이터를 입력 받았는지 그에 따라 CPU는 얼마나 사용하는지 수행 시간은 얼마나 걸리는지를 표현할 수 있다.

가장 많이 쓰이는 표현법으로는 알고리듬의 실행 시간의 상한을 나타내는 `Big-O` 표기법이 있다.

#### Big-O Notations

<img src='https://camo.githubusercontent.com/874181d7b840a494fe94a11cc13c1fad5d372217/68747470733a2f2f6170656c6261756d2e66696c65732e776f726470726573732e636f6d2f323031312f31302f796161636f766170656c6261756d6269676f706c6f742e6a7067' width='400' />

Big-O | Operations for 10 things | Operations for 100 things
--|--|--
O(1) | 1 | 1
O(log n) | 3 | 7
O(n log n) | 30 | 700 |
0(n^2) | 100 | 10000 |

> Solutions - https://www.martinkysel.com/codility-solutions/

`O(1) - Constant Time`

입력되는 데이터양과 상관없이 일정한 실행 시간을 가진다.

`O(log n) - Logarithmic Time`

- 입력 데이터 양이 많아져도 수행 시간이 조금씩 늘어난다.
- 시간에 비례하여, 탐색 가능한 데이터양이 2의 n승이 된다.

> Binary Search


`O(n) - Linear Time`

- 입력 데이터 양에 따라 수행 시간이 정비례한다.

> 선형 탐색, for 문을 통한 탐색을 생각하면 되겠다.

`O(n log n) - Linearithmic time`

- 입력 데이터 양이 n배 많이 진다면, 수행 시간은 n배 보다 조금 더 많아 진다.
- 정비례하지 않는다.

> 예를 들면, 이진 트리 정렬은 n 크기의 배열 각 요소를 하나하나 삽입하여 이진 트리를 만든다. 자가 균형 이진 탐색 트리의 삽입 연산은 O(log n)시간이 걸리기 때문에, 전체 알고리즘은 Linearithmic time이 걸린다.

`O(n^2) - Quadratic Time`

- 입력 데이터의 양에 따라 수행 시간은 제곱에 비례한다.

> Bubble Sort

#### Space Complexity

#### `이하 컨텐츠를 채우는데 함께하고 싶은 분은 PR을 보내주세요! 🤗`

## Algorithm Solving Strategies

#### Divide and Conquer

#### Dynamic Programming

#### Greedy Method

## Algorithms

#### Numerical Analysis

#### Number Theory

#### Computational Geometry

## Data Structures

#### Bitmask

#### Dynamic Arra

#### Linked List

#### Queue

#### Stack

#### String

#### Tree

#### Graph
