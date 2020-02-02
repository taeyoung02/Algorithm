https://www.acmicpc.net/problem/1074
//1074 Z
//재귀함수를 이용하여 함수안의 플로우를 최대한 간결하게 만들어 시간을 0으로 만들었다
#include<iostream>
using namespace std;
int r, c, n, cnt = 0;
void Z(int size, int y, int x) {
	if (y > r )return; //y가 입력값보다 크면 반환
	else if (y+size<=r || x+size<=c) {//사각형범위가 입력값보다 작으면 사이즈크기만큼 더함
		cnt += size * size; return;
	}
	else if (size == 1) {//1->2->3->4분면으로 이동하며 1씩 증가
		if (r == y && x == c) {
			cout << cnt;  return;
		}cnt++; return;
	}
	
	Z(size / 2, y, x);//1사분면
	Z(size / 2, y, x + size / 2);//2사분면
	Z(size / 2, y + size / 2, x);//3사분면
	Z(size / 2, y + size / 2, x + size / 2);//4사분면
}
int main() {
	cin >> n >> r >> c;
	Z(1 << n, 0, 0);
}
