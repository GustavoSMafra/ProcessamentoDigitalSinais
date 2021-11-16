#include <stdio.h>
#include <fcntl.h>
#include <io.h>
#define NSAMPLES 882

int main() {
    FILE *in_file, *out_file;
    int i, n, n_amost;

    short entrada, saida;
    short sample[NSAMPLES] = {0x0};
    float PB = 0, PA = 0, PF = 0, TOTAL = 0; 
    int PB_input = 0, PA_input = 1, PF_input = 0;

    float coefPB[NSAMPLES] = {
        #include "Coef_PB.dat" // Coeficiente Passa Baixa -> 3k5
    };
    float coefPA[NSAMPLES] = {
        #include "Coef_PA.dat" // Coeficiente Passa Alta -> 6k5
    };
    float coefPF[NSAMPLES] = {
        #include "Coef_BP.dat" // Coeficiente Passa Faixa -> 3k5 até 6k5
    };


    if ((in_file = fopen("humble.pcm", "rb")) == NULL){
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }

    if ((out_file= fopen("saida_musica_PA.pcm", "wb")) == NULL){ 
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }


    for (i = 0; i < NSAMPLES; i++){
        sample[i] = 0;
    }

    do {
        PB = 0; 
        PA = 0; 
        PF = 0; 
        TOTAL = 0;
                                              
        n_amost = fread(&entrada, sizeof(short), 1, in_file);
        sample[0] = entrada;

        for (n = 0; n < NSAMPLES; n++){
            if(PB_input == 1){
                PB += coefPB[n] * sample[n];
            }
            if(PA_input == 1){
                PA += coefPA[n] * sample[n];
            }
            if(PF_input == 1){
                PF += coefPF[n] * sample[n];
            }  

            TOTAL = PB + PA + PF;

        }
        for (n = NSAMPLES - 1; n > 0; n--){
                sample[n] = sample[n - 1];
        }
        saida = (short)TOTAL;
        fwrite(&saida, sizeof(short), 1, out_file);

    } while (n_amost);

    fclose(out_file);
    fclose(in_file);
    printf("File ready!");
    return 0;
}