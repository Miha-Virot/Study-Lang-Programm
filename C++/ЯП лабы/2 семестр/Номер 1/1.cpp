#include <iostream>
using namespace std;

int main(){
    float dlina, shirina, visota, obiem;
    cout << ("Вычисление объема параллелепипеда. ") <<endl;
    cout << "Введите исходные данные:" << endl;
    cout << "Длина (см) -> ";
    cin >> dlina;
    cout << "Ширина (см) -> ";
    cin >> shirina;
    cout << "Высота (см) -> ";
    cin >> visota;
    obiem = dlina * shirina * visota;
    cout << "Объем: " << obiem << " куб.см.";
}