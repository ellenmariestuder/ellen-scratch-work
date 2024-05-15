package com.learnMaven;

/**
 * Hello world!
 *
 */
public class App {
    public static String main (){
    // public static String main (String[] args){
        newClass.announce();

        anotherOne djKhalid = new anotherOne();
        djKhalid.yell();

        System.out.println("DDJJJ KKHHAAALLLIIIDDDD!");
        return "check out this return statement!";
    }   
}


class newClass {
    public static void announce(){
        System.out.println("NEW CLASS BABY.");
    }
}

class anotherOne {
    public void yell(){
        System.out.println("ANOTHA ONE.");
    }
}