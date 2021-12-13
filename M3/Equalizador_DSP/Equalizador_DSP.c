#include <stdio.h>
#include <string.h>
#include <cycles.h>


#define NSAMPLES 320

float coefPB[NSAMPLES] = {
	#include "Coef_PB.dat" // Coeficiente Passa Baixa 
}; 
float coefPA[NSAMPLES] = {
	#include "Coef_PA.dat" // Coeficiente Passa Alta 
};
float coefPF[NSAMPLES] = {
	#include "Coef_BP.dat" // Coeficiente Passa Faixa 
};


extern short proc_alg( float *, short *, int);

int main(int argc,char *argv[])
{
 	cycle_stats_t stats;   
	FILE *fin,*fout;
	
	short entrada, saida;
	float saidaPB, saidaPA, saidaBP;

  	short Vet_entr[NSAMPLES]= {0x0};
  	
  	int PB_input = 1, PA_input = 1, BP_input = 1;
	int i;
	
	printf("***************************************************************\n");
	printf("* 						EQUALIZADOR							  *\n");
	printf("*                                                             *\n");
	printf("***************************************************************\n");
	printf("\n");
	
	
	fin = fopen("..\\sweep_100_2k.pcm","rb");
    if ((fin)==NULL){
    	printf("\nErro: nao abriu o arquivo de Entrada\n");
    	return 0;
  	}
    fout = fopen("..\\sai_PBPABP.pcm","wb");
    if ((fout)== NULL){
    	printf("\nErro: nao abriu o arquivo de Saida\n");
    	return 0;
  	}
  	
  	CYCLES_INIT(stats);
  		
  printf("Processando ...\n ");
	
  while (fread(&entrada,sizeof(short),1,fin) == 1){
  		
  		Vet_entr[0] = entrada;
  		
		CYCLES_START(stats);	
		
		saidaPB = proc_alg( coefPB, Vet_entr, NSAMPLES);
		saidaPA = proc_alg( coefPA, Vet_entr, NSAMPLES);
		saidaBP = proc_alg( coefPF, Vet_entr, NSAMPLES);
		
		saida = (saidaPB * PB_input) + (saidaPA * PA_input) + (saidaBP * BP_input);

		CYCLES_STOP(stats);
		fwrite(&saida,sizeof(short),1,fout);	
			
	}

    printf("terminado!\n");
		
    
	CYCLES_PRINT(stats);
	fclose(fin);
	fclose(fout);
		
    return 0;
}


