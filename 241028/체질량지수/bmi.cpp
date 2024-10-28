#include <iostream>
using namespace std;

int main() {
    // 여기에 코드를 작성해주세요.
    int h,w;
    cin>>h>>w;
    cout<<10000*w/h/h<<endl;
    if((10000*w/h/h)>=25){
        cout<<"Obesity";
    }
    return 0;
}