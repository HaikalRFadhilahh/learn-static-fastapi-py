from model.universitas import Universitas
from model.programStudi import ProgramStudi
from model.mahasiswa import Mahasiswa
from typing import List

Data: List[Universitas] = [
    Universitas(
        kodeUniversitas="AMIKOM",
        namaUniversitas="Universitas Amikom Yogyakarta",
        akreditasi="Unggul",
        alamat="Condong Catur, Sleman, Yogyakarta",
        programStudi=[
            ProgramStudi(
                kodeProgramStudi="IF",
                namaProgramStudi="Sarjana Teknik Informatika",
                akreditasi="Baik Sekali"
            ),
            ProgramStudi(
                kodeProgramStudi="SI",
                namaProgramStudi="Sarjana Sistem Informasi",
                akreditasi="Unggul"
            ),
            ProgramStudi(
                kodeProgramStudi="AR",
                namaProgramStudi="Sarjana Arsitektur",
                akreditasi="A"
            ),
            ProgramStudi(
                kodeProgramStudi="MTI",
                namaProgramStudi="Magister Teknik Informatika",
                akreditasi="Baik Sekali"
            )
        ]
    ),
    Universitas(
        kodeUniversitas="UGM",
        namaUniversitas="Universitas Gadjah Mada",
        akreditasi="Unggul",
        alamat="Bulak Sumur, Yogyakarta, Yogyakarta",
        programStudi=[
            ProgramStudi(
                kodeProgramStudi="DIKE",
                namaProgramStudi="Sarjana Ilmu Komputer",
                akreditasi="Unggul"
            ),
            ProgramStudi(
                kodeProgramStudi="FAPERTA",
                namaProgramStudi="Sarjana Pertanian",
                akreditasi="Unggul"
            )
        ]
    )
]

DataMahasiswa: List[Mahasiswa] = [
    Mahasiswa(npm="21.11.3910",
              namaMahasiswa="Haikal Raditya Fadhilah",
              angkatan=2021,
              domisili="Yogyakarta",
              universitas=Data[0]),
    Mahasiswa(npm="21.11.391x",
              namaMahasiswa="Fadli",
              angkatan=2021,
              domisili="Yogyakarta",
              universitas=Data[0])
]