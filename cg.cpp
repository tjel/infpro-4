#include <iostream>
 
using namespace std;
double j,j1,j2,k;

void input(){

	cout<<"wprowadź licznik j"<<endl;
	cin>>j;
	cout<<"wprowadź licznik j1"<<endl;
	cin>>j1;
	cout<<"wprowadź licznik j2"<<endl;
 	cin>>j2;
	j=j/2;
	j1=j1/2;
	j2=j2/2;
	cout<<"to jest j "<<j<<endl;
	cout<<"to jest j1 "<<j1<<endl;
	cout<<"to jest j2 "<<j2<<endl;
}
 
int main()
{	
	input();
	if (j>=j1-j2 && j<=j1+j2)
	{
		cout<<"opcja1"<<endl;
	}
	else
	{
		cout<<"Współczynniki są zerowe"<<endl;
	}


	
	
    
    return 0;
}
