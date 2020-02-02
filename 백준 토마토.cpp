#include<iostream>
#include<queue>
using namespace std;
int arr[1001][1001];
int ripe[1001][1001];
int tomato, notomato, day;
int dx[4] = { 0,0,1,-1 };
int dy[4] = { 1,-1,0,0 };
int main() {
	int n, m;
	cin >> m >> n;
	queue<pair<int,int>> q;
	for(int i=0; i<n; i++)
		for (int j = 0; j < m; j++) {
			cin >> arr[i][j];
			if (arr[i][j] == 1) {
				tomato++;
				q.push(make_pair(i, j));
			}
			else if (arr[i][j] == -1)
				notomato++;
		}
	if (n*m == tomato + notomato) {
		cout << "0";
		return 0;
	}
	while (!q.empty()) {
		int currentsize = q.size();//q.size()를 바로 써버리면 for문을 돌때마다 함수의 값이 바뀜
		for (int k = 0; k < currentsize; k++) {//이 코드가 없으면 각각의 점에서부터 탐색이아니라 특정한 점만
			//끝까지 탐색을하고 다음 점으로 넘어가서 뒤죽박죽이 되어 각 점마다 동시다발적으로 bfs탐색을 할수없음
			int y = q.front().first;
			int x = q.front().second;
			q.pop();
			for (int i = 0; i < 4; i++) {
				int Y = y + dy[i];
				int X = x + dx[i];
				if (X >= 0 && Y >= 0 && X < m && Y < n && !arr[Y][X]) {
					q.push(make_pair(Y, X));
					arr[Y][X] = 1;
					tomato++;
				}
			}
		}
		day++; //for문을 다돌면 각각의 점마다 한칸씩 전진한것이고 하루가 지남
		if (n*m == tomato + notomato) {
			cout << day;
			return 0;
		}
	}
	cout << "-1";
}