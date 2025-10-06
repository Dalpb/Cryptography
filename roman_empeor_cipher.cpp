#include <iostream>
using namespace std;
// This code is for solve the roman cipher
// My introduction to cryptography


int lim = 26;
// to create the abc
char* createABC() {
    char *abc = new char[lim];
    abc[0] = 'a';
    for(int i = 1; i < lim; i++){
        abc[i] = abc[i-1] + 1;
    }
    return abc;
}
char *abc = createABC();

//search the chiperchar's position and transform
char cipherCharRoman(char chiperchard,int shift){
    for(int i = 0; i < lim; i++){
        if(chiperchard != abc[i])continue;
        int j = (i + shift) % lim;
        if( j < 0) j += lim; 
        return abc[j];
    }
    return '#';
}
void solve(const char *cipherword,int shift) {
    for(int i = 0; cipherword[i] != '\0';i++){
        if(cipherword[i] == '_'){
            cout <<" ";
            continue;
        }
        char realchar = cipherCharRoman(cipherword[i],shift);
        cout<<realchar;
    }
    cout<<endl;
}

int main(int argc, char** argv){
    if(argc != 3 ){
        cout << "Use roman_empeor_cipher.o #cipher_word #shift "<<endl;
        return 0;
    }
    int shift = atoi(argv[2]);
    solve(argv[1],shift);
    return 0;
}