#include<iostream>
using namespace std;
int main(){
unsigned short shifts[] = {
    1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1
};
int KS[6][48];
int r=6;
int PC2[] = {
    14, 17, 11, 24, 1, 5,
    3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8,
    16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55,
    30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53,
    46, 42, 50, 36, 29, 32
};
int CD[] = {0,1,1,0,1,1,1,0,0,1,0,1,1,1,1,0,0,1,1,1,1,0,1,1,1,0,0,0,0,0,0,0,1,0,1,0,0,1,1,0,1,1,0,1,0,1,1,1,1,1,0,1,1,0,0,1};
int i, j, k, t1, t2; 
for ( i=0; i<r; i++) { /**--*/
        /* Rotate C and D */
        for (j =0; j <shifts[i]; j++) {
            t1 = CD[0];
            t2 = CD[28];
            for ( k=0; k<27; k++) {
                CD[k] = CD[k+1];
                CD[k+28] = CD[k+29];
            }
            CD[27] = t1;
            CD[55] = t2;
        }
        /* Set the order of subkeys for type of encryption */
        j = r-1-i;   /**--*/
        cout<< "round"<<j+1 <<" key:";  
        /* Permute C and D with PC2 to generate KS[i] */
        for (k=0; k< 48 ; k++) { KS[j][k] = CD[PC2[k] -1];
           cout<<KS[j][k]; 
        }
    cout<<endl;
}
}