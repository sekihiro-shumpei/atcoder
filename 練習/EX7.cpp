#include<bits/stdc++.h>
using namespace std;

int main(){
    bool a = true;
    bool b = false;
    bool c = true;


    if (a) {
        cout << "At";
    }
    
    if (!b || c){
        cout << "Co";
    }

    if (!a || c){
        cout << "der";
    }

    cout << endl;

}