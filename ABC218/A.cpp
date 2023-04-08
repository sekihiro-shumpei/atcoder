#include<bits/stdc++.h>
using namespace std;

int main(){
    string ans;
    for (int i = 0; i < 26; i++){
        int p;
        cin >> p;
        p--;
        ans += (char)('a' + p);
    }
    cout << ans << endl;

}