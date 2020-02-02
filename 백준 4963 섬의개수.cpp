#include<cstring>
#include<iostream>
#include<queue>
using namespace std;
bool arr[51][51];
int x, y, cnt;
bool d[51][51];
int dx[8] = { 0,0,1,1,1,-1,-1,-1 };
int dy[8] = { 1,-1,0,1,-1,0,1,-1 };
void bfs(int X, int Y, int cnt) {
	d[X][Y] = true;
	queue<pair<int, int>> q;
	q.push(make_pair(X, Y));
	while (!q.empty()) {
		int X = q.front().first;
		int Y = q.front().second;
		q.pop();
		for (int k = 0; k < 8; k++) {
			int nx = X + dx[k];
			int ny = Y + dy[k];
			if (nx >= 0 && ny >= 0 && nx < x && ny < y)
				if (arr[nx][ny] && !d[nx][ny]) {
					q.push(make_pair(nx, ny));
					d[nx][ny] = true;
				}
		}
	}
}
int main() {
	while (true) {
		cnt = 0;
		memset(arr, 0, 51 * 51);
		memset(d, 0, 51 * 51);
		cin >> y >> x;
		if (x == 0 && y == 0)break;
		for (int i = 0; i < x; i++)
			for (int j = 0; j < y; j++)
				cin >> arr[i][j];
		for (int i = 0; i < x; i++)
			for (int j = 0; j < y; j++)
				if (!d[i][j] && arr[i][j])
					bfs(i, j, ++cnt);
		cout << cnt << '\n';
	}
}