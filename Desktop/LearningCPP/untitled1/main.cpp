#include <iostream>
#include <vector>
#include <string>
using namespace std;
void PrintVector(const vector<string>& vec){
    for (const auto& s : vec){
        cout << s << endl;
    }
}
void PrintVec(const vector<bool>& holiday){
    for (auto s : holiday){
        cout << s << "\n";

    }
}
int main() {
    int n;
    cout << "number of people : ";
    cin >> n;
    cout << "Name of people : ";
    vector<string> vec(n);
    for (auto &s : vec) {
        cin >> s;
    }
    PrintVector(vec);

    vector<int> days_in_months = {31, 28, 31, 30, 31};
    days_in_months[1]++;
    PrintVector(vec);
// также можно посмотреть размер вектора:
    cout << "Current size = " << vec.size() << endl;

    vector<bool> holiday(28, false);
    holiday[22] = true;
    PrintVec(holiday);

    // используем этот же вектор для мартовских праздников
    //мы можем расширить вектор с помощью resizeБ но тогда исходная часть кода останется нетронутым, поэтому пользуемся методом assign:
    holiday.assign(31, false);
    // и делаем выходной 8 марта:
    holiday[7] = true;
    cout << "\n" << "March : " << endl;
    PrintVec(holiday);
    // если захотим очистить вектор:
    holiday.clear();
// по индексу:
    vector <vector<string>> ind(10);
    ind[0].push_back("work");
    ind[0].push_back("job");
    cout << ind[0][1] << endl;
return 0;
}