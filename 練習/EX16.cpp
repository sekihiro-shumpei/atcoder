#include<bits/stdc++.h>
using namespace std;

int main() {
    vector<int> data(5);
    for (int i = 0; i < 5; i++){
        cin >> data.at(i);
    }
    int cnt = 0;
    for (int i= 0; i < 4; i++){
        if (data.at(i) == data.at(i + 1)){
            cout << "YES" << endl;
            break;
        }
        cnt += 1;
        if(cnt == 4){
            cout << "NO" << endl;
        }
    }
}
