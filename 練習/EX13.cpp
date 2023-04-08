#include<bits/stdc++.h>
using namespace std;

int main() {
    int N;
    cin >> N;

    vector<int> A(N);

    for (int i = 0; i < N; i++){
        cin >> A.at(i);
    }

    int sum = 0;
    for (int i = 0; i < N; i++){
        sum += A.at(i);
    }

    int avg, ans;
    avg = sum / N;

    for (int i = 0; i < N; i++){
        if (A.at(i) < avg){
            ans = avg - A.at(i);
            cout << ans << endl;
            //ans = 0;
        }
        else{
            ans = A.at(i) - avg;
            cout << ans << endl;
            //ans = 0;
        }

    }

}