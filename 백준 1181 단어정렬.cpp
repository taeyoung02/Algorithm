#include <iostream>
#include<algorithm>
#include<vector>
#include<string>
using namespace std;
bool comp(string& s1, string& s2) {
	if (s1.size() == s2.size())return s1 < s2;
	else return s1.size() < s2.size();
}
int main() {
	ios::sync_with_stdio(false);
	cin.tie(NULL), cout.tie(NULL);
	string s[20000];
	int n; cin >> n;
	for (int i = 0; i < n; i++)
		cin >> s[i];
	sort(s, s + n, comp);
	cout << s[0] << '\n';
	for (int i = 1; i < n; i++)
		if (s[i] != s[i - 1])
			cout << s[i] << '\n';
}