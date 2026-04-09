<!-- markdownlint-disable MD041 -->

Create a didactic video overview in Italian for beginners and junior engineers.

Goal:
Explain, in a repository-centered way, why the StandardML repository created a
harmonic-wise paper-faithful branch, how that branch is implemented, what the
current baseline result means, and what still remains missing before a real
end-to-end comparison with the RCIM paper can be claimed.

Requirements:

- Follow the narration outline and required chapter order from the uploaded project package.
- Explain the distinction between `Track 1` paper-faithful reproduction and `Track 2` direct-TE comparison.
- Clarify how the supervised problem changes from direct TE prediction to harmonic target prediction.
- Show where the real code, config, artifact root, and canonical reports live in the repository.
- State the current baseline result and the fact that `Target A` is not yet met.
- State clearly that the branch is still offline-only and that the online compensation loop remains future work.
- Use the terminology sheet as the source of truth for wording.
- Respect the fact-boundary notes and avoid unsupported claims.
- Use both the flow diagram and the repository architecture diagram strongly.

Desired output style:

- 5 to 7 minutes
- calm technical teaching tone
- repository motivation first
- implementation structure second
- benchmark status third
- strong visual use of the diagrams
