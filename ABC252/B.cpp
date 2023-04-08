#include<bits/stdc++.h>
using namespace std;

int main(void){
    int n, k, ans = 0;
    int a[100];
    int b[100];

    cin >> n >> k;
    for (int i = 0; i < n; i++){
        cin >> a[i];
    } 
    for (int i = 0; i < k; i++){
        cin >> b[i];
    }

    for (int i=0; i < n; i++){
        ans = max(ans, a[i]);
    }

    for (int i = 0; i < k; i++){
        if (a[b[i] - 1] == ans){
            cout << "Yes" << endl;
            return 0;
        }
    }

    cout << "No" << endl;



}