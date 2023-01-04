#include<stdio.h>
#include<stdlib.h>
#include <time.h>

/*
n : nombre de disques utilisés
D : emplacement de départ
A : emplacement d'arrivée
I : emplacement intermédiaire
*/

void toursHanoi(int n, char D, char A, char I) {
    if (n == 1)
      printf("Disque 1 de %c a %c \n" , D , A);
    else {
      // D à A
      toursHanoi(n - 1, D, I, A);
      printf("Disque %d de %c a %c \n", n , D ,A);
      //I à A
      toursHanoi(n - 1, I, A, D);
    }
}
//test matestithach aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa
//AVEC ET SANS AFFICHAGE
void Temps_execution(int T[10],int n){
    float T2[10];
    float temps;
    clock_t t1, t2;
    for(int i=0;i<n;i++){
        t1 = clock();
        toursHanoi(T[i], 'A', 'B', 'C');
        t2 = clock();
        temps = (float)(t2-t1)/CLOCKS_PER_SEC;
        T2[i]=temps;
       printf("pour %d disque temps :%f \n",n,T2[i]);
    }
}
void main() {
    // int nDisques = 3;
    // toursHanoi(nDisques, 'A', 'B', 'C');
    // system("pause");

    int n=12;
    float temps;
    clock_t t1, t2;
    int T[10];


    for (int i=0;i<n;i++){
      T[i]=i+1;
    }
    

    Temps_execution(T,n);
  //   while(1)
  // {
  //   printf("Entrer n : ");
  //   scanf("%d",&n);
  //   printf("\n");
  //   if (n>0){ 
  //     t1 = clock();
  //     toursHanoi(n, 'D', 'A', 'I');}
  //     t2 = clock();
  //     temps = (float)(t2-t1)/CLOCKS_PER_SEC;
  //     printf("temps = %f\n", temps);
  // }


}