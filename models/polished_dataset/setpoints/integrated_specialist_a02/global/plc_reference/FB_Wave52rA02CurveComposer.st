FUNCTION_BLOCK FB_Wave52rA02CurveComposer
VAR_INPUT
    aCondition : ARRAY[0..3] OF REAL;
    aK01PredictionCurve : ARRAY[0..2047] OF REAL;
    aH08PredictionCurve : ARRAY[0..2047] OF REAL;
    fDirectionFlag : REAL;
    bExecute : BOOL;
END_VAR
VAR_OUTPUT
    aPredictionCurve : ARRAY[0..2047] OF REAL;
    aH08CenteredResidual : ARRAY[0..2047] OF REAL;
    fK01Mean : REAL;
    fH08Mean : REAL;
    fLearnedH08Gate : REAL;
    fForwardGate : REAL;
    bValid : BOOL;
END_VAR
VAR
    aNormalizedCondition : ARRAY[0..3] OF REAL;
    aHidden : ARRAY[0..11] OF REAL;
    fAccumulator : REAL;
    fCenteredDifference : REAL;
    fResidual : REAL;
    nInputIndex : INT;
    nOutputIndex : INT;
    nCurveIndex : INT;
END_VAR

bValid := FALSE;
IF bExecute THEN
    fK01Mean := 0.0;
    fH08Mean := 0.0;
    FOR nCurveIndex := 0 TO 2047 DO
        fK01Mean := fK01Mean + aK01PredictionCurve[nCurveIndex];
        fH08Mean := fH08Mean + aH08PredictionCurve[nCurveIndex];
    END_FOR
    fK01Mean := fK01Mean / 2048.0;
    fH08Mean := fH08Mean / 2048.0;

    FOR nInputIndex := 0 TO 3 DO
        aNormalizedCondition[nInputIndex] :=
            (aCondition[nInputIndex]
            - GVL_Wave52rA02Parameters.A02_CONDITION_MEAN[nInputIndex])
            / GVL_Wave52rA02Parameters.A02_CONDITION_SCALE[nInputIndex];
    END_FOR
    FOR nOutputIndex := 0 TO 11 DO
        fAccumulator :=
            GVL_Wave52rA02Parameters.A02_GATE_LAYER_0_BIAS[nOutputIndex];
        FOR nInputIndex := 0 TO 3 DO
            fAccumulator := fAccumulator
                + aNormalizedCondition[nInputIndex]
                * GVL_Wave52rA02Parameters.A02_GATE_LAYER_0_WEIGHT[
                    nOutputIndex * 4 + nInputIndex
                ];
        END_FOR
        aHidden[nOutputIndex] := TANH(fAccumulator);
    END_FOR
    fAccumulator := GVL_Wave52rA02Parameters.A02_GATE_LAYER_2_BIAS[0];
    FOR nInputIndex := 0 TO 11 DO
        fAccumulator := fAccumulator
            + aHidden[nInputIndex]
            * GVL_Wave52rA02Parameters.A02_GATE_LAYER_2_WEIGHT[nInputIndex];
    END_FOR
    fLearnedH08Gate := TANH(fAccumulator);
    IF fDirectionFlag > 0.0 THEN fForwardGate := 1.0; ELSE fForwardGate := 0.0; END_IF

    FOR nCurveIndex := 0 TO 2047 DO
        fCenteredDifference :=
            (aH08PredictionCurve[nCurveIndex] - fH08Mean)
            - (aK01PredictionCurve[nCurveIndex] - fK01Mean);
        fResidual := fForwardGate * fLearnedH08Gate * fCenteredDifference;
        fResidual := LIMIT(
            -GVL_Wave52rA02Parameters.A02_BRANCH_BOUND_DEG,
            fResidual,
            GVL_Wave52rA02Parameters.A02_BRANCH_BOUND_DEG
        );
        aH08CenteredResidual[nCurveIndex] := fResidual;
        aPredictionCurve[nCurveIndex] :=
            aK01PredictionCurve[nCurveIndex] + fResidual;
    END_FOR
    bValid := TRUE;
END_IF
