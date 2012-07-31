//This is a test comment (bad)
var my_func = function my_fun(){
    //The purpose of this func is to increment a variable called my_var
    //  by looping twenty times and increasing it's value
    //The intended purpose is that it will get called by some user of 
    //  this script
    var my_var = 42;
    //Loop twenty iterations and increase the value of my_var
    //  by the current iteration value
    for(i=0;i<20;i++){
        my_var += i;
    }
}
