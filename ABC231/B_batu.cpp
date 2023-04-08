#include<bits/stdc++.h>
#include <algorithm>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<string> v(n);
    for (int i = 0; i < n; i++){
        cin >> v[i];
    }
    int cnt = 1, ans = 0;
    vector<int> a(n - 1);
    for (int j = 0; j < n; j++){
        for (int i = 0; i < n; i++){
            if (v[i] == v[i + 1]){
                cnt += 1;
            }
        }
        cout << cnt << endl;
        a[j] = cnt;
        cnt = 1;
    }
    for (int i = 0; i < n - 2; i++){
        ans = max(a[i], a[i + 1]);
    }
    cout << ans << endl;

}

綺麗にできなっしんぐ。