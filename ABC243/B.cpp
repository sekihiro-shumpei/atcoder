#include<bits/stdc++.h>
using namespace std;

int main(){
    int n;
    cin >> n;
    vector<int> a(n); 
    vector<int> b(n); 

    for (int i = 0; i < n; i++){
        cin >> a[i];
    }
    for (int i = 0; i < n; i++){
        cin >> b[i];
    }
    int ans1 = 0, ans2 = 0;
    for (int i = 0; i < n; i++){
        for (int j = 0; j < n; j++){
            if (a[i] == b[j]){
                if (i == j){
                    ans1 += 1;
                }
                else{
                    ans2 += 1;
                }
            }
        }
    }
    cout << ans1 << endl;
    cout << ans2 << endl;
}