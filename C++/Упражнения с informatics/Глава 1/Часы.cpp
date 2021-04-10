#include <iostream>
using namespace std;

int main()
{
    int h, m, s;
    double angle;

    cout << "Hours: ";
    cin >> h;
    cout << "Minutes: ";
    cin >> m;
    cout << "Seconds: ";
    cin >> s;

    angle = h * (double(360) / 12) + m * (double(360) / 12 / 60) + s * (double(360) / 12 / 60 / 60);
    if (angle >= 180)
    {
        cout << 360 - angle << endl;
    }
    else
    {
        cout << angle << endl;
    }
}