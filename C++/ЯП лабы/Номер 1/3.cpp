#include <iostream>
#include <cmath>

using namespace std;

int main()
{
    float a;
    cout << "Вычисление объема куба." << endl;
    cout << "Введите длину ребра(см) -> ";
    cin >> a;
    a = pow(a, 3);
    cout << "Объем куба: " << a << " куб.см." << endl;
}