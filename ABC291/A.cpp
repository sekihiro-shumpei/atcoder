#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    string s;

    cin >> s;
    n = s.size();

    for(int i = 0; i < n; i++){
        if(isupper(s[i])){
            cout << i + 1 << endl;
        }

    }

    return 0;

}