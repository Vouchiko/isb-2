#include <iostream> 

int main(int argc, char *argv[])
{
    int x = std::rand() % 12347;
    int N = 128;
    bool b;
    for(int i = 0; i < N; i++) {
        x = (x * 222 + 4) % 12347;
        b = x % 2;
        std::cout << b;
    }
    return 0;
}