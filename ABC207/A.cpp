#include<bits/stdc++.h>
using namespace std;

int main(){
    int a, b, c;
    cin >> a >> b >> c;
    int ans1, ans2;

    ans1 = max(a + b, a + c);
    ans2 = max(ans1, b + c);



    cout << max(ans1, ans2) << endl;
    ans1 = max({a + b, a + c, b+c});
    cout << ans1 << endl;

}