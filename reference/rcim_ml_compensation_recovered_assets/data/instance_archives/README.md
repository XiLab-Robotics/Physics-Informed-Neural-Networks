# Instance Archives

This folder contains the heavy archived instance material recovered from the
paper workflow.

## Available Archive

- [instance_v1/](./instance_v1/)

Current archive characteristics:

- file count: about `913`
- total size: about `4.68 GB`
- filename pattern:
  `rpm / torque / deg`, for example
  `100.0rpm500.0Torque30.0deg.pickle`

## Interpretation

The filename convention strongly suggests that this subtree contains archived
condition-indexed instances or processed measurement objects rather than model
objects.

This interpretation is also supported by the recovered backup code, where
`instance_v2.py` defines an `Instance` object carrying:

- forward and backward TE signals;
- FFT coefficients;
- operating conditions such as `rpm`, `deg`, and `tor`.

## Current Limitation

A direct unpickle test was not completed successfully because the recovered
code references additional instance-class modules that are not yet fully
recovered in a runnable form, including a missing `instance_v4` dependency in
the later evaluation path.

So the current repository stance should be:

- preserve the archive;
- treat it as valuable recovered evidence;
- do not assume it is immediately runnable without a small reconstruction pass
  of the original instance-class environment.

## Usage Guidance

- Do not treat this subtree as ordinary source code.
- Do not copy these files casually into new experiment outputs.
- Use this archive only when reconstructing or auditing the original paper data
  path, not for generic repository runtime.
