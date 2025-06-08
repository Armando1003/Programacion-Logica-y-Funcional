%hechos
humedad(baja).
temperatura(35).
hora(20).
probabilidad_lluvia(false).


%reglas
%¿Es una hora adecuada para regar?
hora_adecuada :- hora(H), (H < 10 ; H > 18).

%¿Cuando se debe activar el sistema?
activar_riego :-
    humedad(baja),
    probabilidad_lluvia(false),
    hora_adecuada.

%Diagnostico del sistema
estado_riego('Activado') :- activar_riego.
estado_riego('No activado') :- \+ activar_riego.


%Alerta por calor extremo.
alerta_calor :-
    temperatura(T),
    T >= 32.

%Mensaje: el sistema emite una recomendación
recomendacion :-
    activar_riego,
    alerta_calor, !,
    write('Alerta: Riego activado con temperatura alta. Considere riego nocturno o por goteo.').

recomendacion :- 
    write('Sin recomendaciones especiales para el riego.').
