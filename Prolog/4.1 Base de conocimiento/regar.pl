% --- Datos de sensores por zona ---
zona(jardin, humedad(30), temperatura(35), hora(15), false).
zona(huerto, humedad(20), temperatura(28), hora(9), true).
zona(cesped, humedad(40), temperatura(25), hora(19), false).

% --- Requerimientos de humedad ideal por zona ---
necesidad_riego(jardin, 40).
necesidad_riego(huerto, 25).
necesidad_riego(cesped, 35).

% --- Tipo de planta por zona ---
tipo_planta(jardin, ornamentales).
tipo_planta(huerto, hortalizas).
tipo_planta(cesped, gramineas).

% --- Hora adecuada para riego ---
hora_adecuada(hora) :- hora < 10 ; hora > 18.

% --- Alerta por calor extremo según tipo de planta ---
alerta_calor(Zona, Temperatura) :-
    tipo_planta(Zona, Tipo),
    (Tipo = ornamentales, Temperatura > 30;
     Tipo = hortalizas, Temperatura > 35;
     Tipo = gramineas, Temperatura > 38).

% --- Regla para decidir si se debe activar el riego ---
activar_riego(Zona) :-
    zona(Zona, humedad(HActual), _, hora, false),
    necesidad_riego(Zona, HDeseada),
    HActual < HDeseada,
    hora_adecuada(hora).

% --- Estado del riego según situación ---
estado_riego(Zona, 'Activado - Requiere riego urgente') :-
    activar_riego(Zona),
    zona(Zona, _, temperatura(T), _, _),
    alerta_calor(Zona, T).

estado_riego(Zona, 'Activado - Riego normal') :-
    activar_riego(Zona),
    zona(Zona, _, temperatura(T), _, _),
    \+ alerta_calor(Zona, T).

estado_riego(Zona, 'No activado') :-
    \+ activar_riego(Zona).

% --- Recomendaciones inteligentes ---
recomendacion(Zona, 'ALERTA: Evite regar en horas de calor. Use riego por goteo.') :-
    activar_riego(Zona),
    zona(Zona, _, temperatura(T), _, _),
    alerta_calor(Zona, T).

recomendacion(Zona, 'Recomendación: Riegue durante 10-15 minutos.') :-
    activar_riego(Zona),
    zona(Zona, _, temperatura(T), _, _),
    \+ alerta_calor(Zona, T).

recomendacion(Zona, 'No se requiere riego: Humedad óptima.') :-
    zona(Zona, humedad(H), _, _, _),
    necesidad_riego(Zona, HDeseada),
    H >= HDeseada.

recomendacion(Zona, 'Advertencia: No es hora ideal para regar (evite el sol directo).') :-
    zona(Zona, _, _, hora, _),
    Hora >= 10, Hora =< 18.
