#include <iostream>
#include <fstream>
using namespace std;

int main()
{
    ifstream in;  // Поток in будем использовать для чтения
    ofstream out; // Поток out будем использовать для записи
    in.open("input.txt");
    out.open("output.txt");
}