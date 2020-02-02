#include<iostream>
using namespace std;
int main() {
	int test;
	cin >> test;
	string s;
	int num = 0;
	for (int i = 0; i < test; i++) {
		int arr[26] = { 0 }, check = 1;
		cin >> s;
		for (int i = 0; i < s.size(); i++) {
			if (s[i] != s[i + 1])arr[s[i] - 'a']++;
			if (arr[s[i] - 'a'] > 1)check = 0;
		}
		if(check==1)num++;
	}
	cout << num;
}