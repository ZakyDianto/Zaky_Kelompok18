#include <iostream>
using namespace std;

class matematika1 {
    public:
        void penjumlahan(int a, int b) {
        int c = a + b;
            cout << "Hasil penjumlahan: " << c <<endl;
        }
        void pengurangan() {
        int c = 10 - 20;
            cout << "Hasil pengurangan: " << c <<endl;
        }
};

class matematika2 {
    public:
        int pembagian(int a, int b) {
            int c = a / b;
        return c;
        }
        int perkalian() {
            int c = 10 * 20;
        return c;
    }
};

int main() {
    matematika1 objek1;
        objek1.penjumlahan(10,20);
        objek1.pengurangan();
    matematika2 objek2;
        cout << "Hasil perkalian: " << objek2.perkalian() <<endl;
        
        int d = objek2.pembagian(100,20);
        cout << "Hasil pembagian: " << d;
    return 0;
}