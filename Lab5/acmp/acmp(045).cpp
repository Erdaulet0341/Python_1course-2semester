#include <iostream>
 
using namespace std;
int main()
{
    int n;
    cin >> n;
    if(0 == n){
        cout << 10;
        return 0;
         
    }
    if(n == 1){
        cout << 1;
        return 0;
         
    }
     
    int a[10];
    for(int i =  0; i < 10; ++i)
        a[i] = 0;
    for(int i = 9; i > 1; --i){
        while((n % i)==0){ 
            n/=i;
            a[i]++;
        }
    }
    if(n == 1){
        for(int i = 2; i <= 9; ++i){
            while(a[i]){
                a[i]--;
                cout << i;
            }
        }
    }
    else
        cout << -1;
    return 0;
}