function xd = NumDiff( x , t , xd0 , xdN )

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Syntax
% xd = NumDiff1( x , dt )
% xd = NumDiff1( x , t )
% xd = NumDiff1( x , dt , xd0 , xdN )
% xd = NumDiff1( x , t , xd0 , xdN )
%
% Inputs
% x --> funzione da derivare (vettore colonna o matrice di vettori colonna)
% dt --> constant time step (scalare)
% t --> tempo (vettore colonna)
% xd0 --> condizioni iniziali (vettore riga)
% xdN --> condizioni finali (vettore riga)
%
% Outputs
% xd --> funzione derivata (vettore colonna o matrice di vettori colonna)
%
% Description
% Calcola un approssimazione della derivata di x rispetto a t (o dt).
% Utilizza formule alle differenze centrali a 3 punti.
% Se xd0 ed xdN non sono assegnati, vengono calcolati con formule alle
% differenze in avanti ed all'indietro a 3 punti.
% Se x ha solo 1 valore, la derivata restituita è zero.
% Se x ha solo 2 valori, vengono utilizzante formule a 2 punti.
%
% NOTA: dove x sale e scende la derivata è posta a 0 per evitare sovraelongazioni.
%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%

% leggo le dimensioni
[ K , N ] = size(x) ;   % K istanti di tempo, N variabili

% memory allocation for output
xd = zeros(K,N) ;


%%%%%%%%%%%%%%%
% se x ha almeno 3 punti,
%%%%%%%%%%%%%%%
if K>=3
    switch nargin
        
        case 2   % se NON sono specificate le derivate agli estremi le calcolo
            if isscalar(t)   % punti equispaziati
                for n = 1 : N
                    %%% calcolo condizioni iniziali
                    if x(1,n) == x(2,n)   % se i primi 2 punti sono uguali imposto a zero la derivata, per evitare sovraelongazioni
                        xd(1,n) = 0 ;
                    else
                        % xd(1,:) = ( x(2,:)-x(1,:) ) ./ t ;      % 2 punti = errore del I ord.
                        xd(1,:) = ( - 3*x(1,:) + 4*x(2,:) - x(3,:) ) ./ (2*t) ;      % 3 punti = errore del II ord.
                    end
                    %%% calcolo condizioni finali
                    if x(K,n) == x(K-1,n)   % se gli ultimi 2 punti sono uguali imposto a zero la derivata, per evitare sovraelongazioni
                        xd(K,n) = 0 ;
                    else
                        % xd(K,:) = ( x(K,:)-x(K-1,:) ) ./ t ;    % 2 punti = errore del I ord.
                        xd(K,:) = ( + 3*x(K,:) - 4*x(K-1,:) + x(K-2,:) ) ./ (2*t) ;    % 3 punti = errore del II ord.
                    end
                end
            else   % per punti NON equispaziati
                hh0 = t(3)-t(1) ;
                hhK = t(K)-t(K-2) ;
                for n = 1 : N
                    %%% calcolo condizioni iniziali
                    if x(1,n) == x(2,n)   % se i primi 2 punti sono uguali imposto a zero la derivata, per evitare sovraelongazioni
                        xd(1,n) = 0 ;
                    else
                        xd(1,:) = ( - 3*x(1,:) + 4*x(2,:) - x(3,:) ) ./ hh0 ;      % 3 punti = errore del II ord.
                    end
                    %%% calcolo condizioni finali
                    if x(K,n) == x(K-1,n)   % se gli ultimi 2 punti sono uguali imposto a zero la derivata, per evitare sovraelongazioni
                        xd(K,n) = 0 ;
                    else
                        xd(K,:) = ( + 3*x(K,:) - 4*x(K-1,:) + x(K-2,:) ) ./ hhK ;    % 3 punti = errore del II ord.
                    end
                end
            end
            
        case 4   % se sono specificate le derivate agli estremi le assegno
            % assegno condizioni iniziali
            xd(1,:) = xd0 ;
            % assegno condizioni finali
            xd(K,:) = xdN ;
            
        otherwise
            error('Wrong number of input arguments')
    end
    
    
    % calcolo derivata per i punti interni (differenze centrali)
    if isscalar(t)   % punti equispaziati
        tt = 2*t ;
        for n = 1 : N
            for k = 2:(K-1)
                if ( (x(k,n)>=x(k-1,n)) && (x(k,n)>=x(k+1,n)) ) || ...
                        ( (x(k,n)<=x(k-1,n)) && (x(k,n)<=x(k+1,n)) )
                    xd(k,n) = 0;
                else
                    xd(k,n) = ( x(k+1,n) - x(k-1,n) ) ./ tt ;    % errore del II ord.
                    % xd(k,n) = ( x(k-2,n) - 8*x(k-1,n) + 8*x(k+1,n) - x(k+2,n) ) ./ ( 12*t ) ;    % errore del IV ord.
                end
            end
        end
    else   % per punti NON equispaziati
        for n = 1 : N
            for k = 2:(K-1)
                hh = t(k+1)-t(k-1) ;
                if ( (x(k,n)>=x(k-1,n)) && (x(k,n)>=x(k+1,n)) ) || ...
                        ( (x(k,n)<=x(k-1,n)) && (x(k,n)<=x(k+1,n)) )
                    xd(k,n) = 0;
                else
                    xd(k,n) = ( x(k+1,n) - x(k-1,n) ) ./ hh ;    % errore del II ord.
                end
            end
        end
    end
    return
end



%%%%%%%%%%%%%%%
% se x ha solo 2 punti, uso le formule a 2 punti
%%%%%%%%%%%%%%%
if K==2
    switch nargin
        % se NON sono specificate le derivate agli estremi le calcolo con le formule in avanti ed indietro a 2 punti
        case 2
            if isscalar(t)   % punti equispaziati
                % calcolo condizioni iniziali
                xd(1,:) = ( x(2,:)-x(1,:) ) ./ t ;      % 2 punti = errore del I ord.
                % calcolo condizioni finali
                xd(K,:) = ( x(K,:)-x(K-1,:) ) ./ t ;    % 2 punti = errore del I ord.
            else   % per punti NON equispaziati
                % calcolo condizioni iniziali
                hp = t(2)-t(1) ;
                xd(1,:) = ( x(2,:)-x(1,:) ) ./ ( hp ) ;      % 2 punti
                % calcolo condizioni finali
                hm = t(K)-t(K-1) ;
                xd(K,:) = ( x(K,:)-x(K-1,:) ) ./ ( hm ) ;      % 2 punti
            end
            % se sono specificate le derivate agli estremi le assegno
        case 4
            % assegno condizioni iniziali
            xd(1,:) = xd0 ;
            % assegno condizioni finali
            xd(K,:) = xdN ;
        otherwise
            error('Wrong number of input arguments')
    end
    return
end



%%%%%%%%%%%%%%%
% se x ha solo 1 punto, assegno zero alla derivata
%%%%%%%%%%%%%%%
if K==1
    xd = zeros(K,N) ;
    return
end





%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% NOTE
% punti NON equispaziati
%zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
% % %         for k = 2:(K-1)
% % %             % con il polinomio di Lagrange
% % %             % xd(k,:) = ...
% % %             %    x(k-1,:) * ( t(k)-t(k+1) )/( (t(k-1)-t(k))*(t(k-1)-t(k+1)) ) + ...
% % %             %    x(k,:) * ( 2*t(k)-t(k-1)-t(k+1) )/( (t(k)-t(k-1))*(t(k)-t(k+1)) ) + ...
% % %             %    x(k+1,:) * ( t(k)-t(k-1) )/( (t(k+1)-t(k-1))*(t(k+1)-t(k)) ) ;  % errore del II ord.
% % %             hp = t(k+1) - t(k) ;
% % %             hm = t(k) - t(k-1) ;
% % %             xd(k,:) = ( x(k+1,:) - x(k-1,:) ) ./ ( hp + hm ) ;
% % %         end
%zzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzzz
