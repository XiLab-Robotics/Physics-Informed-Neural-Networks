(* Stage 15 H04 PLC reference. Runtime build and timing remain pending. *)
FUNCTION_BLOCK FB_Stage15H04CoefficientResidual
VAR_INPUT
    Enable : BOOL;
    SignedTorqueNm : REAL;
    AbsoluteSpeedRpm : REAL;
    OilTemperatureDegC : REAL;
    OutputAngleRad : REAL;
END_VAR
VAR_OUTPUT
    Valid : BOOL;
    AnalyticalTeDeg : REAL;
    CorrectionTeDeg : REAL;
    PredictedTeDeg : REAL;
    AnalyticalCoefficient : ARRAY[0..18] OF REAL;
    CoefficientCorrection : ARRAY[0..18] OF REAL;
    PredictedCoefficient : ARRAY[0..18] OF REAL;
END_VAR
VAR
    NormalizedCondition : ARRAY[0..2] OF REAL;
    QuadraticBasis : ARRAY[0..9] OF REAL;
    Hidden0 : ARRAY[0..63] OF REAL;
    Hidden1 : ARRAY[0..63] OF REAL;
    Hidden2 : ARRAY[0..31] OF REAL;
    RawCorrection : ARRAY[0..18] OF REAL;
    HarmonicOrder : ARRAY[0..8] OF DINT := [1, 3, 39, 40, 78, 81, 156, 162, 240];
    InputValue : ARRAY[0..2] OF REAL;
    Accumulator : REAL;
    HarmonicIndex : DINT;
    InputIndex : DINT;
    OutputIndex : DINT;
END_VAR

Valid := FALSE;
IF NOT Enable THEN
    PredictedTeDeg := 0.0;
    RETURN;
END_IF

InputValue[0] := SignedTorqueNm;
InputValue[1] := AbsoluteSpeedRpm;
InputValue[2] := OilTemperatureDegC;
FOR InputIndex := 0 TO 2 DO
    NormalizedCondition[InputIndex] :=
        (InputValue[InputIndex] - GVL_Stage15H04Parameters.H04_FEATURE_MEAN[InputIndex])
        / GVL_Stage15H04Parameters.H04_FEATURE_SCALE[InputIndex];
END_FOR

QuadraticBasis[0] := NormalizedCondition[0] * NormalizedCondition[0];
QuadraticBasis[1] := NormalizedCondition[1] * NormalizedCondition[1];
QuadraticBasis[2] := NormalizedCondition[2] * NormalizedCondition[2];
QuadraticBasis[3] := NormalizedCondition[0] * NormalizedCondition[1];
QuadraticBasis[4] := NormalizedCondition[0] * NormalizedCondition[2];
QuadraticBasis[5] := NormalizedCondition[1] * NormalizedCondition[2];
QuadraticBasis[6] := NormalizedCondition[0];
QuadraticBasis[7] := NormalizedCondition[1];
QuadraticBasis[8] := NormalizedCondition[2];
QuadraticBasis[9] := 1.0;

FOR OutputIndex := 0 TO 18 DO
    Accumulator := 0.0;
    FOR InputIndex := 0 TO 9 DO
        Accumulator := Accumulator
            + QuadraticBasis[InputIndex]
            * GVL_Stage15H04Parameters.H04_PFA_COEFFICIENT_MATRIX[
                InputIndex * 19 + OutputIndex
            ];
    END_FOR
    AnalyticalCoefficient[OutputIndex] := Accumulator;
END_FOR

FOR OutputIndex := 0 TO 63 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_0_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 2 DO
        Accumulator := Accumulator
            + NormalizedCondition[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_0_WEIGHT[
                OutputIndex * 3 + InputIndex
            ];
    END_FOR
    Hidden0[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 63 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_2_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 63 DO
        Accumulator := Accumulator
            + Hidden0[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_2_WEIGHT[
                OutputIndex * 64 + InputIndex
            ];
    END_FOR
    Hidden1[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 31 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_4_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 63 DO
        Accumulator := Accumulator
            + Hidden1[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_4_WEIGHT[
                OutputIndex * 64 + InputIndex
            ];
    END_FOR
    Hidden2[OutputIndex] := TANH(Accumulator);
END_FOR

FOR OutputIndex := 0 TO 18 DO
    Accumulator := GVL_Stage15H04Parameters.H04_LAYER_6_BIAS[OutputIndex];
    FOR InputIndex := 0 TO 31 DO
        Accumulator := Accumulator
            + Hidden2[InputIndex]
            * GVL_Stage15H04Parameters.H04_LAYER_6_WEIGHT[
                OutputIndex * 32 + InputIndex
            ];
    END_FOR
    RawCorrection[OutputIndex] := Accumulator;
    CoefficientCorrection[OutputIndex] :=
        GVL_Stage15H04Parameters.H04_CORRECTION_BOUND[OutputIndex]
        * TANH(RawCorrection[OutputIndex]);
    PredictedCoefficient[OutputIndex] :=
        AnalyticalCoefficient[OutputIndex] + CoefficientCorrection[OutputIndex];
END_FOR

AnalyticalTeDeg := AnalyticalCoefficient[0];
CorrectionTeDeg := CoefficientCorrection[0];
FOR HarmonicIndex := 0 TO 8 DO
    AnalyticalTeDeg := AnalyticalTeDeg
        + AnalyticalCoefficient[1 + 2 * HarmonicIndex]
        * SIN(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad)
        + AnalyticalCoefficient[2 + 2 * HarmonicIndex]
        * COS(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad);
    CorrectionTeDeg := CorrectionTeDeg
        + CoefficientCorrection[1 + 2 * HarmonicIndex]
        * SIN(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad)
        + CoefficientCorrection[2 + 2 * HarmonicIndex]
        * COS(DINT_TO_REAL(HarmonicOrder[HarmonicIndex]) * OutputAngleRad);
END_FOR
PredictedTeDeg := AnalyticalTeDeg + CorrectionTeDeg;
Valid := TRUE;
