# include <iostream>

using namespace std;

int main() 
{ 
    float PI = 3.14159265359;                // variables can be initialized during declaration 
    double rad;
    double area;
    cout<< "Enter the radius:  /n"; 
    cin>>rad; 
if (rad<=0)
    cout<<"Nie można wykonać operacji"<<endl;
else
    area=PI * rad * rad;
    cout<< "Area of the circle is "<< area <<endl; 
    return 0;
}  
