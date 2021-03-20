#include <iostream>
using namespace std;

int main()
{
    cout << "Вычисление стоимости покупки. " << endl;
    cout << "Введите исходные данные :" << endl;

    float cn, nn, cp, np, s;
    cout << "Цена тетради(руб.) -> ";
    cin >> cn;
    cout << "Количество тетрадей-> ";
    cin >> nn;
    cout << "Цена карандаша(руб.)-> ";
    cin >> cp;
    cout << "Количество карандашей-> ";
    cin >> np;
    cout << "Стоимость покупки: ";
    cout << cn * nn + cp * np << endl;
}