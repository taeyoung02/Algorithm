#include<iostream>
#include<cstring>
using namespace std;
bool check[100001];
int arr[100001];
int dfs(int x, int start) {
	check[x] = true;//����湮���� üũ
	int y = arr[x];//�������� ����Ű�� ��
	int cnt = 0;
	if (!check[y])dfs(y, start);//�̹湮�� ���̸� �湮
	else {//��湮�̶��
		for (int i = start; i != y; i = arr[i])//���������� ��湮�� ����(����Ŭ�� ���۵Ǵ�����)
											//���� ������ ���� �̰��� ����Ŭ�� ���Ե������� ����
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
			if (!check[i])ans += dfs(i, i);//������ ���� ������ ����
		cout << ans << '\n';
	}
}