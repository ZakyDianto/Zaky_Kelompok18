<?php
    class MyClass {
         // Method dengan return type
        public function hitungAkar($nilai) {
            return sqrt($nilai);
        }
        // Method tanpa return type (menggabungkan data)
        public function cetakProfil($nama, $umur) {
            echo "Nama saya $nama <br>";
            echo "Umur saya $umur <br>";
            echo "Saya adalah seorang mahasiswa";
        }
    }
        
    // Pembuatan instance objek
    $objek = new MyClass();
        
    // Pemanggilan method menggunakan ->
    echo "Akar kuadrat dari 121 adalah: " . $objek->hitungAkar(121) . "<br><hr>";

    $objek->cetakProfil("Jeki", 18);
?>