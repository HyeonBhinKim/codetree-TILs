#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    cout << fixed;
    double a,b,c;
    cin>>a>>b;
    c = (a+b) / (a-b); 
    cout.precision(2);
    cout << c;

    return 0;
}