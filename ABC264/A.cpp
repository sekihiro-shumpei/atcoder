#include<bits/stdc++.h>
using namespace std;

int main() {
    string s = "atcoder";
    int l, r;
    cin >> l >> r;
    cout << s.substr(l-1,r-l + 1) << endl;

}