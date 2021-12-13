#include <stdio.h>
#define NSAMPLES 8 // MM
#define K 20 // COEF DESEJADOS

int main() {
    
    FILE *in_file, *out_file, *out_erro;
    int n_amost = 0, i = 0;
    short entrada, saida;
    double coefW[K]= {0x0};
    short sample[K] = {0x0};
    float d = 0, y = 0; 
    double erro = 0;
    double u = 0.0000000005;
    int n = 0;

    float coef[NSAMPLES] = {
        #include "Coefs_MM_8.dat" // MM -> 8
    };

    if ((in_file = fopen("..\\ruido_branco.pcm", "rb")) == NULL){ // Sinal de entrada
        printf("\nErro: Nao abriu o arquivo de entrada\n");
        return 0;
    }

    if ((out_file = fopen("..\\saida_teste.pcm", "wb")) == NULL){ // Sinal de saida
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }
    if ((out_erro = fopen("..\\error.dat", "wb")) == NULL){ // Erro
        printf("\nErro: Nao abriu o arquivo de saida\n");
        return 0;
    }
    
    printf("***************************************************************\n");
	printf("* 					   Filtro LMS							  *\n");
	printf("*                                                             *\n");
	printf("***************************************************************\n");
	printf("\n");
	printf("Processando ...\n ");
	
    do {
        n_amost = fread(&entrada, sizeof(short), 1, in_file);

        sample[0] = entrada;

        d = 0; 
        for (n = 0; n < NSAMPLES; n++){ // Desejado
            d += coef[n] * sample[n];
        }

        y = 0;
        for (n = 0; n < K; n++){ // Atual
            y += coefW[n] * sample[n];
        }

        erro = d - y;

        if(i > K){ // Atualiza Coeficientes
            for(n = 0; n < K; n++){
                coefW[n] = coefW[n] + (u*erro*(sample[n]));
            }
        }

        for (n = K-1; n > 0; n--){ // Atualiza Sample
            sample[n] = sample[n-1];
        }

        saida = (short)y;
        fwrite(&saida, sizeof(short), 1, out_file);
        fprintf(out_erro, "\nErro: %f", erro);
        i++;
    } while (n_amost);
	
    printf("\nCoefs gerados!");
    for(n = 0; n < K; n++){
        printf("\n%f", coefW[n]);
    }

    fclose(out_erro);
    fclose(out_file);
    fclose(in_file);
    printf("\n\nFile ready!");
    return 0;
}