"""Generate a standalone TwinCAT TF3820 PLC model-test harness.

The harness is intentionally independent from the TestRig solution. It consumes
the TF3820 artifacts produced by the ONNX family compatibility matrix and emits
a small PLC-only source tree with one generated runner per model.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import uuid
import xml.etree.ElementTree as ET
from dataclasses import dataclass
from pathlib import Path


DEFAULT_MATRIX_ROOT = Path("output/deployment/twincat_onnx_conversion/family_matrix_20260710_shape_fixed")
DEFAULT_OUTPUT_ROOT = Path("reference/codes/TwinCAT_TF3820_StandaloneModelTest")
PRODUCT_VERSION = "3.1.4026.20"
TARGET_MODEL_ROOT = r"C:\TwinCAT\3.1\Boot\ML\tf3820\standalone"
UUID_NAMESPACE = uuid.UUID("814e26b8-e832-4f5d-8c8c-bd3514e416df")


@dataclass(frozen=True)
class ModelEntry:
    """Prepared TF3820 model metadata used for code generation."""

    family_id: str
    enum_name: str
    type_prefix: str
    runner_name: str
    source_directory: Path
    model_directory: Path
    model_json_path: Path
    model_onnx_path: Path
    model_plcopen_path: Path
    input_shape: tuple[int, ...]
    output_shape: tuple[int, ...]
    input_type_declaration: str
    output_type_declaration: str
    input_type_name: str
    output_type_name: str
    input_tensor_name: str
    output_tensor_name: str


def parse_args() -> argparse.Namespace:
    """Parse command-line arguments."""

    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--matrix-root", type=Path, default=DEFAULT_MATRIX_ROOT)
    parser.add_argument("--output-root", type=Path, default=DEFAULT_OUTPUT_ROOT)
    parser.add_argument("--clean", action="store_true", help="Remove the generated harness before writing it.")
    return parser.parse_args()


def stable_guid(name: str) -> str:
    """Return a deterministic TwinCAT-style GUID string."""

    return "{" + str(uuid.uuid5(UUID_NAMESPACE, name)) + "}"


def pascal_identifier(raw_name: str) -> str:
    """Convert a file/family identifier into a compact PascalCase identifier."""

    token_list = re.split(r"[^A-Za-z0-9]+", raw_name)
    return "".join(token[:1].upper() + token[1:] for token in token_list if token)


def enum_identifier(raw_name: str) -> str:
    """Convert a model family identifier into a TwinCAT enum member."""

    token_list = re.split(r"[^A-Za-z0-9]+", raw_name)
    return "Model_" + "_".join(token[:1].upper() + token[1:] for token in token_list if token)


def read_json(path: Path) -> dict:
    """Read a JSON file."""

    return json.loads(path.read_text(encoding="utf-8"))


def extract_plain_type_declarations(plcopen_path: Path, family_id: str) -> tuple[str, str, str, str, str, str]:
    """Extract and rename the generated PLCopen input/output DUT declarations."""

    root = ET.parse(plcopen_path).getroot()
    namespace = {"plc": "http://www.plcopen.org/xml/tc6_0200"}
    declaration_text_list: list[str] = []

    for data_type in root.findall(".//plc:dataType", namespace):
        data_type_name = data_type.attrib.get("name", "")
        if data_type_name not in {"ST_modelInput", "ST_modelOutput"}:
            continue
        plain_node = data_type.find(".//{http://www.w3.org/1999/xhtml}xhtml")
        if plain_node is None or plain_node.text is None:
            raise ValueError(f"Missing plaintext declaration in {plcopen_path}")
        declaration_text_list.append(plain_node.text.strip())

    if len(declaration_text_list) != 2:
        raise ValueError(f"Expected two generated DUT declarations in {plcopen_path}, found {len(declaration_text_list)}")

    type_prefix = pascal_identifier(family_id)
    input_type_name = f"ST_{type_prefix}Input"
    output_type_name = f"ST_{type_prefix}Output"

    input_declaration = declaration_text_list[0].replace("TYPE ST_modelInput :", f"TYPE {input_type_name} :")
    output_declaration = declaration_text_list[1].replace("TYPE ST_modelOutput :", f"TYPE {output_type_name} :")

    input_tensor_match = re.search(r"\b(in_[A-Za-z0-9_]+)\s*:", input_declaration)
    output_tensor_match = re.search(r"\b(out_[A-Za-z0-9_]+)\s*:", output_declaration)
    if input_tensor_match is None or output_tensor_match is None:
        raise ValueError(f"Could not locate generated tensor fields in {plcopen_path}")

    return (
        input_declaration,
        output_declaration,
        input_type_name,
        output_type_name,
        input_tensor_match.group(1),
        output_tensor_match.group(1),
    )


def discover_models(matrix_root: Path) -> list[ModelEntry]:
    """Discover all prepared TF3820 model artifacts from the family matrix."""

    model_entry_list: list[ModelEntry] = []

    for source_directory in sorted(matrix_root.glob("tf3820_*")):
        tf3820_directory = source_directory / "tf3820"
        model_json_path = tf3820_directory / "model.json"
        model_onnx_path = tf3820_directory / "model.onnx"
        model_plcopen_path = tf3820_directory / "model_plcopen.xml"
        if not (model_json_path.exists() and model_onnx_path.exists() and model_plcopen_path.exists()):
            continue

        family_id = source_directory.name.removeprefix("tf3820_")
        model_configuration = read_json(model_json_path)["MLlib_JSON_File"]["MachineLearningModel"]["Configuration"]
        input_shape = tuple(int(value) for value in model_configuration["Inputs"]["TensorDesc0"]["int32_shape"])
        output_shape = tuple(int(value) for value in model_configuration["Outputs"]["TensorDesc0"]["int32_shape"])
        (
            input_type_declaration,
            output_type_declaration,
            input_type_name,
            output_type_name,
            input_tensor_name,
            output_tensor_name,
        ) = extract_plain_type_declarations(model_plcopen_path, family_id)

        type_prefix = pascal_identifier(family_id)
        model_entry_list.append(
            ModelEntry(
                family_id=family_id,
                enum_name=enum_identifier(family_id),
                type_prefix=type_prefix,
                runner_name=f"FB_{type_prefix}Tf3820Runner",
                source_directory=source_directory,
                model_directory=Path("ML_models") / family_id,
                model_json_path=model_json_path,
                model_onnx_path=model_onnx_path,
                model_plcopen_path=model_plcopen_path,
                input_shape=input_shape,
                output_shape=output_shape,
                input_type_declaration=input_type_declaration,
                output_type_declaration=output_type_declaration,
                input_type_name=input_type_name,
                output_type_name=output_type_name,
                input_tensor_name=input_tensor_name,
                output_tensor_name=output_tensor_name,
            )
        )

    if not model_entry_list:
        raise RuntimeError(f"No prepared TF3820 models found under {matrix_root}")

    return model_entry_list


def write_text(path: Path, content: str) -> None:
    """Write text with a final newline."""

    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def wrap_tc_dut(name: str, declaration: str) -> str:
    """Wrap a DUT declaration into a TwinCAT XML object."""

    return f'''<?xml version="1.0" encoding="utf-8"?>
<TcPlcObject Version="1.1.0.1" ProductVersion="{PRODUCT_VERSION}">
  <DUT Name="{name}" Id="{stable_guid("dut:" + name)}">
    <Declaration><![CDATA[{declaration}
]]></Declaration>
  </DUT>
</TcPlcObject>'''


def runner_input_assignment(model: ModelEntry) -> str:
    """Generate ST assignments from the common harness input to the model input tensor."""

    shape = model.input_shape
    tensor_name = model.input_tensor_name
    if shape == (1, 3):
        return f"""stModelInput.{tensor_name}[0,0] := fThetaDot;
\t\t\tstModelInput.{tensor_name}[0,1] := fTemperature;
\t\t\tstModelInput.{tensor_name}[0,2] := fTorque;"""
    if shape == (1, 5):
        return f"""stModelInput.{tensor_name}[0,0] := fTheta;
\t\t\tstModelInput.{tensor_name}[0,1] := fThetaDot;
\t\t\tstModelInput.{tensor_name}[0,2] := fTorque;
\t\t\tstModelInput.{tensor_name}[0,3] := fTemperature;
\t\t\tstModelInput.{tensor_name}[0,4] := fDirectionFlag;"""
    if shape == (1, 33, 4):
        return f"""FOR nSequenceIndex := 0 TO 32 DO
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,0] := fTheta + (INT_TO_REAL(nSequenceIndex) * fThetaStep);
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,1] := fThetaDot;
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,2] := fTorque;
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,3] := fTemperature;
\t\t\tEND_FOR"""
    if shape == (1, 33, 5):
        return f"""FOR nSequenceIndex := 0 TO 32 DO
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,0] := fTheta + (INT_TO_REAL(nSequenceIndex) * fThetaStep);
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,1] := fThetaDot;
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,2] := fTorque;
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,3] := fTemperature;
\t\t\t\tstModelInput.{tensor_name}[0,nSequenceIndex,4] := fDirectionFlag;
\t\t\tEND_FOR"""
    raise ValueError(f"Unsupported input shape for {model.family_id}: {shape}")


def runner_output_assignment(model: ModelEntry) -> str:
    """Generate ST assignments from the generated output tensor to common output array."""

    output_width = model.output_shape[-1]
    tensor_name = model.output_tensor_name
    assignment_list = [f"aPredictionOutput[{index}] := stModelOutput.{tensor_name}[0,{index}];" for index in range(output_width)]
    if output_width <= 8:
        assignment_list.append(f"FOR nOutputIndex := {output_width} TO 8 DO")
        assignment_list.append("\taPredictionOutput[nOutputIndex] := 0.0;")
        assignment_list.append("END_FOR")
    return "\n\t\t\t\t".join(assignment_list)


def generate_runner(model: ModelEntry) -> str:
    """Generate a model-specific TwinCAT function block."""

    input_assignment = runner_input_assignment(model)
    output_assignment = runner_output_assignment(model)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<TcPlcObject Version="1.1.0.1" ProductVersion="{PRODUCT_VERSION}">
  <POU Name="{model.runner_name}" Id="{stable_guid("runner:" + model.runner_name)}" SpecialFunc="None">
    <Declaration><![CDATA[FUNCTION_BLOCK {model.runner_name}
VAR_INPUT
\tsModelJsonFilePath\t: T_MaxString;
\tsMlSvrNetId\t\t\t: T_MaxString := 'local';
\teExecutionProvider\t: E_ExecutionProvider := E_ExecutionProvider.CPU;
\tbEnable\t\t\t\t: BOOL;
\tbReset\t\t\t\t\t: BOOL;
\tbLoadModel\t\t\t: BOOL;
\tnConfigureTimeout\t: UDINT := 1000;
\tnPredictTimeout\t\t: UDINT := 100;
\tnPriority\t\t\t: UDINT := 0;
\tfTheta\t\t\t\t\t: REAL;
\tfThetaDot\t\t\t\t: REAL;
\tfTorque\t\t\t\t: REAL;
\tfTemperature\t\t\t: REAL;
\tfDirectionFlag\t\t: REAL;
\tfThetaStep\t\t\t: REAL := 0.25;
END_VAR
VAR
\tfbMlSvr\t\t\t\t: FB_MlSvrPrediction;
\tstModelInput\t\t: {model.input_type_name};
\tstModelOutput\t\t: {model.output_type_name};
\trtrig_model\t\t\t: R_TRIG;
\tnState\t\t\t\t\t: INT := 0;
\tnSequenceIndex\t\t: INT;
\tnOutputIndex\t\t: INT;
END_VAR
VAR_OUTPUT
\tbConfigured\t\t\t: BOOL;
\tbBusy\t\t\t\t\t: BOOL;
\tbPredictionPending\t: BOOL;
\tbPredictionReady\t: BOOL;
\tbResetDone\t\t\t: BOOL;
\tbError\t\t\t\t\t: BOOL;
\tnErrorCode\t\t\t: HRESULT;
\tnMaxInferenceDuration\t: UDINT;
\taPredictionOutput\t: ARRAY[0..8] OF REAL;
END_VAR]]></Declaration>
    <Implementation>
      <ST><![CDATA[rtrig_model(CLK := bLoadModel);

IF rtrig_model.Q THEN
\tbPredictionPending := FALSE;
\tbPredictionReady := FALSE;
\tbResetDone := FALSE;
\tbError := FALSE;
\tIF fbMlSvr.bConfigured THEN
\t\tnState := 5;
\tELSE
\t\tbConfigured := FALSE;
\t\tnState := 10;
\tEND_IF
END_IF

IF bReset THEN
\tbPredictionPending := FALSE;
\tbPredictionReady := FALSE;
\tbError := FALSE;
\tIF fbMlSvr.bConfigured THEN
\t\tnState := 5;
\tELSE
\t\tbConfigured := FALSE;
\t\tbResetDone := TRUE;
\t\tnState := 0;
\tEND_IF
END_IF

CASE nState OF
\t0:
\t\tbBusy := FALSE;
\t\tIF bLoadModel AND NOT(bConfigured) AND NOT(bReset) THEN
\t\t\tnState := 10;
\t\tEND_IF

\t5:
\t\tbBusy := TRUE;
\t\tIF fbMlSvr.Deconfigure(nTimeout := nConfigureTimeout) THEN
\t\t\tnErrorCode := fbMlSvr.nErrorCode;
\t\t\tbError := fbMlSvr.bError OR (nErrorCode <> 0);
\t\t\tbConfigured := FALSE;
\t\t\tbBusy := FALSE;
\t\t\tbResetDone := NOT(bError);
\t\t\tIF bError THEN
\t\t\t\tnState := 90;
\t\t\tELSIF bReset THEN
\t\t\t\tnState := 0;
\t\t\tELSE
\t\t\t\tnState := 10;
\t\t\tEND_IF
\t\tEND_IF

\t10:
\t\tbBusy := TRUE;
\t\tfbMlSvr.stPredictionParameter.sMlModelFilePath := sModelJsonFilePath;
\t\tfbMlSvr.stPredictionParameter.sMlSvrNetId := sMlSvrNetId;
\t\tfbMlSvr.stPredictionParameter.eExecutionProvider := eExecutionProvider;
\t\tIF fbMlSvr.Configure(nTimeout := nConfigureTimeout, nPriority := nPriority) THEN
\t\t\tnErrorCode := fbMlSvr.nErrorCode;
\t\t\tbError := fbMlSvr.bError OR (nErrorCode <> 0);
\t\t\tbConfigured := fbMlSvr.bConfigured AND NOT(bError);
\t\t\tbBusy := FALSE;
\t\t\tIF bConfigured THEN
\t\t\t\tnState := 20;
\t\t\tELSE
\t\t\t\tnState := 90;
\t\t\tEND_IF
\t\tEND_IF

\t20:
\t\tbBusy := FALSE;
\t\tbPredictionPending := FALSE;
\t\tIF bEnable AND bConfigured AND NOT(bError) AND NOT(bReset) THEN
\t\t\t{input_assignment}
\t\t\tbPredictionReady := FALSE;
\t\t\tbPredictionPending := TRUE;
\t\t\tnState := 30;
\t\tEND_IF

\t30:
\t\tbBusy := TRUE;
\t\tbPredictionPending := TRUE;
\t\tIF fbMlSvr.Predict(
\t\t\tpDataIn := ADR(stModelInput),
\t\t\tnDataInSize := SIZEOF({model.input_type_name}),
\t\t\tpDataOut := ADR(stModelOutput),
\t\t\tnDataOutSize := SIZEOF({model.output_type_name}),
\t\t\tnTimeout := nPredictTimeout,
\t\t\tnPriority := nPriority) THEN
\t\t\tnErrorCode := fbMlSvr.nErrorCode;
\t\t\tbError := fbMlSvr.bError OR (nErrorCode <> 0);
\t\t\tnMaxInferenceDuration := fbMlSvr.nMaxInferenceDuration;
\t\t\tbPredictionPending := FALSE;
\t\t\tbBusy := FALSE;
\t\t\tIF NOT(bError) THEN
\t\t\t\t{output_assignment}
\t\t\t\tbPredictionReady := TRUE;
\t\t\t\tnState := 20;
\t\t\tELSE
\t\t\t\tnState := 90;
\t\t\tEND_IF
\t\tEND_IF

\t90:
\t\tbBusy := FALSE;
\t\tbPredictionPending := FALSE;
\t\tbError := TRUE;
END_CASE

nErrorCode := fbMlSvr.nErrorCode;
nMaxInferenceDuration := fbMlSvr.nMaxInferenceDuration;]]></ST>
    </Implementation>
  </POU>
</TcPlcObject>'''


def generate_enum(model_entry_list: list[ModelEntry]) -> str:
    """Generate the model selection enum DUT."""

    enum_lines = [f"\t{model.enum_name} := {index}" for index, model in enumerate(model_entry_list)]
    declaration = "{attribute 'qualified_only'}\n{attribute 'strict'}\nTYPE E_TF3820StandaloneModelId :\n(\n"
    declaration += ",\n".join(enum_lines)
    declaration += "\n);\nEND_TYPE"
    return wrap_tc_dut("E_TF3820StandaloneModelId", declaration)


def generate_program(model_entry_list: list[ModelEntry]) -> str:
    """Generate the standalone top-level test program."""

    runner_declarations = "\n".join(f"\tfb{model.type_prefix}\t: {model.runner_name};" for model in model_entry_list)
    case_lines: list[str] = []
    for model in model_entry_list:
        model_path = TARGET_MODEL_ROOT + "\\" + model.family_id + r"\model.json"
        case_lines.append(
            f"""\tE_TF3820StandaloneModelId.{model.enum_name}:
\t\tfb{model.type_prefix}(
\t\t\tsModelJsonFilePath := '{model_path}',
\t\t\tsMlSvrNetId := sMlSvrNetId,
\t\t\teExecutionProvider := eExecutionProvider,
\t\t\tbEnable := bEnablePrediction,
\t\t\tbReset := bReset,
\t\t\tbLoadModel := bLoadSelectedModel,
\t\t\tnConfigureTimeout := nConfigureTimeout,
\t\t\tnPredictTimeout := nPredictTimeout,
\t\t\tnPriority := nPriority,
\t\t\tfTheta := fTheta,
\t\t\tfThetaDot := fThetaDot,
\t\t\tfTorque := fTorque,
\t\t\tfTemperature := fTemperature,
\t\t\tfDirectionFlag := fDirectionFlag,
\t\t\tfThetaStep := fThetaStep,
\t\t\tbConfigured => bConfigured,
\t\t\tbBusy => bBusy,
\t\t\tbPredictionPending => bPredictionPending,
\t\t\tbPredictionReady => bPredictionReady,
\t\t\tbResetDone => bResetDone,
\t\t\tbError => bError,
\t\t\tnErrorCode => nErrorCode,
\t\t\tnMaxInferenceDuration => nMaxInferenceDuration,
\t\t\taPredictionOutput => aPredictionOutput);"""
        )

    case_body = "\n".join(case_lines)
    return f'''<?xml version="1.0" encoding="utf-8"?>
<TcPlcObject Version="1.1.0.1" ProductVersion="{PRODUCT_VERSION}">
  <POU Name="P_TF3820StandaloneModelTest" Id="{stable_guid("program:P_TF3820StandaloneModelTest")}" SpecialFunc="None">
    <Declaration><![CDATA[PROGRAM P_TF3820StandaloneModelTest
VAR_INPUT
\tSelectedModel\t\t: E_TF3820StandaloneModelId := E_TF3820StandaloneModelId.{model_entry_list[0].enum_name};
\tbLoadSelectedModel\t: BOOL := TRUE;
\tbEnablePrediction\t: BOOL := TRUE;
\tbReset\t\t\t\t: BOOL;
\tsMlSvrNetId\t\t\t: T_MaxString := 'local';
\teExecutionProvider\t: E_ExecutionProvider := E_ExecutionProvider.CPU;
\tnConfigureTimeout\t: UDINT := 1000;
\tnPredictTimeout\t\t: UDINT := 100;
\tnPriority\t\t\t: UDINT := 0;
\tfTheta\t\t\t\t\t: REAL := 0.0;
\tfThetaDot\t\t\t\t: REAL := 500.0;
\tfTorque\t\t\t\t: REAL := 100.0;
\tfTemperature\t\t\t: REAL := 30.0;
\tfDirectionFlag\t\t: REAL := 1.0;
\tfThetaStep\t\t\t: REAL := 0.25;
END_VAR
VAR_OUTPUT
\tbConfigured\t\t\t: BOOL;
\tbBusy\t\t\t\t\t: BOOL;
\tbPredictionPending\t: BOOL;
\tbPredictionReady\t: BOOL;
\tbResetDone\t\t\t: BOOL;
\tbError\t\t\t\t\t: BOOL;
\tnErrorCode\t\t\t: HRESULT;
\tnMaxInferenceDuration\t: UDINT;
\taPredictionOutput\t: ARRAY[0..8] OF REAL;
END_VAR
VAR
{runner_declarations}
END_VAR]]></Declaration>
    <Implementation>
      <ST><![CDATA[CASE SelectedModel OF
{case_body}
END_CASE]]></ST>
    </Implementation>
  </POU>
</TcPlcObject>'''


def generate_task() -> str:
    """Generate the PLC task object."""

    return f'''<?xml version="1.0" encoding="utf-8"?>
<TcPlcObject Version="1.1.0.1" ProductVersion="{PRODUCT_VERSION}">
  <Task Name="PlcTask_TF3820Standalone" Id="{stable_guid("task:PlcTask_TF3820Standalone")}">
    <CycleTime>1000</CycleTime>
    <Priority>10</Priority>
    <PouCall>
      <Name>P_TF3820StandaloneModelTest</Name>
    </PouCall>
  </Task>
</TcPlcObject>'''


def generate_plcproj(model_entry_list: list[ModelEntry]) -> str:
    """Generate a PLC project file."""

    compile_items = [
        "DUTs\\E_TF3820StandaloneModelId.TcDUT",
        "PlcTask_TF3820Standalone.TcTTO",
    ]
    for model in model_entry_list:
        compile_items.append(f"DUTs\\{model.input_type_name}.TcDUT")
        compile_items.append(f"DUTs\\{model.output_type_name}.TcDUT")
        compile_items.append(f"POUs\\{model.runner_name}.TcPOU")
    compile_items.append("POUs\\P_TF3820StandaloneModelTest.TcPOU")

    compile_xml = "\n".join(
        f'''    <Compile Include="{item}">
      <SubType>Code</SubType>
    </Compile>'''
        for item in compile_items
    )

    return f'''<Project DefaultTargets="Build" xmlns="http://schemas.microsoft.com/developer/msbuild/2003">
  <PropertyGroup>
    <FileVersion>1.0.0.0</FileVersion>
    <SchemaVersion>2.0</SchemaVersion>
    <ProjectGuid>{stable_guid("plcproj:TF3820StandalonePLC").lower()}</ProjectGuid>
    <SubObjectsSortedByName>True</SubObjectsSortedByName>
    <DownloadApplicationInfo>true</DownloadApplicationInfo>
    <WriteProductVersion>true</WriteProductVersion>
    <GenerateTpy>false</GenerateTpy>
    <Name>TF3820StandalonePLC</Name>
    <ProgramVersion>{PRODUCT_VERSION}</ProgramVersion>
    <Application>{stable_guid("plcproj:application").lower()}</Application>
    <TypeSystem>{stable_guid("plcproj:typesystem").lower()}</TypeSystem>
    <LibraryReferences>{stable_guid("plcproj:libraries").lower()}</LibraryReferences>
  </PropertyGroup>
  <ItemGroup>
{compile_xml}
  </ItemGroup>
  <ItemGroup>
    <Folder Include="DUTs" />
    <Folder Include="POUs" />
  </ItemGroup>
  <ItemGroup>
    <PlaceholderReference Include="Tc2_Standard">
      <DefaultResolution>Tc2_Standard, * (Beckhoff Automation GmbH)</DefaultResolution>
      <Namespace>Tc2_Standard</Namespace>
    </PlaceholderReference>
    <PlaceholderReference Include="Tc2_System">
      <DefaultResolution>Tc2_System, * (Beckhoff Automation GmbH)</DefaultResolution>
      <Namespace>Tc2_System</Namespace>
    </PlaceholderReference>
    <PlaceholderReference Include="Tc3_MlServer">
      <DefaultResolution>Tc3_MlServer, * (Beckhoff Automation GmbH)</DefaultResolution>
      <Namespace>Tc3_MlServer</Namespace>
    </PlaceholderReference>
  </ItemGroup>
</Project>'''


def generate_sln() -> str:
    """Generate a Visual Studio solution that references the TwinCAT project."""

    return f'''Microsoft Visual Studio Solution File, Format Version 12.00
# Visual Studio Version 17
VisualStudioVersion = 17.14.36930.0
MinimumVisualStudioVersion = 10.0.40219.1
Project("{{B1E792BE-AA5F-4E3C-8C82-674BF9C0715B}}") = "TwinCAT_TF3820_StandaloneModelTest", "TwinCAT_TF3820_StandaloneModelTest.tsproj", "{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}"
EndProject
Global
\tGlobalSection(SolutionConfigurationPlatforms) = preSolution
\t\tDebug|TwinCAT RT (x64) = Debug|TwinCAT RT (x64)
\t\tRelease|TwinCAT RT (x64) = Release|TwinCAT RT (x64)
\tEndGlobalSection
\tGlobalSection(ProjectConfigurationPlatforms) = postSolution
\t\t{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}.Debug|TwinCAT RT (x64).ActiveCfg = Debug|TwinCAT RT (x64)
\t\t{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}.Debug|TwinCAT RT (x64).Build.0 = Debug|TwinCAT RT (x64)
\t\t{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}.Release|TwinCAT RT (x64).ActiveCfg = Release|TwinCAT RT (x64)
\t\t{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}.Release|TwinCAT RT (x64).Build.0 = Release|TwinCAT RT (x64)
\tEndGlobalSection
\tGlobalSection(SolutionProperties) = preSolution
\t\tHideSolutionNode = FALSE
\tEndGlobalSection
EndGlobal'''


def generate_tsproj() -> str:
    """Generate a minimal TwinCAT system-manager project."""

    return f'''<?xml version="1.0"?>
<TcSmProject xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:noNamespaceSchemaLocation="http://www.beckhoff.com/schemas/2012/07/TcSmProject" TcSmVersion="1.0" TcVersion="{PRODUCT_VERSION}">
\t<Project ProjectGUID="{stable_guid("tsproj:TwinCAT_TF3820_StandaloneModelTest")}" Target64Bit="true" AutoPrioManagement="true">
\t\t<System>
\t\t\t<Settings MaxCpus="1" NonWinCpus="1">
\t\t\t\t<Cpu CpuId="1" BaseTime="1000"/>
\t\t\t</Settings>
\t\t\t<Tasks>
\t\t\t\t<Task Id="1" Priority="10" CycleTime="10000" AmsPort="350" DisableFpExceptions="true" AdtTasks="true">
\t\t\t\t\t<Name>PlcTask_TF3820Standalone</Name>
\t\t\t\t</Task>
\t\t\t</Tasks>
\t\t</System>
\t\t<Plc>
\t\t\t<Project GUID="{stable_guid("plcproj:TF3820StandalonePLC")}" Name="TF3820StandalonePLC" PrjFilePath="PLC_project\\TF3820StandalonePLC.plcproj" AmsPort="851" FileArchiveSettings="#x000e" SymbolicMapping="true" />
\t\t</Plc>
\t</Project>
</TcSmProject>'''


def generate_readme(model_entry_list: list[ModelEntry]) -> str:
    """Generate the harness README."""

    shape_lines = []
    shape_counter: dict[tuple[tuple[int, ...], tuple[int, ...]], int] = {}
    for model in model_entry_list:
        key = (model.input_shape, model.output_shape)
        shape_counter[key] = shape_counter.get(key, 0) + 1
    for (input_shape, output_shape), count in sorted(shape_counter.items(), key=lambda item: (item[0][0], item[0][1])):
        shape_lines.append(f"- `{list(input_shape)}` -> `{list(output_shape)}`: {count} model(s)")

    return f"""# TwinCAT TF3820 Standalone Model Test

This folder is generated from the StandardML TF3820 compatibility matrix. It is
intended for a blank Beckhoff PLC target with TwinCAT and TF3820 installed.

The harness is independent from the full TestRig project. It provides one
generated runner per prepared model and a top-level PLC program:

```text
P_TF3820StandaloneModelTest
```

Model artifacts are copied under:

```text
ML_models/<family_id>/
```

Before runtime testing, copy that folder to the target path expected by the PLC:

```text
{TARGET_MODEL_ROOT}
```

Supported shape groups:

{chr(10).join(shape_lines)}

Runtime validation flow:

1. Open `TwinCAT_TF3820_StandaloneModelTest.sln`.
2. Resolve the `Tc3_MlServer` library.
3. Build the PLC project.
4. Copy `ML_models` to `{TARGET_MODEL_ROOT}` on the target.
5. Start `TcMlServer`.
6. Select a value of `SelectedModel`.
7. Pulse `bLoadSelectedModel`.
8. Enable `bEnablePrediction`.
9. Watch `bPredictionReady`, `bError`, `nErrorCode`,
   `nMaxInferenceDuration`, and `aPredictionOutput`.

The synthetic input contract is common across models:

```text
theta, theta_dot, tau_load, T, direction_flag
```

Sequence models receive the same operating point repeated over 33 samples with
`fThetaStep` added to `theta` at each sequence index.
"""


def generate_catalog(model_entry_list: list[ModelEntry]) -> str:
    """Generate a JSON catalog for external tooling and documentation."""

    catalog = []
    for model in model_entry_list:
        catalog.append(
            {
                "family_id": model.family_id,
                "enum_name": model.enum_name,
                "runner_name": model.runner_name,
                "input_shape": list(model.input_shape),
                "output_shape": list(model.output_shape),
                "model_directory": model.model_directory.as_posix(),
                "target_json_path": f"{TARGET_MODEL_ROOT}\\{model.family_id}\\model.json",
            }
        )
    return json.dumps({"schema_version": 1, "model_count": len(catalog), "model_list": catalog}, indent=2)


def copy_model_artifacts(output_root: Path, model: ModelEntry) -> None:
    """Copy prepared model artifacts into the standalone harness."""

    destination = output_root / model.model_directory
    destination.mkdir(parents=True, exist_ok=True)
    shutil.copy2(model.model_json_path, destination / "model.json")
    shutil.copy2(model.model_onnx_path, destination / "model.onnx")
    shutil.copy2(model.model_plcopen_path, destination / "model_plcopen.xml")


def generate_harness(matrix_root: Path, output_root: Path, clean: bool) -> None:
    """Generate all harness files."""

    model_entry_list = discover_models(matrix_root)
    if clean and output_root.exists():
        shutil.rmtree(output_root)

    write_text(output_root / "TwinCAT_TF3820_StandaloneModelTest.sln", generate_sln())
    write_text(output_root / "TwinCAT_TF3820_StandaloneModelTest.tsproj", generate_tsproj())
    write_text(output_root / "PLC_project" / "TF3820StandalonePLC.plcproj", generate_plcproj(model_entry_list))
    write_text(output_root / "PLC_project" / "PlcTask_TF3820Standalone.TcTTO", generate_task())
    write_text(output_root / "PLC_project" / "DUTs" / "E_TF3820StandaloneModelId.TcDUT", generate_enum(model_entry_list))
    write_text(output_root / "PLC_project" / "POUs" / "P_TF3820StandaloneModelTest.TcPOU", generate_program(model_entry_list))
    write_text(output_root / "README.md", generate_readme(model_entry_list))
    write_text(output_root / "model_catalog.json", generate_catalog(model_entry_list))

    for model in model_entry_list:
        write_text(output_root / "PLC_project" / "DUTs" / f"{model.input_type_name}.TcDUT", wrap_tc_dut(model.input_type_name, model.input_type_declaration))
        write_text(output_root / "PLC_project" / "DUTs" / f"{model.output_type_name}.TcDUT", wrap_tc_dut(model.output_type_name, model.output_type_declaration))
        write_text(output_root / "PLC_project" / "POUs" / f"{model.runner_name}.TcPOU", generate_runner(model))
        copy_model_artifacts(output_root, model)


def main() -> None:
    """Run the generator."""

    args = parse_args()
    generate_harness(matrix_root=args.matrix_root, output_root=args.output_root, clean=args.clean)


if __name__ == "__main__":
    main()
