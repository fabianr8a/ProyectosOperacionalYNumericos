/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package logic;

import java.util.Arrays;

/**
 *
 * @author EILEMUS
 */
public class logica {

    private int iy;
    private int jx;
    private static logica log;
    private double matrizX[][];
    private double trMatrizX[][];
    private double matrizY[][];
    
    private String resultado;

    public String getResultado() {
        return resultado;
    }

    public void setResultado(String resultado) {
        this.resultado = resultado;
    }

    
    
    public double[][] getMatrizX() {
        return matrizX;
    }

    public void setMatrizX(double[][] matrizX) {
        this.matrizX = matrizX;
    }

    public double[][] getTrMatrizX() {
        return trMatrizX;
    }

    public void setTrMatrizX(double[][] trMatrizX) {
        this.trMatrizX = trMatrizX;
    }

    public double[][] getMatrizY() {
        return matrizY;
    }

    public void setMatrizY(double[][] matrizY) {
        this.matrizY = matrizY;
    }
    
    public static logica getLogica(){
        return log;
    }
    
    public static logica getLogica(int a, int b,int c, int d){
     if (log==null){
         log = new logica(a, b, c, d);
     }
         return log;
    }
    
    private logica(int a, int b,int c, int d) {
        jx=0;
        iy=0;
        this.matrizX = new double[a][b];
        this.trMatrizX = new double[b][a];
        this.matrizY = new double[c][d];

        for (int i = 0; i < a; i++) {
            matrizX[i][0] = 1;
        }
    }
    
    public void addMatrizY(double y){
       matrizY[iy][0] = y;
       iy++;
    }
    
    public void limpiarMatrizY(){
        for(int i=0; i < matrizY.length;i++){
            matrizY[i][0]=0;
        }
        iy=0;
    }
    public void limpiarMatrizX(int column){
        for(int i=0; i < matrizX.length;i++){
            matrizX[i][column]=0;
        }
    }
    
    public void addMatrizX(int row,int column,double x){
       matrizX[row][column] = x;    
    }

    //calcula matriz transpuesta
    public static double[][] transpuesta(double[][] matriz1) {
        double TR[][] = new double[matriz1[0].length][matriz1.length];
        for (int i = 0; i < matriz1.length; i++) {
            for (int j = 0; j < matriz1[i].length; j++) {
                TR[j][i] = matriz1[i][j];
            }
        }
        return TR;
    }

    public static double[][] multiplicarMatrices(double[][] matriz1,double[][] matriz2) {
        double AB[][] = new double[matriz1.length][matriz2[0].length];
        for (int i = 0; i < AB.length; i++) {
            for (int j = 0; j < AB[0].length; j++) {
                for (int k = 0; k < matriz1[0].length; k++) {
                    
                    AB[i][j] +=   matriz1[i][k]*matriz2[k][j];

                }
            }   
        }
        return AB;
    }    
    public static double[][] matrizInversa(double[][] matriz) {
        double det=1/determinante(matriz);
        double[][] nmatriz=matrizAdjunta(matriz);
        nmatriz=multiplicarMatriz(det,nmatriz);
        return nmatriz;
    }

    public static double[][] multiplicarMatriz(double n, double[][] matriz) {
        for(int i=0;i<matriz.length;i++){
            for(int j=0;j<matriz.length;j++){
                matriz[i][j]*=n;
            }
        }    
        return matriz;
    }

    public static double[][] matrizAdjunta(double [][] matriz){
        return matrizTranspuestaB(matrizCofactores(matriz));
    }

    public static double[][] matrizCofactores(double[][] matriz){
        double[][] nm=new double[matriz.length][matriz.length];
        for(int i=0;i<matriz.length;i++) {
            for(int j=0;j<matriz.length;j++) {
                double[][] matrizResult=new double[matriz.length-1][matriz.length-1];
                double detValor;
                for(int k=0;k<matriz.length;k++) {
                    if(k!=i) {
                        for(int l=0;l<matriz.length;l++) {
                            if(l!=j){
                                int indice1=k<i ? k : k-1 ;
                                int indice2=l<j ? l : l-1 ;
                                matrizResult[indice1][indice2]=matriz[k][l];
                            }
                        }
                    }
                }
                detValor=determinante(matrizResult);
                nm[i][j]=detValor * (double)Math.pow(-1, i+j);
            }
        }
        return nm;
    }

    public static double[][] matrizTranspuestaB(double [][] matriz){
        double[][]nuevam=new double[matriz[0].length][matriz.length];
        for(int i=0; i<matriz.length; i++){
            for(int j=0; j<matriz.length; j++)
                nuevam[i][j]=matriz[j][i];
        }
        return nuevam;
    }

    public static double determinante(double[][] matriz){
        double det;
        if(matriz.length==1){
        det=matriz[0][0];
        return det;
        }
        else if(matriz.length==2){
            det=(matriz[0][0]*matriz[1][1])-(matriz[1][0]*matriz[0][1]);
            return det;
        }
        double suma=0;
        for(int i=0; i<matriz.length; i++){
        double[][] nm=new double[matriz.length-1][matriz.length-1];
            for(int j=0; j<matriz.length; j++){
                if(j!=i){
                    for(int k=1; k<matriz.length; k++){
                        int indice=-1;
                        if(j<i)
                            indice=j;
                        else if(j>i)
                            indice=j-1;
                            nm[indice][k-1]=matriz[j][k];
                    }
                }
            }
            if(i%2==0)
                suma+=matriz[i][0] * determinante(nm);
            else
                suma-=matriz[i][0] * determinante(nm);
        }
        return suma;
    }
}
