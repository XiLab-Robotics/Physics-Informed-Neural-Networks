"""Embryonic Wave 4A adapter for MMT TE equation diagnostics."""

from __future__ import annotations

# Import Standard Libraries
from dataclasses import dataclass
from typing import Any

# Import Numerical Libraries
import numpy as np

# Import MMT Reproduction Utilities
from scripts.paper_reimplementation.mmt_te_modeling.mmt_te_modeling_reproduction import ARCSECOND_PER_RADIAN
from scripts.paper_reimplementation.mmt_te_modeling.mmt_te_modeling_reproduction import EquivalentErrors
from scripts.paper_reimplementation.mmt_te_modeling.mmt_te_modeling_reproduction import ReducerParameters
from scripts.paper_reimplementation.mmt_te_modeling.mmt_te_modeling_reproduction import run_rv80e_demo


@dataclass(frozen=True)
class Wave4MMTDiagnosticSummary:

    """Compact output summary for an MMT diagnostic curve."""

    sample_count: int
    rte_arcsec_mean: float
    rte_arcsec_peak_to_peak: float
    dominant_harmonic_index_list: list[int]
    dominant_harmonic_amplitude_arcsec_list: list[float]
    campaign_readiness: str = "not_campaign_ready"


class Wave4MMTDiagnosticAdapter:

    """Batch-callable diagnostic wrapper around the MMT reproduction."""

    def __init__(
        self,
        reducer_parameters: ReducerParameters | None = None,
        equivalent_errors: EquivalentErrors | None = None,
    ) -> None:
        """Initialize the diagnostic adapter.

        Args:
            reducer_parameters: Optional fixed reducer geometry. The current
                demo path uses the reproduction defaults.
            equivalent_errors: Optional equivalent-error vector reserved for
                later calibrated diagnostics.
        """

        self.reducer_parameters = reducer_parameters or ReducerParameters()
        self.equivalent_errors = equivalent_errors or EquivalentErrors()
        self.campaign_readiness = "not_campaign_ready"
        self.blocker_list = [
            "requires_parameter_inventory",
            "requires_track2h_loss_policy",
            "requires_wave4a_diagnostic_acceptance",
        ]

    def run_demo_curve(self, sample_count: int = 720) -> tuple[np.ndarray, np.ndarray]:

        """Run the existing MMT RV-80E demonstration curve."""

        assert sample_count > 8, f"Sample Count must be greater than 8 | {sample_count}"
        return run_rv80e_demo(sample_count=sample_count)

    def summarize_curve(self, rte_rad: np.ndarray, top_k: int = 8) -> Wave4MMTDiagnosticSummary:

        """Compute a compact harmonic and offset summary for one RTE curve."""

        # Prepare Curve And Spectrum
        rte_arcsec = np.asarray(rte_rad, dtype=float) * ARCSECOND_PER_RADIAN
        centered_rte_arcsec = rte_arcsec - np.mean(rte_arcsec)
        spectrum = np.fft.rfft(centered_rte_arcsec)
        harmonic_bins = np.fft.rfftfreq(centered_rte_arcsec.size, d=1.0 / centered_rte_arcsec.size)
        amplitude = 2.0 * np.abs(spectrum) / centered_rte_arcsec.size
        candidate_index_array = np.argsort(amplitude[1:])[-int(top_k):][::-1] + 1

        return Wave4MMTDiagnosticSummary(
            sample_count=int(rte_arcsec.size),
            rte_arcsec_mean=float(np.mean(rte_arcsec)),
            rte_arcsec_peak_to_peak=float(np.ptp(rte_arcsec)),
            dominant_harmonic_index_list=[int(harmonic_bins[index]) for index in candidate_index_array],
            dominant_harmonic_amplitude_arcsec_list=[float(amplitude[index]) for index in candidate_index_array],
        )

    def run_demo_summary(self, sample_count: int = 720, top_k: int = 8) -> Wave4MMTDiagnosticSummary:

        """Run and summarize the demonstration diagnostic."""

        _, rte_rad = self.run_demo_curve(sample_count=sample_count)
        return self.summarize_curve(rte_rad=rte_rad, top_k=top_k)

    def to_status_dictionary(self) -> dict[str, Any]:

        """Return implementation-readiness metadata for validators."""

        return {
            "implementation_status": "implementation_ready",
            "campaign_readiness": self.campaign_readiness,
            "blocker_list": list(self.blocker_list),
            "adapter": self.__class__.__name__,
            "reducer_tooth_counts": {
                "z1": int(self.reducer_parameters.z1),
                "z2": int(self.reducer_parameters.z2),
                "z4": int(self.reducer_parameters.z4),
                "z5": int(self.reducer_parameters.z5),
            },
        }
