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
		맨처음  soccer(0,cnt,check)안에서 for문 안의 soccer 1,2,3이 다돌고 check[0]=0 실행뒤 soccer(0,cnt,check)종료
		이제 i가 1증가하여 soccer(1,cnt,check)부터 시작
		soccer(1,cnt,check)안에서 for문 2,3이 돌고 soccer(1,cnt,check)종료
		for문에 의해 i=2가되어 soccer(2,cnt,check)실행
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