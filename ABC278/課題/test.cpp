#include<bits/stdc++.h>
using namespace std;

int main(){
   int arr[] ={2, 8, 2, 1, 3, 3, 3, 9, 5, 4};
   int ans=0;

    for (int i = 0; i < 10; i++){
        for(int j = 0; j < 10; j++){
            if (i == arr[j]){
                break;
            }
            if(j == 9){
                ans += 1;
            }

        }
    }
    cout << ans << endl;
    
}