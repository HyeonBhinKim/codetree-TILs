#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double a,b;
    cin>>a>>b;
    if (1.0<=a && 1.0<=b){
        cout<<"High";
    }
    else if (0.5<=a && 0.5<=b){
        cout<<"Middle";
    }
    else
        cout<<"Low";
    return 0;
}