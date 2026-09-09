#include<iostream>
#include<string>
#include<queue>
using namespace std ;
struct task{
int ID;
string Name;
};
void menu();

int main(){
   
menu();
}
void menu(){
    int choice;
     queue<task> tasks ;
    
     while(choice!=3){
    cout<<" press 1 for add task"<<endl;
    cout<<" press 2 for remove task"<<endl;
    cout<<" press 3 to exit "<<endl;
    cin>>choice;
    if(choice==1){
        task temp;
        cout<<"Enter the task ID :";
        cin>>temp.ID;
        cout<<"Enter the task Name :";
        cin>>temp.Name;
        tasks.push(temp);
    }else if(choice==2){
        task temp=tasks.front();
        cout<<"the task removes is:"<<endl;
        cout<<"Enter the task ID :"<<temp.ID;
        cout<<"Enter the task Name :"<<temp.Name;
        tasks.pop();
       

    }
    else{
        break;
    }
}
}