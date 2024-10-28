#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double a;
    cin>>a;
    if (a<0.5){
        cout<<"Low";
    }
    else if (a<1){
        cout<<"Middle";
    }
    else{
        cout<<"High";
    }
    return 0;
}