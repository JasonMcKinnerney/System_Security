
#include <iostream>
using namespace std;
static int cnt=0;
int dexp(unsigned int x, unsigned int y, int n)  
{  
    int res = 1;
    x = x % n;
    if (x == 0) return 0;
    while (y > 0){  
        // If y is odd, multiply x with result  
        if (y & 1)  //used to check large numbers and is faster
            res = (res*x) % n;  
  
  //else make y even
        y = y/2;  
        x = (x*x) % n;  
        cnt++;
    }  
    return res;  
}
int main() 
{
    int result=dexp(35,77,83);
    cout << result<<endl;
    cout<<"Total no of multiplications required were: "<<cnt-1<<endl;
    
    return 0;
}