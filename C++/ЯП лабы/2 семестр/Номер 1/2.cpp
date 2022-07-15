#include <iostream>
using namespace std;
int main(){
    float a, b, c, ob;
    cout << "Вычисление площади поверхности параллелепипеда. Введите исходные данные:"<< endl;
    cout <<"Длина (см) -> ";
    cin >> a;
    cout << "Ширина (см) -> ";
    cin >> b;
    cout << "Высота (см) -> ";
    cin >> c;
    ob=2*(a*b+b*c+a*c);
    cout << "Площадь поверхности: "<< ob <<" кв.см."<< endl;
}