% periodo 9.048 gg

Magnitude=[4.08, 4.09, 4.1, 4.08, 4.07,4.02, 3.85, 3.68, 3.63, 3.59, 3.57, 3.61, 3.65, ...
    3.73, 3.78, 3.86, 3.92, 3.97, 4.05, 4.08];
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
d=180; %in parsec
M=@(m) m-5*log(d/10);
Luminosita_caso2=M(New);
tempo=tempo';
Luminosita_caso2=Luminosita_caso2';