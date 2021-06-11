# Too Much Information from the JoonionTV TMILab. 

### A* Search Algorithm

최단 경로를 찾는 휴리스틱 알고리즘. 다익스트라 알고리즘의 변형.
자세한 설명은 유튜브 동영상 해설 참조
<https://youtu.be/pUZhNMAqLbI>

더 자세한 설명은 이 블로그에서 참조할 수 있음.
<https://www.redblobgames.com/pathfinding/a-star/introduction.html>

### N-Puzzle Solver

8-퍼즐, 15-퍼즐 문제를 파이썬으로 해결해 보자. 

먼저 solvable 조건을 이해해야 한다. 왜냐하면, 퍼즐을 풀 수 없는 경우가 있기 때문이다. 여기에 대해서는 다음 사이트에서 solvable 조건을 정확하게 파악할 수 있다.
<https://www.geeksforgeeks.org/check-instance-8-puzzle-solvable/>
<https://www.geeksforgeeks.org/check-instance-15-puzzle-solvable/>

8-퍼즐은 다익스트라 알고리즘으로도 풀 수 있다. 하지만, 15-퍼즐은 다익스트라로는 답이 없다. A* 알고리즘을 적용해야 겨우 풀 수 있다. A*를 적용하려고 해도, 효율적인 구현을 하지 못하면 실행 시간이 너무 오래 걸린다. 이런저런 테크닉을 적용해서 겨우겨우 10초 이내에 풀 수 있도록 구현할 수 있었다.

이 문제를 Branch-and-Bound로 구현해서 A*와의 성능 비교를 해보는 것도 좋겠다. 
