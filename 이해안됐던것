#include<iostream>
#include <stack>
#include<string>
using namespace std;
string check(char vps[]) {
    stack<char>VPS;
    for (int i = 0; i < 50; i++) {
        if (vps[i] == '(')
            VPS.push('(');
        else if (vps[i] == ')') {
            if (VPS.size() < 1)return "NO";
            else VPS.pop();
        }
    }
    if (VPS.empty())return "YES";
    else return "NO";
}
int main() {
    char s[51];
    int n; cin >> n;
    while (n--) {
        cin >> s;
        cout << check(s) << endl;
    }
}
틀린 이유 :
매개변수로 받은 배열은 포인터라 크기가 4이고 입력된 원소의 갯수만 셀수없기때문에 0부터 50까지 돌리는데
vps[0]부터 vps[50]까지 검사할때 입력되지않은 쓰레기값은 if문에서 비교가 불가하기때문에 에러가남
string으로 해결가능
*vps[i]!=NULL 이 문장으로 갯수를 몰라도 쓰레기값이 아닐때까지만 돌기때문에 해결가능
