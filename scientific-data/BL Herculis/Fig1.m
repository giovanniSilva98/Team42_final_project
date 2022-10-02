
HippMagnitude=[10.75, 10.65, 10.45, 10.2, 9.85, 9.9, 9.95, 10.05, 10.1, 10.1, 10.18, 10.25, 10.3, 10.4, 10.45, 10.55, 10.6, 10.65, 10.7, 10.75];
HippNew=[];
for i=1:length(HippMagnitude)-1
    a=linspace(HippMagnitude(i),HippMagnitude(i+1),10);
    HippNew=[HippNew a];
end
tempo=linspace(0,0.95,length(HippNew));


% Dati sole: 
%m2=-26.8; 
%f2=3.9e26;

%AppLum=@(m) f2*100.^((m2-m)/5);
%distanza
%ly=
%d=385
%AssLum=4*pi*d^2*AppLum(HippNew);    
d=118;
M=@(m) m-5*log(d/10);
Luminosita_caso1=M(HippNew);
tempo=tempo';
Luminosita_caso1=Luminosita_caso1';
