#include<bits/stdc++.h>
using namespace std;

int main(){
    int n, p, ans = 0;
    cin >> n >> p;
    int a[n];
    
    for (int i = 0; i < n; i++){
        cin >> a[i];
        if (a[i] < p){
            ans += 1;
        }
    }

    cout << ans << endl;

}