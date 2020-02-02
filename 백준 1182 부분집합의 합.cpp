#include<iostream>
using namespace std;
int main() {
	int a, b,sum=0; cin >> a >> b;
	while (a != 0) {
		int B = b;
		while (B != 0) {
			sum += (B % 10)*(a % 10);
			B /= 10;
		}
		a /= 10;
	}
	cout << sum;
}