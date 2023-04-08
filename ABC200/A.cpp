#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, ans;
    cin >> n;
    ans = (n / 100) + 1;
    if (n % 100 == 0){
        ans = n / 100;
    }
    cout << ans << endl;


}