%Interpoblacion de Newton
%function[yi,p,b]=inter_newton(x,y,xi)
%Inicializacion de variables
x=input('Introduzca el valor independiente "x"= ');
y=input('Indrouzca el valor dependiente "y"= ');
xi=input('Introduzca el valor "xi" a interpolar= ');

n=length(x);
b=zeros(n);
b(:,1)=y(:);

%Obtencion de la tabla de diferencias finitas
disp('Obtencion de la Tabla de Diferencias Finitas')
for j=2:n
    for i=1:n-j+1
        b(i,j)=(b(i+1,j-1)-b(i,j-1))/(x(i+j-1)-x(i));
         
    end
    disp('La matriz es '),disp(b);
end
%Calcula el dato interpoblado
%disp('Valor de "y" Interpoblador: ');
x1=1;
yi=b(1,1);
for j=1:n-1
    x1=x1.*(xi-x(j));
    yi=yi+b(1,j+i)*x1;
   
end
disp('El valor de "yi" interpoblado es igual a = '),disp(yi);


%Construye el polinomio
p=num2str(b(1,1));
xx=x*-1;
for j=2:n
    signo='';
    if b(1,j)>=0
                 signo='+';
    end
    x1='';
    for i=1:j-1
        signo2='';
        if xx(i)>=0
            signo2='+';
        end
        x1=strcat(x1,'*(x',signo2,num2str(xx(i)),')');
    end
    p=strcat(p,signo,num2str(b(1,j)),x1);
end 
    disp('El polinomio de Interpoblacion de Newton es igual a: P(x)=  '),disp(p);
    
  % Construccion de la Grafica
plot(x,y,'linewidth',3)
title('Funcion')
xlabel('x')
ylabel('y')
grid on
grid on %activamos la cuadricula de la pantalla
hold on % se mantiene el grafico por pantalla
i=1;
    [v1,v2,button]= ginput(1); %Obtenemos la coordenada de un punto en la pantalla
    plot(v1,v2,'ro');%pintamos cada punto por pantalla
    hold on %hacemos que siempre este presente en el dibujo
disp('El valor del error real: ');
v2

%optencion de los errores 
errorFinal=abs((v2-yi)/v2);
errorPorcentual=errorFinal*100;

 disp('El error relativo es:')
disp(errorFinal);
 disp('El error relativo porcentual:')
    disp(errorPorcentual);
