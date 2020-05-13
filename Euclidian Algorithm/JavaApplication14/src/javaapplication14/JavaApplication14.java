/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package javaapplication14;

/**
 *
 * @author USER
 */
public class JavaApplication14 {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        int a = 79;
        int b = 283;
        if(b>a){
            int temp = a;
            a = b;
            b = temp;
        }
        int p = 1;
        int q = 0;
        int r = 0;
        int s = 1;
        int hasil_1 = (p*a)+(q*b);
        System.out.println(hasil_1);
        int hasil_2 = (r*a)+(s*b);
        System.out.println(hasil_2);
        System.out.println(p+"."+a+" + "+q+"."+b+"="+hasil_1);
        System.out.println(r+"."+a+" + "+s+"."+b+"="+hasil_2);
        System.out.println("");
        while (hasil_2 != 1 && hasil_2 != 0){
            int n = 1;
            int jum = hasil_2;
            while(jum <= hasil_1){
                n++;
                jum +=hasil_2;
            }
            jum = jum-hasil_2;
            n-=1;
            int temp_2 = p;
            int temp_3 = q;
            p = r;
            q = s;
            r = temp_2 - (p * n);
            s = temp_3 - (q * n);
            int temp_1 = hasil_2;
            hasil_2 = hasil_1 - jum;
            hasil_1 = temp_1;
            System.out.println(hasil_2);
            System.out.println(p+"."+a+" + "+q+"."+b+"="+hasil_1);
            System.out.println(r+"."+a+" + "+s+"."+b+"="+hasil_2);
            System.out.println("");
        }
    }
    
}
