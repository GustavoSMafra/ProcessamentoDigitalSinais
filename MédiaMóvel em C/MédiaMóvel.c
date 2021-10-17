#include <stdio.h>
#include <fcntl.h>
#include <io.h>
#define NSAMPLES 4 

int main() {
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = {0x0};
    float y = 0;

    float coef[NSAMPLES] = {
        #include "Coefs_mm_4.dat"
    };


    if ((in_file = fopen("sweep_100_2k.pcm", "rb")) == NULL){
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }

    if ((out_file = fopen("sai_sweep_mm_4.pcm", "wb")) == NULL){
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }

    for (i = 0; i < NSAMPLES; i++){
        sample[i] = 0;
    }

    do {
        y = 0;                                             
        n_amost = fread(&entrada, sizeof(short), 1, in_file);
        sample[0] = entrada;
        for (n = 0; n < NSAMPLES; n++){
                y += coef[n] * sample[n];
        }
        for (n = NSAMPLES - 1; n > 0; n--){
                sample[n] = sample[n - 1];
        }
        saida = (short)y;

        fwrite(&saida, sizeof(short), 1, out_file);
    } while (n_amost);

    fclose(out_file);
    fclose(in_file);
    return 0;
}