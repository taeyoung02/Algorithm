#include<iostream>
#include<algorithm>
using namespace std;
int N, k, w[101], v[101];
int d[101][100001]; //최대 가치
int main() {
	cin >> N >> k;
	for (int i = 1; i <= N; i++) //d[i-1]에서 i가 0이 되지않기위해 1부터저장.
		cin >> w[i] >> v[i];
	for (int i = 1; i <= N; i++)
		for (int j = 0; j <= k; j++)
			if (w[i] > j) d[i][j] = d[i - 1][j]; //현재 용량보다 무게가 큰경우
			else d[i][j] = max(d[i - 1][j - w[i]] + v[i], d[i - 1][j]); //i번째 아이템 챙겼을떄 vs 챙기지 않았을때
	cout << d[N][k];
}
