% Caso 3, RV tauri

% periodo=78 gg

Magnitude=[7.4,7.6,7.9,8.3,8.5,8.3,7.7,7.4,7.3,7.35,7.42,7.6,7.65,7.65,7.65,7.6,7.4,7.4,7.3,7.6,7.4];
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
d=1280;
M=@(m) m-5*log(d/10);
Luminosita_caso3=M(New);
tempo=tempo';
Luminosita_caso3=Luminosita_caso3';