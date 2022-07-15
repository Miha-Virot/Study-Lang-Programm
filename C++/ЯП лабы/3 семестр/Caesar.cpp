#include <iostream>
#include <string>

class Caesar ()
{
    private:
        int i, key;
        string message, crypt;
        char list [28] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    public:
        Caesar ()
        {
            this->key = 0;
            this->message = ""; // указатель "this" указывает что именно менять надо приватную переменную, а не ту что в методе используется
            /*
            key = random();
            message = random();
            */ 
            // тут буду испльзовать рандомайзер, спец функцию
        }
        void printData ()
        {
            cout << this->key << this->message;
        }
        ~Caecar ()
        {
            delete this->i, this->key, this->message, this->crypt;
        }
}

int main () 
{
    Caesar one();
    one.printData;
    delete one; // удалить объект, требуется уточнить про область видимости и 
    return 0;
}
