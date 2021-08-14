#include <iostream>
#include <ctime>
#include <cmath>
#include <algorithm>
/*
# # Инициализируем переменные
# i - время
# reb - секунды, когда взрослый находился в зоне видимости ребенка
# vzr - секунды, когда ребенок находился в зоне видимости взрослого
# d - зона видимости
# raz - размер поля
#1)Рассматриваем вариант рандомного движения
#2)Вычисляем расстояние между взрослым и ребенком
#3)Рассматриваем вариант конца времени
#4)Рассматриваем варианты выхода субъекта за территорию(для ребенка и взрослого)
#5)Варианты видимости ребенка взрослого и наоборот
#6)Повторяем эксперимент 100 раз
*/
using namespace std;
int vzr = 0;
int reb = 0;
int raz = 300;

int randomMove(int x) {
    x += 2*(rand() % 2) - 1;
    if (x < 0) {
        x = raz;
    } else if (x > raz) {
        x = 0;
    }
    return x;
}

int distance(int x1, int y1, int x2, int y2) {
    int x = x2 - x1;
    int y = y2 - y1;
    return sqrt(x*x + y*y);
}

void moves() {
    int x1 = 0;
    int y1 = 0;
    int x2 = raz;
    int y2 = raz;
    for (int i = 0; i < 600; i++) {
        if (rand() % 2 == 0) {
            x1 = randomMove(x1);
        } else {
            y1 = randomMove(y1);
        }

        if (rand() % 2 == 0) {
            x2 = randomMove(x2);
        } else {
            y2 = randomMove(y2);
        }
        int d = distance(x1, y1, x2, y2);
        if (d <= 40) {
            vzr += 1;
        }
        if (d <= 80) {
            reb += 1;
        }
    }
}

int main()
{
    srand( time(0) );

    int count = 100;
    for (int i = 0; i < count; i++) {
        moves();
    }
    cout << "В среднем при заданных условиях взрослый видит ребенка - " << (float)vzr/count << " секунд "<<"\n";
    cout << "В среднем при заданных условиях ребенок видит взрослого - " <<(float)reb/count <<" секунд" << "\n";

    return 0;
}