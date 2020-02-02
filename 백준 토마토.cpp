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
		int currentsize = q.size();//q.size()�� �ٷ� ������� for���� �������� �Լ��� ���� �ٲ�
		for (int k = 0; k < currentsize; k++) {//�� �ڵ尡 ������ ������ ���������� Ž���̾ƴ϶� Ư���� ����
			//������ Ž�����ϰ� ���� ������ �Ѿ�� ���׹����� �Ǿ� �� ������ ���ôٹ������� bfsŽ���� �Ҽ�����
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
		day++; //for���� �ٵ��� ������ ������ ��ĭ�� �����Ѱ��̰� �Ϸ簡 ����
		if (n*m == tomato + notomato) {
			cout << day;
			return 0;
		}
	}
	cout << "-1";
}