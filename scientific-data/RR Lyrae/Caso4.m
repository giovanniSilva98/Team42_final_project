% Caso 4, RR Lyrae

% periodo=13h

Magnitude=[7.19, 7.3,7.35,7.41,7.5,7.6,7.72,7.75,7.79,7.81,7.84,7.85,7.86,7.84,7.9,7.97,7.97,7.9,7.5,7.19];
New=[];
for i=1:length(Magnitude)-1
    a=linspace(Magnitude(i),Magnitude(i+1),10);
    New=[New a];
end
tempo=linspace(0,0.95,length(New));


% Dati sole: 
%m2=-26.8; 
%f2=3.9e26;

%AppLum=@(m) f2*100.^((m2-m)/5);
%distanza
%ly=
%d=385
%AssLum=4*pi*d^2*AppLum(HippNew);    
d=7.66;
M=@(m) m-5*log(d/10);
Luminosita_caso4=M(New);
tempo=tempo';
Luminosita_caso4=Luminosita_caso4';