"""Install the Wave 5.2R A02 composer into the maintained TF3820 harness."""

from __future__ import annotations

# Import Python Utilities
import hashlib
import json
from pathlib import Path
import shutil
import sys

# Add Repository Root For Direct Script Execution
PROJECT_ROOT = Path(__file__).resolve().parents[3]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))

# Import Harness Generation Utilities
from scripts.deployment.twincat_onnx_conversion.build_tf3820_standalone_harness import (
    extract_plain_type_declarations,
    stable_guid,
    wrap_tc_dut,
)


# Define The Approved Standalone Package Contract
FAMILY_ID = "integrated_specialist_a02"
ENUM_NAME = "Model_Integrated_Specialist_A02_Composer"
RUNNER_NAME = "FB_IntegratedSpecialistA02Tf3820Runner"
TYPE_PREFIX = "IntegratedSpecialistA02"
INPUT_TYPE_NAME = f"ST_{TYPE_PREFIX}Input"
OUTPUT_TYPE_NAME = f"ST_{TYPE_PREFIX}Output"
CONVERSION_ROOT = (
    PROJECT_ROOT
    / "output"
    / "deployment"
    / "twincat_onnx_conversion"
    / "wave52r_integrated_specialist_a02_composer"
    / "tf3820"
)
SOURCE_ONNX_PATH = (
    PROJECT_ROOT
    / "models"
    / "polished_dataset"
    / "setpoints"
    / FAMILY_ID
    / "global"
    / "onnx"
    / "model.onnx"
)
HARNESS_ROOT = (
    PROJECT_ROOT
    / "reference"
    / "codes"
    / "TwinCAT_TF3820_StandaloneModelTest"
)
MODEL_ROOT = HARNESS_ROOT / "ML_models" / FAMILY_ID
PLC_ROOT = HARNESS_ROOT / "PLC_project"
CATALOG_PATH = HARNESS_ROOT / "model_catalog.json"
PLC_PROJECT_PATH = PLC_ROOT / "TF3820StandalonePLC.plcproj"


def compute_file_sha256(file_path: Path) -> str:
    """Return the lowercase SHA-256 digest for one file."""

    sha256_digest = hashlib.sha256()
    with file_path.open("rb") as input_file:
        while byte_chunk := input_file.read(1024 * 1024):
            sha256_digest.update(byte_chunk)
    return sha256_digest.hexdigest()


def read_json(input_path: Path) -> dict:
    """Read one JSON mapping."""

    payload = json.loads(input_path.read_text(encoding="utf-8"))
    assert isinstance(payload, dict)
    return payload


def write_text(output_path: Path, text: str) -> None:
    """Write text with one final newline."""

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(
        text.rstrip() + "\n",
        encoding="utf-8",
        newline="\n",
    )


def tensor_shape_map(tensor_payload: dict) -> dict[str, list[int]]:
    """Return the named Beckhoff tensor shape map."""

    return {
        tensor_record["str_name"]: tensor_record["int32_shape"]
        for tensor_record in tensor_payload.values()
    }


def build_runner_xml() -> str:
    """Build the dedicated fixed-grid multi-input A02 TF3820 runner."""

    return f'''<?xml version="1.0" encoding="utf-8"?>
<TcPlcObject Version="1.1.0.1" ProductVersion="3.1.4026.24">
  <POU Name="{RUNNER_NAME}" Id="{stable_guid('runner:' + RUNNER_NAME)}" SpecialFunc="None">
    <Declaration><![CDATA[FUNCTION_BLOCK {RUNNER_NAME}
VAR_INPUT
    sModelJsonFilePath : T_MaxString;
    sMlSvrNetId : T_MaxString := 'local';
    eExecutionProvider : E_ExecutionProvider := E_ExecutionProvider.CPU;
    bEnable : BOOL;
    bReset : BOOL;
    bLoadModel : BOOL;
    nConfigureTimeout : UDINT := 1000;
    nPredictTimeout : UDINT := 100;
    nPriority : UDINT := 0;
    aCondition : ARRAY[0..3] OF REAL;
    aK01PredictionCurve : ARRAY[0..2047] OF REAL;
    aH08PredictionCurve : ARRAY[0..2047] OF REAL;
    fDirectionFlag : REAL;
END_VAR
VAR_OUTPUT
    bConfigured : BOOL;
    bBusy : BOOL;
    bPredictionPending : BOOL;
    bPredictionReady : BOOL;
    bResetDone : BOOL;
    bError : BOOL;
    nErrorCode : HRESULT;
    nMaxInferenceDuration : UDINT;
    fForwardGate : REAL;
    fK01Mean : REAL;
    fH08Mean : REAL;
    fLearnedH08Gate : REAL;
    aK01CenteredCurve : ARRAY[0..2047] OF REAL;
    aH08CenteredDifference : ARRAY[0..2047] OF REAL;
    aH08CenteredResidual : ARRAY[0..2047] OF REAL;
    aPredictionCurve : ARRAY[0..2047] OF REAL;
END_VAR
VAR
    fbMlSvr : FB_MlSvrPrediction;
    stModelInput : {INPUT_TYPE_NAME};
    stModelOutput : {OUTPUT_TYPE_NAME};
    rtLoadModel : R_TRIG;
    nState : INT := 0;
    nConditionIndex : INT;
    nCurveIndex : INT;
END_VAR]]></Declaration>
    <Implementation>
      <ST><![CDATA[// A02 Is A Fixed-Grid Composer, Not A Standalone Expert
// K01 And H08 Curves Must Be Produced By Their Exact Qualified Dependencies
rtLoadModel(CLK := bLoadModel);

IF rtLoadModel.Q THEN
    bPredictionPending := FALSE;
    bPredictionReady := FALSE;
    bResetDone := FALSE;
    bError := FALSE;
    IF fbMlSvr.bConfigured THEN nState := 5; ELSE bConfigured := FALSE; nState := 10; END_IF
END_IF

IF bReset THEN
    bPredictionPending := FALSE;
    bPredictionReady := FALSE;
    bError := FALSE;
    IF fbMlSvr.bConfigured THEN nState := 5; ELSE bConfigured := FALSE; bResetDone := TRUE; nState := 0; END_IF
END_IF

CASE nState OF
    0:
        bBusy := FALSE;
        IF bLoadModel AND NOT(bConfigured) AND NOT(bReset) THEN nState := 10; END_IF
    5:
        bBusy := TRUE;
        IF fbMlSvr.Deconfigure(nTimeout := nConfigureTimeout) THEN
            nErrorCode := fbMlSvr.nErrorCode;
            bError := fbMlSvr.bError OR (nErrorCode <> 0);
            bConfigured := FALSE;
            bBusy := FALSE;
            bResetDone := NOT(bError);
            IF bError THEN nState := 90; ELSIF bReset THEN nState := 0; ELSE nState := 10; END_IF
        END_IF
    10:
        bBusy := TRUE;
        fbMlSvr.stPredictionParameter.sMlModelFilePath := sModelJsonFilePath;
        fbMlSvr.stPredictionParameter.sMlSvrNetId := sMlSvrNetId;
        fbMlSvr.stPredictionParameter.eExecutionProvider := eExecutionProvider;
        IF fbMlSvr.Configure(nTimeout := nConfigureTimeout, nPriority := nPriority) THEN
            nErrorCode := fbMlSvr.nErrorCode;
            bError := fbMlSvr.bError OR (nErrorCode <> 0);
            bConfigured := fbMlSvr.bConfigured AND NOT(bError);
            bBusy := FALSE;
            IF bConfigured THEN nState := 20; ELSE nState := 90; END_IF
        END_IF
    20:
        bBusy := FALSE;
        bPredictionPending := FALSE;
        IF bEnable AND bConfigured AND NOT(bError) AND NOT(bReset) THEN
            FOR nConditionIndex := 0 TO 3 DO
                stModelInput.in_condition[0,nConditionIndex] := aCondition[nConditionIndex];
            END_FOR
            stModelInput.in_direction_flag[0,0] := fDirectionFlag;
            FOR nCurveIndex := 0 TO 2047 DO
                stModelInput.in_k01_prediction_curve[0,nCurveIndex] := aK01PredictionCurve[nCurveIndex];
                stModelInput.in_h08_prediction_curve[0,nCurveIndex] := aH08PredictionCurve[nCurveIndex];
            END_FOR
            bPredictionReady := FALSE;
            bPredictionPending := TRUE;
            nState := 30;
        END_IF
    30:
        bBusy := TRUE;
        bPredictionPending := TRUE;
        IF fbMlSvr.Predict(
            pDataIn := ADR(stModelInput),
            nDataInSize := SIZEOF({INPUT_TYPE_NAME}),
            pDataOut := ADR(stModelOutput),
            nDataOutSize := SIZEOF({OUTPUT_TYPE_NAME}),
            nTimeout := nPredictTimeout,
            nPriority := nPriority) THEN
            nErrorCode := fbMlSvr.nErrorCode;
            bError := fbMlSvr.bError OR (nErrorCode <> 0);
            nMaxInferenceDuration := fbMlSvr.nMaxInferenceDuration;
            bPredictionPending := FALSE;
            bBusy := FALSE;
            IF NOT(bError) THEN
                fForwardGate := stModelOutput.out_forward_gate[0,0];
                fK01Mean := stModelOutput.out_k01_mean[0,0];
                fH08Mean := stModelOutput.out_h08_mean[0,0];
                fLearnedH08Gate := stModelOutput.out_learned_h08_gate[0,0];
                FOR nCurveIndex := 0 TO 2047 DO
                    aK01CenteredCurve[nCurveIndex] := stModelOutput.out_k01_centered_curve[0,nCurveIndex];
                    aH08CenteredDifference[nCurveIndex] := stModelOutput.out_h08_centered_difference[0,nCurveIndex];
                    aH08CenteredResidual[nCurveIndex] := stModelOutput.out_h08_centered_residual[0,nCurveIndex];
                    aPredictionCurve[nCurveIndex] := stModelOutput.out_prediction_curve[0,nCurveIndex];
                END_FOR
                bPredictionReady := TRUE;
                nState := 20;
            ELSE nState := 90;
            END_IF
        END_IF
    90:
        bBusy := FALSE;
        bPredictionPending := FALSE;
        bError := TRUE;
END_CASE

nErrorCode := fbMlSvr.nErrorCode;
nMaxInferenceDuration := fbMlSvr.nMaxInferenceDuration;]]></ST>
    </Implementation>
  </POU>
</TcPlcObject>'''


def install_package() -> None:
    """Install artifacts, generated TwinCAT objects, catalog, and project items."""

    required_file_list = [
        CONVERSION_ROOT / "model.json",
        CONVERSION_ROOT / "model.onnx",
        CONVERSION_ROOT / "model_plcopen.xml",
    ]
    assert SOURCE_ONNX_PATH.is_file()
    assert all(path.is_file() for path in required_file_list)
    MODEL_ROOT.mkdir(parents=True, exist_ok=True)
    for source_path in required_file_list:
        shutil.copy2(source_path, MODEL_ROOT / source_path.name)

    (
        input_declaration,
        output_declaration,
        input_type_name,
        output_type_name,
        _,
        _,
    ) = extract_plain_type_declarations(
        CONVERSION_ROOT / "model_plcopen.xml",
        FAMILY_ID,
    )
    assert input_type_name == INPUT_TYPE_NAME
    assert output_type_name == OUTPUT_TYPE_NAME
    write_text(
        PLC_ROOT / "DUTs" / f"{INPUT_TYPE_NAME}.TcDUT",
        wrap_tc_dut(INPUT_TYPE_NAME, input_declaration),
    )
    write_text(
        PLC_ROOT / "DUTs" / f"{OUTPUT_TYPE_NAME}.TcDUT",
        wrap_tc_dut(OUTPUT_TYPE_NAME, output_declaration),
    )
    write_text(
        PLC_ROOT / "POUs" / "Model Runners" / f"{RUNNER_NAME}.TcPOU",
        build_runner_xml(),
    )

    model_json = read_json(CONVERSION_ROOT / "model.json")
    configuration = model_json[
        "MLlib_JSON_File"
    ]["MachineLearningModel"]["Configuration"]
    input_tensor_map = tensor_shape_map(configuration["Inputs"])
    output_tensor_map = tensor_shape_map(configuration["Outputs"])
    catalog = read_json(CATALOG_PATH)
    package_record = {
            "family_id": FAMILY_ID,
            "enum_name": ENUM_NAME,
            "runner_name": RUNNER_NAME,
            "selectable_in_generic_predictor": False,
            "integration_role": "fixed_grid_curve_composer",
            "input_shape": input_tensor_map["condition"],
            "output_shape": output_tensor_map["forward_gate"],
            "input_tensors": input_tensor_map,
            "output_tensors": output_tensor_map,
            "model_directory": f"ML_models/{FAMILY_ID}",
            "target_json_path": (
                "C:\\Users\\Administrator\\Documents\\ML_Models\\"
                f"{FAMILY_ID}\\model.json"
            ),
            "source_onnx_path": (
                "models/polished_dataset/setpoints/"
                f"{FAMILY_ID}/global/onnx/model.onnx"
            ),
            "source_onnx_sha256": compute_file_sha256(SOURCE_ONNX_PATH),
            "prepared_onnx_sha256": compute_file_sha256(
                MODEL_ROOT / "model.onnx"
            ),
        }
    existing_record_index = next(
        (
            record_index
            for record_index, record in enumerate(catalog["model_list"])
            if record["family_id"] == FAMILY_ID
        ),
        None,
    )
    if existing_record_index is None:
        catalog["model_list"].append(package_record)
    else:
        catalog["model_list"][existing_record_index] = package_record
    catalog["model_list"].sort(key=lambda record: record["family_id"])
    catalog["model_count"] = len(catalog["model_list"])
    write_text(CATALOG_PATH, json.dumps(catalog, indent=2))

    plc_project_text = PLC_PROJECT_PATH.read_text(encoding="utf-8")
    marker = (
        '    <Compile Include="POUs\\FB_TF3820TransmissionErrorPredictor.TcPOU">'
    )
    compile_block = f'''    <Compile Include="DUTs\\{INPUT_TYPE_NAME}.TcDUT">
      <SubType>Code</SubType>
    </Compile>
    <Compile Include="DUTs\\{OUTPUT_TYPE_NAME}.TcDUT">
      <SubType>Code</SubType>
    </Compile>
    <Compile Include="POUs\\Model Runners\\{RUNNER_NAME}.TcPOU">
      <SubType>Code</SubType>
    </Compile>
'''
    if compile_block not in plc_project_text:
        assert marker in plc_project_text
        plc_project_text = plc_project_text.replace(
            marker,
            compile_block + marker,
            1,
        )
    write_text(
        PLC_PROJECT_PATH,
        plc_project_text,
    )

    assert catalog["model_count"] == 40
    print(
        "[PASS] Installed A02 standalone composer package | "
        f"models={catalog['model_count']} | "
        f"onnx={compute_file_sha256(MODEL_ROOT / 'model.onnx')[:12]}",
        flush=True,
    )


if __name__ == "__main__":
    install_package()
