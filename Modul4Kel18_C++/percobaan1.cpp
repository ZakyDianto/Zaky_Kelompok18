#include <iostream>
using namespace std;

void penjumlahan(int a, int b) {
int c = a + b;
    cout << "Hasil penjumlahan: " << c <<endl;
}

void pengurangan() {
    int c = 10 - 20;
    cout << "Hasil pengurangan: " << c <<endl;
}

int pembagian(int a, int b) {
    int c = a / b;
    return c;
}

int perkalian() {
    int c = 10 * 20;
    return c;
}

int main() {

    penjumlahan(10,20);

    pengurangan();

    perkalian();
    cout << "Hasil perkalian: " << perkalian() <<endl;

    int d = pembagian(100,20);
    cout << "Hasil pembagian: " << d;
    
    return 0;
    }