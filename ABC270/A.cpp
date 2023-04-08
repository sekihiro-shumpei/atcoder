#include<bits/stdc++.h>
using namespace std;

int main() {
    int a, b;
    cin >> a >> b;
    if (a+b == 2 or a+b == 1){
        cout << 1 << endl;
    }
    else if(a+b==2 or (a+b==4 and (a==2 and b==2))){
        cout << 2 << endl;
    }
    else if(a+b==3 or a+b==4 or (a+b==6 and ((a==4 and b==2) or (b == 4 and a==2)))) {
        cout << 3 << endl;
    }
    else if(a+b==4 or (a+b==8 and (a == 4 and b == 4))){
        cout << 4 << endl;
    }
    else if(a+b==6 or (a+b==8 and ((a==4 and b==2) or (b==4 and a==2))) or a+b==12){
        cout << 6 << endl;
    }
    else if(a+b==7 or a+b==8 or a+b==10 or a+b==14){
        cout << 7 << endl;
    }
    else{
        cout << 0 << endl;
    }
}

テストケース３つが通らない。未解決なりけり。