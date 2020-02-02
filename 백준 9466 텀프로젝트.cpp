#include<iostream>
#include<cstring>
using namespace std;
bool check[100001];
int arr[100001];
int dfs(int x, int start) {
	check[x] = true;//현재방문한점 체크
	int y = arr[x];//현재점이 가리키는 점
	int cnt = 0;
	if (!check[y])dfs(y, start);//미방문한 점이면 방문
	else {//재방문이라면
		for (int i = start; i != y; i = arr[i])//시작점부터 재방문한 지점(사이클이 시작되는지점)
											//까지 갯수를 세줌 이것은 싸이클에 포함되지못한 점들
			cnt++;
		return cnt;
	}
}
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
	int t, n;
	cin >> t;
	while (t--) {
		int ans = 0;
		cin >> n;
		memset(check, 0, sizeof(check));
		for (int i = 1; i <= n; i++)
			cin >> arr[i];
		for (int i = 1; i <= n; i++)
			if (!check[i])ans += dfs(i, i);//떨거지 점의 갯수를 합함
		cout << ans << '\n';
	}
}