#include <bits/stdc++.h>
using namespace std;

int main(){
    string s;
    cin >> s;

    if (s.size() == 1){
        cout << s + s + s + s + s + s ;
    }
    else if (s.size() == 2){
        cout << s + s + s;
    }
    else{
        cout << s + s ;
    }

    return 0;


}