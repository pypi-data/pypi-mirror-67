
#include <fstream>
#include <iostream>
#include <vector>

#include <chrono>
#include <thread>

#include "bgen.h"
#include "header.h"
#include "samples.h"
#include "variant.h"

int main() {
  // std::string path = "/users/jmcrae/ukb_imp_chr21_v3.bgen";
  // std::string path = "/users/jmcrae/ukb_imp_chrXY_v3.bgen";
  std::string path = "/users/jmcrae/bgen/tests/data/complex.5bits.bgen";
  auto time_1 = std::chrono::high_resolution_clock::now();
  bgen::Bgen bgen_file(path);
  auto time_2 = std::chrono::high_resolution_clock::now();
  std::cout << "file load: " << std::chrono::duration_cast<std::chrono::milliseconds>(time_2 - time_1).count() << std::endl;
  
  // auto rsids = bgen_file.rsids();
  // // std::vector<int> to_drop = {0, 1};
  // // bgen_file.drop_variants(to_drop);
  //
  // // auto var = bgen_file[20000];
  // // std::cout << var.chrom << ":" << var.pos << "\n";
  //
  // int i = 0;
  for (auto var : bgen_file.variants) {
    std::cout << "\n" << var.rsid << " " << var.chrom << ":" << var.pos << ", n_alleles: " << var.n_alleles << "\n";
    auto geno = var.probs_1d();
  }
  //   i++;
  //   std::cout << var.rsid << " " << i << "\n";
  //   auto time_a = std::chrono::high_resolution_clock::now();
  //  auto geno = var.probabilities();
  //   auto time_b = std::chrono::high_resolution_clock::now();
  //   auto & minor_allele_dosage = var.minor_allele_dosage();
  //   auto time_c = std::chrono::high_resolution_clock::now();
  //   // std::cout << " - parse genotypes: " << std::chrono::duration_cast<std::chrono::milliseconds>(time_b - time_a).count() << std::endl;
  //   std::cout << " - get alt dosage: " << std::chrono::duration_cast<std::chrono::milliseconds>(time_c - time_b).count() << std::endl;
  //   // std::cout << " - dosage size: " << alt_dosage.size() << std::endl;
  //
  //   // double total = 0;
  //   // for (auto d : alt_dosage) {
  //   //   total += d;
  //   // }
  //   // double mean_dosage = total / (double) alt_dosage.size();
  //   // std::cout << " - dosage mean: " << mean_dosage << std::endl;
  //
  //   // for (auto d : alt_dosage ) {
  //   //   std::cout << d << "\n";
  //   // }
  //   // break;
  // }
  //
  // std::cout << bgen_file.variants.size() << std::endl;
  // std::cout << "sleeping after parsing file" << std::endl;
  // std::this_thread::sleep_for(std::chrono::seconds(20));
}


// set zstd_common (find zstd/lib/common -name "*.c")
// set zstd_compress (find zstd/lib/compress -name "*.c")
// set zstd_decompress (find zstd/lib/decompress -name "*.c")
// set zstd_builder (find zstd/lib/dictBuilder -name "*.c")
// set zstd_deprecated (find zstd/lib/deprecated -name "*.c")
// set zstd_legacy (find zstd/lib/legacy -name "*.c")
// set zstd_c_code $zstd_common $zstd_compress $zstd_decompress $zstd_builder $zstd_deprecated $zstd_legacy
//
// gcc -c -lm -std=gnu11 \
//   -Izstd/lib \
//   -Izstd/lib/common \
//   -Izstd/lib/compress \
//   -Izstd/lib/decompress \
//   -Izstd/lib/dictBuilder \
//   -Izstd/lib/deprecated \
//   -Izstd/lib/legacy \
//   $zstd_c_code
//
// gcc -lm -lz -lzstd -std=c++11 -lstdc++ -Izstd/lib -Izstd/lib/common -Lzstd/lib/ \
//   main.cpp bgen.cpp genotypes.cpp header.cpp samples.cpp utils.cpp variant.cpp \
//   *.o
