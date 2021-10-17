#include <iostream>
#include <fcntl.h>
#include <vector>
#include <io.h>
using namespace std;

#define A0 0.5
#define A1 0.3
#define D  0.5
#define FS 8000
#define NSAMPLES (D*FS)


int main() {
    FILE *in_file, *out_file;
    int n_amost, tam_entrada = 0;
    short entrada; 
    vector <short> vetor_entrada; 
    vector <short> vetor_saida;

    if ((in_file = fopen("voz.pcm", "rb")) == NULL){
        cout << "\nErro: Nao abriu o arquivo de entrada\n";
        return 0;
    }

    if ((out_file = fopen("voz_eco.pcm", "wb")) == NULL){
        cout << "\nErro: Nao abriu o arquivo de saida\n";
        return 0;
    }

    do {
        n_amost = fread(&entrada, sizeof(short), 1, in_file);
        vetor_entrada.push_back(entrada);
        cout << "\nIndice ->  " << tam_entrada << " valor = " << vetor_entrada[tam_entrada];
        tam_entrada++;
    } while (n_amost);

    for(int i = 0; i<tam_entrada; i++){
        if(i - NSAMPLES > 0){
            vetor_saida.push_back(A0 * vetor_entrada[i] + A1* vetor_saida[i - NSAMPLES]);
        } else {
            vetor_saida.push_back(A0 * vetor_entrada[i]);
        }
        fwrite(&vetor_saida[i], sizeof(short), 1, out_file);
    }

    fclose(out_file);
    fclose(in_file);
    return 0;
}
