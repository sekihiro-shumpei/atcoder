#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, a, x, y;
    int ans;
    cin >> n >> a >> x >> y;

    if (n > a){
        ans = (x * a) + (y * (n - a));
    }
    else{
        ans = x * n;
    }
    cout << ans << endl;



}