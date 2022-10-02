% Caso 5 - type 1 cepheids
% Luminosità dell'utente --> Ricavi Mv
% Una volta che abbiamo Mv: S=S+Mv
% Periodo: 10 gg

% L'input è Mv
Mv=; % Va inserito da grafico pyhton
P=10*24*60*60;
w=2*pi/((-Mv+1.42)/2.78); % Chiedere a Silva se Mv è negativo
t=linspace(0,P,200);

S=0.418*sin(w*t-20.76)+0.1419*sin(2*w*t-63.76)...
     +0.0664*sin(3*w*t-91.57)+0.0354*sin(4*w*t-112.62)...
     +0.020*sin(5*w*t-129.47);
S=(S+Mv)
plot(t,S);