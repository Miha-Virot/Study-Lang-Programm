#include <iostream>
using namespace std;

int main()
{
     float t, o, k, s;
     cout << "Вычисление стоимости покупки." << endl
          << "Введите исходные данные:" << endl;
     cout << "Цена тетради (руб.) -> ";
     cin >> t;
     cout << "Цена обложки (руб.) -> ";
     cin >> o;
     cout << "Количество комплектов (шт.) -> ";
     cin >> k;
     s = k * t + k * o;
     cout << endl
          << "Стоимость покупки: " << s << " руб." << endl;
     return 0;
}