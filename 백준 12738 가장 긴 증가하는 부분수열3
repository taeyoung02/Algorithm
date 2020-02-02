#include<iostream>
#include<algorithm>
#include<vector>
long long MAX = -1000000001,n;
using namespace std;
int main() {
	ios::sync_with_stdio(0);
	cin.tie(0), cout.tie(0);
    cin >> n;
	vector<long long> lis;
	lis.push_back(MAX);
	for (int a,i= 0; i < n; i++) {
		cin >> a;
		// a가 lis에 저장된 수열의 최댓값보다 크면
		if (a > lis.back()) lis.push_back(a); //a를 lis에 추가하고 길이는 1증가함
		// a가 lis의 저장된 수열의 최댓값보다 작다면
		else *lower_bound(lis.begin(), lis.end(), a)=a; //a보다 크거나 같은값중 가장 근사한 원소에 a를 넣고 인덱스는 a부터 시작
	}//숫자를 받아 부분수열을 만들때 이분탐색을 이용하여 O(N) X O(log N) 의 시간이걸림 
	cout << lis.size()-1; //MAX를 빼준 길이
}
