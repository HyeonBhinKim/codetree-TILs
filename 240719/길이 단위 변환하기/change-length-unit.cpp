#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    double ft = 30.48, mi = 160934, x = 9.2, y= 1.3;

    cout<<fixed;
    cout.precision(1);
    cout << x <<"ft = "<< x*ft << "cm" << endl;
    cout << y <<"mi = "<< y*mi << "cm" << endl;
    

    return 0;
}