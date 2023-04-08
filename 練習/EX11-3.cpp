#include<bits/stdc++.h>
using namespace std;

int main(){
    int N;
    string S, ans;

    cin >> N;

    for (int i=0; i < N; i++){

        cin >> S;
        if (S == "Y"){
            ans = "Four";
            break;
        }
        else{
            ans = "Three";
        }
    }
    cout << ans << endl;
     
}