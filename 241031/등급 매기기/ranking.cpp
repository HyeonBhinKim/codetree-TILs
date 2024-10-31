#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int n;
    cin>>n;
    if (n<60) 
        cout<<"F";
    else if (n<70)
        cout<<"D";
    else if (n<80)
        cout<<"C";
    else if (n<90)
        cout<<"B";
    else
        cout<<"A";
    return 0;
}