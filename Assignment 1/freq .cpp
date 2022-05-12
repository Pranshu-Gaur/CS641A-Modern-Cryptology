#include<bits/stdc++.h>
using namespace std;
int main(){

    string s;
    getline(cin,s);
    int n=s.size();
    int i=0;
    float cnt=0;
    float ch[26]={0};
    while(i<n){
       s[i]=tolower(s[i]); 
       if(s[i]<97 || s[i]>122){
         cnt++;
         i++;
         continue;
       }   
       ch[s[i]-'a']++; 
       i++; 
    } 
      
    vector<pair<float,char>> vp;  
    for(int i=0;i<26;i++){
       float freq;
       freq= (ch[i]/(n-cnt)*100);
       char c= 'a'+i;
      vp.push_back({freq,c});
    }
    sort(vp.begin(),vp.end());
    for(int i=25;i>=0;i--){
       cout<<vp[i].second<<" - ";
       cout<<setprecision(4)<<vp[i].first<<endl;

    }
}