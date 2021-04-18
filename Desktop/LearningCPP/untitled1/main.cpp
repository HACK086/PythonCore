#include <iostream>
#include <vector>
#include <string>
using namespace std;
// пример 1
/*void PrintVector(const vector<string>& vec){
    for (auto s : vec){
        cout << s << endl;
    }
}
int main(){
    int n;
    cin >> n;
    vector <string> vec(n);
    for (auto& s : vec){
    cin >> s;
    }

    PrintVector(vec);

    return 0;
}*/


// пример 2

void PrintVector(const vector<bool>& d){
    for (auto s : d){
        cout << s << endl;
    }
}
/*
int main(){
    vector <int> days_in_months = {31, 28, 31, 30, 31};
        if (true) {
            days_in_months[1]++;
        }
    PrintVector(days_in_months);

    return 0;}*/
// пример 3
int main(){
    vector <bool> holiday( 28, false);
    holiday[22] = true;
    PrintVector(holiday);
    return 0;
}