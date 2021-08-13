#include <iostream>
#include <vector>
#include <string>
#include <cmath>
#include <algorithm>
#include <ctime>
using namespace std;


/*
# # Инициализируем переменные
# i - время
# r - секунды, когда взрослый находился в зоне видимости ребенка
# k - секунды, когда ребенок находился в зоне видимости взрослого
# reb - зона видимости ребенка
# vzr - зона видимости взрослого
# x1 - координата взрослого на оси X
# y1 - координата взрослого на оси Y
# х2 - координата ребенка на оси Х
# y2 - координата ребенка на оси Y
#1)Прибавляем к времени 1 секунду
#2)Рассматриваем вариант конца времени(tmax=t?)
#3)Сгенерируем число от 1 до 4(для ребенка и взрослого)
#4)Обновляем координаты, обращая внимание на направление
#5)Рассматриваем варианты выхода субъекта за территорию(для ребенка и взрослого)
#6)Вычисляем расстояние между взрослым и ребенком
#7)Варианты видимости ребенка взрослого и наоборот
*/

double length( int x1, int y1, int x2, int y2 )
{
    return sqrt( (x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1) );
}

int walk(){
    int i=0, r=0, k=0, reb =80,vzr =40,x=300,y=300,x1=1,x2=300,y1=1,y2=300,c=0;
    int t = 1;
    while (t <= 600){
        t += 1;

        srand(time(0));
        int object1 = rand() % 4 +1;
        srand(time(0));
        int object2 = rand() % 4 +1;

        //4
        if (object1 % 2 == 1){
        x1 = x1 + 1;}

        else if (object1 % 2 == 0){
        y1 = y1 + 1;}

        if (object2 % 2 == 1){
        x2 = x2 - 1;}

        else if (object2 % 2 == 0){
        y2 = y2 - 1;}
        //5
        if (x1 == 301){
        x1 = 1;}
        else if (x1 == -1){
        x1 = 299;}
        if (y1 == 301){
        y1 = 1;}
        else if (y1 == -1){
        y1 = 299;}
        if (x2 == 301){
        x2 = 1;}
        else if (x2 == -1){
        x2 = 299;}
        if (y2 == 301){
        y2 = 1;}
        else if (y2 == -1){
        y2 = 299;}

        //6
        c = length(x1, y1, x2, y2);

        //7
        if (c <= reb){
        r = r + 1;}
        else {return r;}

        if (c <= vzr){
        k = k + 1;}
        else {return k;}

    }
}
int main(){
    int n = 100, p=0.95,ts = 1.644854;
    int midr=0,midk=0,rw2=0,kw2=0;
    for(int l=0;l<=n;n++){
        int rw = walk(), kw = walk();
        midr += rw;
        midk += kw;
        rw2 += rw*rw;
        kw2 += kw*kw;
    }
    midr = midr / n;
    midk = midk / n;
    int sr = sqrt((rw2 - n * midr*midr) / (n - 1));
    int sk = sqrt((kw2 - n * midk*midk) / (n - 1));
    int pin_r = sr * ts / sqrt(n);
    int pin_k = sk * ts / sqrt(n);
    cout << midr << "+-" << pin_r;
    cout << midk << "+-" << pin_k;
    return 0;
}