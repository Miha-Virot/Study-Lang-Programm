#include <iostream>
#define _USE_MATH_DEFINES // for C++
#include <cmath>
using namespace std;

int main()
{
    float r, h, o;
    cout << "Вычисление объема цилиндра." << endl;
    cout << "Введите исходные данные:" << endl;
    cout << "Радиус основания(см) -> ";
    cin >> r;
    cout << "Высота цилиндра(см) -> ";
    cin >> h;
    o = M_PI * pow(r, 2) * h;
    cout << "Объем цилиндра:" << o << " см.куб." << endl;
}