<?php
function jumlahkan($a, $b) {
    return $a + $b;
}

$x = 50;
$y = 30;
$hasil_return = jumlahkan($x, $y);

echo "Hasil function return: $hasil_return <br><hr>";

function cetak_jumlah($a, $b) {
    $hasil = $a + $b;
    echo "Hasil function non-return: $hasil";
}

cetak_jumlah($x, $y);
?>