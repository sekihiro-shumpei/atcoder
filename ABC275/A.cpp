#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    int h[100];
    int ans = 0;

    cin >> n;
    for(int i = 0; i < n; i++){
        cin >> h[i];
    }

    for(int i = 0; i < n; i++){
        if (h[ans] < h[i]){
            ans = i;
        }
    }

    cout << ans + 1 << endl;


}