#include<bits/stdc++.h>
using namespace std;

int main(){
    string cand[4] = {"ABC","AGC","AHC","ARC"};
    bool used[4] = {};
    string str;
    for (int i = 0; i < 3; i++){
        cin >> str;
        for (int j = 0; j < 4; j++){
            if (cand[j] == str){
                used[j] = true;
            }
        }
    }
    for (int i = 0; i < 4; i++){
        if (!used[i]){
            cout << cand[i] << endl;
        }
    }

}