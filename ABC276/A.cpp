#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;
    int n = s.length();
    //cout << n << endl;
    int ans = -1;

    for(int i = 0; i <= n; i++){
        if (s[i] == 'a'){
            ans = i;
        }
    }

    if (ans == -1){
        ans = -2;
    } 

    cout << ans + 1 << endl;

}