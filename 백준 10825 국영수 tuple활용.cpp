#include <bits/stdc++.h>
using namespace std;
struct member {
	string name;
	int k, e, m;
};
int main() {
	int n; cin >> n;
	vector<member>arr(n);
	for (int i = 0; i < n; i++)
		cin >> arr[i].name >> arr[i].k>>arr[i].e>>arr[i].m;
	sort(arr.begin(), arr.end(), [](member u, member v) {
		return make_tuple(-u.k, u.e, -u.m,u.name) < make_tuple(-v.k, v.e, -v.m,v.name);
	});
	for (int i = 0; i < n; i++)
		cout << arr[i].name << '\n';
}
