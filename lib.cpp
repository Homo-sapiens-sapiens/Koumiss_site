#include <iostream>
#include <string>
#include <vector>
#include <ctime>
using namespace std;

string alph = "0123456789`-=QWERTYUIOPASDFGHJKL;'ZXCVBNM,./*~[]qwertyuiop{}asdfghjkl!@#$%^&()_+zxcvbnm ";

extern "C"{
	__declspec(dllexport) const char* ces(const char* inn, const char* key, bool mode);
	__declspec(dllexport) const char* mix(const char* inn, const char* key, bool mode);
	__declspec(dllexport) const char* fill(const char* inn, const char* key, bool mode);}

// Определение функции
const char* ces(const char* inn, const char* key, bool mode){
	string input(inn);
	string k(key);
	int m = k.size();
	int let;
	static string out;
	out.clear();
	int mod = mode?1:-1;
	for(int i=0; i<input.size(); i++){
		let=alph.find(input[i]);
		let+=alph.find(k[i%m])*mod;
		if(let<0){let+=88;}
		out+=alph[let%88];}
	return out.c_str();}

const char* mix(const char* inn, const char* key, bool mode){
	string input(inn);
	string k(key);
	int m = k.size();
	int n = input.size();
	static string out;
	out.assign(n,'_');
	vector<int> inds;
	int s;
	for(int i=0; i<n; i++){inds.push_back(i);}
	if(mode){
		for(int i=0; i<n; i++){
			s = inds.size();
			out[inds[alph.find(k[i%m])%s]]=input[i];
			inds.erase(inds.begin()+alph.find(k[i%m])%s);}}
	else{
		for(int i=0; i<n; i++){
			s = inds.size();
			out[i]=input[inds[alph.find(k[i%m])%s]];
			inds.erase(inds.begin()+alph.find(k[i%m])%s);}}
	return out.c_str();}

const char* fill(const char* inn, const char* key, bool mode){
	srand(time(0));
	string input(inn);
	string k(key);
	int m = k.size();
	int n = input.size();
	static string out;
	out.clear();
	if(mode){
		for(int i=0; i<n; i++){
			for(int j=0; j<alph.find(k[i%m]); j++){out+=alph[rand()%88];}
			out+=input[i];}
		for(int j=0; j<alph.find(k[n%m]); j++){out+=alph[rand()%88];}}
	else{
		int c=alph.find(k[0]);
		int i=1;
		while(c<n){
			out+=input[c];
			c+=alph.find(k[i%m])+1;
			i++;}}
	return out.c_str();}

/*
int main(){
	string a, b;
	bool c;
	cin>>a>>b>>c;
	const char* oo = fill(a.c_str(), b.c_str(), c);
	string o(oo);
	cout<<o<<endl;}*/