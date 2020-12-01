function [x,y] = Euler_Pvi(f,a,b,N,y0)
%Método de Euler para problemas de valor inicial
%   EDO de Orden 1 con condicion inicial
h = (b-a)/N;
x = a:h:b;
y = zeros(N+1,1);
y(1) = y0;
for k=1:N
    y(k+1) = y(k)+h*feval(f,x(k),y(k));
end
end

