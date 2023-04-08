#include<bits/stdc++.h>
using namespace std;

int main(){
    string s;
    int n, x;
    cin >> n >> x;
    for (int i = 0; i < 26; i++){
        for (int j = 0; j < n; j++){
            s.push_back('A' + i);
            /*cout << s << endl;*/
        }
    }
    cout << s[x-1] << endl; 


}