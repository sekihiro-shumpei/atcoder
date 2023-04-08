#include<bits/stdc++.h>
using namespace std;

int main() {
    int N, l, r, ans = 0;
    cin >> N;

    for (int i = 0; i < N; i++){
        cin >> l >> r;
        ans += (r - l) + 1;
        //l = 0;
        //r = 0;

    }
    cout << ans << endl;
}