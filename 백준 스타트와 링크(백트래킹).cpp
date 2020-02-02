#include<iostream>
#include<math.h>
using namespace std;
int min = 100000000;
int N;
int arr[20][20];
int check[20];
int calcul(int* check) {
	int sum1 = 0;
	int sum2 = 0;
	for (int p = 0; p < N; p++)
		if (!check[p])
			for (int i = 0; i < N; i++)
				if (!check[i])
					sum1 += arr[p][i];
	for (int p = 0; p < N; p++)
		if (check[p])
			for (int i = 0; i < N; i++)
				if (check[i])
					sum2 += arr[p][i];
	return abs(sum1 - sum2);
}

void soccer(int playerNum, int cnt, int* check) {
	cout << "soccer(" << playerNum << " , cnt + 1, check)" << endl;
	if (cnt == N / 2) {
		cout << "cnt==N/2" << endl;
		cout << endl;
		int res = calcul(check);
		if (min > res)min = res;
		return;
	}
	for (int i = playerNum; i < N; i++)
	{
		/*
		��ó��  soccer(0,cnt,check)�ȿ��� for�� ���� soccer 1,2,3�� �ٵ��� check[0]=0 ����� soccer(0,cnt,check)����
		���� i�� 1�����Ͽ� soccer(1,cnt,check)���� ����
		soccer(1,cnt,check)�ȿ��� for�� 2,3�� ���� soccer(1,cnt,check)����
		for���� ���� i=2���Ǿ� soccer(2,cnt,check)����
		*/
		if (check[i]==0)
		{	
			check[i] = 1;			 cout << "check["<<i<<"] = true" << endl;
			soccer(i + 1, cnt + 1, check);
			check[i] = 0;				 cout << "check["<<i<<"] = 0" << endl;
		}
	}
}

int main() {
	cin >> N;
	for (int i = 0; i < N; i++)
		for (int j = 0; j < N; j++)
			cin >> arr[i][j];
	soccer(0, 0, check);
	cout << min;
}