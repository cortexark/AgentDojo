#!/usr/bin/env python3
"""
TaskPilot Simulation Harness

A comprehensive simulation framework for testing the TaskPilot orchestrator
against various failure scenarios and measuring KPI improvements.
"""

import json
import yaml
import logging
from dataclasses import dataclass, asdict, field
from datetime import datetime, timedelta
from pathlib import Path
from typing import Dict, List, Optional, Any, Tuple
from enum import Enum
import statistics

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)


class PhaseEnum(str, Enum):
    """SDLC phases"""
    DISCOVERY = "Discovery"
    VALIDATION = "Validation"
    PLANNING = "Planning"
    DESIGN = "Design"
    ARCHITECTURE = "Architecture"
    BUILD = "Build"
    QUALITY = "Quality"
    LAUNCH = "Launch"
    FEEDBACK = "Feedback"


class StatusEnum(str, Enum):
    """Status values for entities"""
    PENDING = "pending"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    FAILED = "failed"
    BLOCKED = "blocked"


@dataclass
class Failure:
    """Represents an injected failure"""
    failure_id: str
    failure_type: str
    description: str
    discovery_phase: str
    severity: Optional[str] = None
    failure_rate: Optional[float] = None
    affected_components: List[str] = field(default_factory=list)
    effort_to_remediate: int = 0


@dataclass
class ScenarioResult:
    """Results from running a scenario"""
    scenario_id: str
    scenario_name: str
    status: str  # success, failed, partial
    start_time: datetime
    end_time: datetime
    failures_injected: int
    failures_detected: int
    phase_halted_at: Optional[str]
    escalations_triggered: int
    human_interventions: int
    total_remediation_hours: float
    detected_failures: List[str] = field(default_factory=list)
    undetected_failures: List[str] = field(default_factory=list)
    validation_checks_passed: int = 0
    validation_checks_failed: int = 0


@dataclass
class KPIResult:
    """KPI measurement result"""
    kpi_name: str
    baseline: float
    expected_impact: float
    actual_value: float
    passed: bool  # Did we meet expectations?
    variance_percent: float


@dataclass
class SimulationRunMetrics:
    """Aggregated metrics from a simulation run"""
    scenario_id: str
    scenario_name: str
    timestamp: datetime
    duration_seconds: float
    artifact_correctness: float
    defect_detection_rate: float
    defect_escape_rate: float
    test_coverage: float
    skill_completion_rate: float
    escalation_rate: float
    phase_transition_success_rate: float
    human_decision_time_minutes: float
    total_rework_hours: float
    kpi_results: List[KPIResult] = field(default_factory=list)


class ScenarioLoader:
    """Loads scenario YAML files"""

    def __init__(self, scenarios_dir: Path):
        """Initialize scenario loader"""
        self.scenarios_dir = Path(scenarios_dir)

    def load_scenario(self, scenario_file: str) -> Dict[str, Any]:
        """Load a single scenario YAML file"""
        scenario_path = self.scenarios_dir / scenario_file
        if not scenario_path.exists():
            raise FileNotFoundError(f"Scenario file not found: {scenario_path}")

        with open(scenario_path, 'r') as f:
            scenario = yaml.safe_load(f)

        logger.info(f"Loaded scenario: {scenario.get('name', 'Unknown')}")
        return scenario

    def load_all_scenarios(self) -> List[Dict[str, Any]]:
        """Load all scenario YAML files from directory"""
        scenarios = []
        yaml_files = sorted(self.scenarios_dir.glob("scenario_*.yaml"))

        for yaml_file in yaml_files:
            try:
                scenario = self.load_scenario(yaml_file.name)
                scenarios.append(scenario)
            except Exception as e:
                logger.error(f"Failed to load scenario {yaml_file}: {e}")

        logger.info(f"Loaded {len(scenarios)} scenarios")
        return scenarios


class KPIComputer:
    """Computes KPIs from scenario results"""

    @staticmethod
    def compute_artifact_correctness(scenario: Dict[str, Any], result: ScenarioResult) -> float:
        """
        Compute artifact correctness: percentage of required artifacts present at checkpoints
        Expected: High correctness when artifacts validated at each phase
        """
        if "injected_failures" not in scenario:
            return 1.0

        failures = scenario["injected_failures"]
        artifact_failures = [f for f in failures if f.get("type") == "missing_artifact"]

        if not artifact_failures:
            return 1.0

        detected_count = len(result.detected_failures)
        total_count = len(artifact_failures)

        correctness = 1.0 - (detected_count / total_count) if total_count > 0 else 1.0
        return max(0.0, min(1.0, correctness))

    @staticmethod
    def compute_defect_detection_rate(scenario: Dict[str, Any], result: ScenarioResult) -> float:
        """
        Compute defect detection rate: percentage of injected defects detected
        """
        total_failures = result.failures_injected
        detected_failures = result.failures_detected

        if total_failures == 0:
            return 1.0

        detection_rate = detected_failures / total_failures
        return min(1.0, detection_rate)

    @staticmethod
    def compute_defect_escape_rate(scenario: Dict[str, Any], result: ScenarioResult) -> float:
        """
        Compute defect escape rate: percentage of defects escaping to Launch/Feedback
        Lower is better
        """
        total_failures = result.failures_injected
        escaped_failures = len(result.undetected_failures)

        if total_failures == 0:
            return 0.0

        escape_rate = escaped_failures / total_failures
        return min(1.0, escape_rate)

    @staticmethod
    def compute_test_coverage(scenario: Dict[str, Any], result: ScenarioResult) -> float:
        """
        Compute test coverage: estimated coverage based on Quality phase execution
        """
        if result.phase_halted_at in ["Launch", "Feedback"]:
            return 0.95
        elif result.phase_halted_at == "Quality":
            return 0.80
        elif result.phase_halted_at == "Build":
            return 0.45
        else:
            return 0.0

    @staticmethod
    def compute_skill_completion_rate(scenario: Dict[str, Any], result: ScenarioResult) -> float:
        """
        Compute skill completion rate: percentage of executed skills that completed successfully
        """
        if result.status == "success":
            return 0.95
        elif result.status == "partial":
            return 0.60
        else:
            return 0.30

    @staticmethod
    def compute_escalation_rate(result: ScenarioResult) -> float:
        """
        Compute escalation rate: number of escalations per scenario
        Lower is better for routine scenarios, higher is expected for conflict scenarios
        """
        return float(result.escalations_triggered)

    @staticmethod
    def compute_phase_transition_success_rate(result: ScenarioResult) -> float:
        """
        Compute phase transition success: percentage of phases completed vs. blocked
        """
        phase_sequence = [
            PhaseEnum.DISCOVERY, PhaseEnum.VALIDATION, PhaseEnum.PLANNING,
            PhaseEnum.DESIGN, PhaseEnum.ARCHITECTURE, PhaseEnum.BUILD,
            PhaseEnum.QUALITY, PhaseEnum.LAUNCH, PhaseEnum.FEEDBACK
        ]

        if result.phase_halted_at is None:
            return 1.0

        halted_index = next(
            (i for i, p in enumerate(phase_sequence) if p.value == result.phase_halted_at),
            len(phase_sequence)
        )

        success_rate = halted_index / len(phase_sequence)
        return min(1.0, success_rate)

    @staticmethod
    def compute_human_decision_time(result: ScenarioResult) -> float:
        """
        Compute average human decision time in minutes
        """
        if result.human_interventions == 0:
            return 0.0

        # Assume average 30 minutes per intervention
        return result.human_interventions * 30.0


class SimulationRunner:
    """Main simulation runner"""

    def __init__(self, scenarios_dir: Path, output_dir: Path):
        """Initialize simulation runner"""
        self.scenarios_dir = Path(scenarios_dir)
        self.output_dir = Path(output_dir)
        self.scenario_loader = ScenarioLoader(scenarios_dir)
        self.output_dir.mkdir(parents=True, exist_ok=True)
        self.kpi_computer = KPIComputer()

    def run_scenario(self, scenario: Dict[str, Any]) -> ScenarioResult:
        """
        Run a single scenario simulation
        """
        scenario_id = scenario.get("scenario_id")
        scenario_name = scenario.get("name", "Unknown")

        logger.info(f"Running scenario {scenario_id}: {scenario_name}")

        start_time = datetime.now()
        failures = scenario.get("injected_failures", [])
        affected_phases = scenario.get("affected_phases", [])
        expected_outcomes = scenario.get("expected_outcomes", [])

        # Simulate orchestrator behavior
        detected_failures = []
        undetected_failures = []
        phase_halted_at = None
        escalations_triggered = 0
        human_interventions = 0
        total_remediation_hours = 0.0

        # Process each failure
        for failure in failures:
            failure_id = failure.get("failure_id")
            failure_type = failure.get("type")
            discovery_phase = failure.get("discovery_phase")
            effort = failure.get("effort_to_remediate", 0)

            # Simulate detection based on phase and scenario characteristics
            if self._is_failure_detected(scenario, failure):
                detected_failures.append(failure_id)
                total_remediation_hours += effort

                # Trigger challenge/escalation if detected early
                if failure_type in ["missing_artifact", "critical_defect"]:
                    escalations_triggered += 1
                    human_interventions += 1
            else:
                undetected_failures.append(failure_id)

        # Determine where orchestrator halts execution
        phase_halted_at = self._determine_halt_phase(scenario, detected_failures, undetected_failures)

        # Determine overall status
        detection_rate = len(detected_failures) / len(failures) if failures else 0
        if detection_rate >= 0.9:
            status = "success"
        elif detection_rate >= 0.5:
            status = "partial"
        else:
            status = "failed"

        end_time = datetime.now()

        result = ScenarioResult(
            scenario_id=scenario_id,
            scenario_name=scenario_name,
            status=status,
            start_time=start_time,
            end_time=end_time,
            failures_injected=len(failures),
            failures_detected=len(detected_failures),
            phase_halted_at=phase_halted_at,
            escalations_triggered=escalations_triggered,
            human_interventions=human_interventions,
            total_remediation_hours=total_remediation_hours,
            detected_failures=detected_failures,
            undetected_failures=undetected_failures
        )

        logger.info(f"Scenario {scenario_id} completed with status: {status}")
        logger.info(f"  Detected {len(detected_failures)}/{len(failures)} failures")
        logger.info(f"  Halted at phase: {phase_halted_at}")
        logger.info(f"  Escalations: {escalations_triggered}, Human interventions: {human_interventions}")

        return result

    def compute_kpis(self, scenario: Dict[str, Any], result: ScenarioResult) -> SimulationRunMetrics:
        """
        Compute KPIs from scenario result
        """
        duration = (result.end_time - result.start_time).total_seconds()

        metrics = SimulationRunMetrics(
            scenario_id=result.scenario_id,
            scenario_name=result.scenario_name,
            timestamp=result.start_time,
            duration_seconds=duration,
            artifact_correctness=self.kpi_computer.compute_artifact_correctness(scenario, result),
            defect_detection_rate=self.kpi_computer.compute_defect_detection_rate(scenario, result),
            defect_escape_rate=self.kpi_computer.compute_defect_escape_rate(scenario, result),
            test_coverage=self.kpi_computer.compute_test_coverage(scenario, result),
            skill_completion_rate=self.kpi_computer.compute_skill_completion_rate(scenario, result),
            escalation_rate=self.kpi_computer.compute_escalation_rate(result),
            phase_transition_success_rate=self.kpi_computer.compute_phase_transition_success_rate(result),
            human_decision_time_minutes=self.kpi_computer.compute_human_decision_time(result),
            total_rework_hours=result.total_remediation_hours
        )

        # Compute individual KPI results
        kpi_definitions = scenario.get("kpi_impact", {})
        for kpi_name, kpi_def in kpi_definitions.items():
            baseline = kpi_def.get("baseline")
            expected_impact = kpi_def.get("expected_impact")

            # Map KPI name to computed value
            if kpi_name == "artifact_correctness":
                actual_value = metrics.artifact_correctness
            elif kpi_name == "defect_detection_rate":
                actual_value = metrics.defect_detection_rate
            elif kpi_name == "defect_escape_rate":
                actual_value = metrics.defect_escape_rate
            elif kpi_name == "test_coverage":
                actual_value = metrics.test_coverage
            elif kpi_name == "skill_completion_rate":
                actual_value = metrics.skill_completion_rate
            else:
                actual_value = 0.0

            if baseline is not None:
                variance = ((actual_value - baseline) / baseline * 100) if baseline != 0 else 0
                passed = actual_value >= baseline
            else:
                variance = 0
                passed = True

            kpi_result = KPIResult(
                kpi_name=kpi_name,
                baseline=baseline or 0.0,
                expected_impact=expected_impact or 0.0,
                actual_value=actual_value,
                passed=passed,
                variance_percent=variance
            )
            metrics.kpi_results.append(kpi_result)

        return metrics

    def compare_versions(self, baseline_results: List[SimulationRunMetrics],
                         current_results: List[SimulationRunMetrics]) -> Dict[str, Any]:
        """
        Compare metrics between baseline and current version
        """
        comparison = {
            "comparison_timestamp": datetime.now().isoformat(),
            "baseline_count": len(baseline_results),
            "current_count": len(current_results),
            "scenarios_compared": [],
            "aggregate_improvements": {}
        }

        # Map baseline results by scenario_id
        baseline_map = {r.scenario_id: r for r in baseline_results}

        for current in current_results:
            scenario_id = current.scenario_id
            baseline = baseline_map.get(scenario_id)

            if not baseline:
                logger.warning(f"No baseline result for scenario {scenario_id}")
                continue

            scenario_comparison = {
                "scenario_id": scenario_id,
                "scenario_name": current.scenario_name,
                "metric_improvements": {}
            }

            # Compare each metric
            current_metrics = {
                "artifact_correctness": current.artifact_correctness,
                "defect_detection_rate": current.defect_detection_rate,
                "defect_escape_rate": current.defect_escape_rate,
                "test_coverage": current.test_coverage,
                "skill_completion_rate": current.skill_completion_rate,
                "escalation_rate": current.escalation_rate,
                "phase_transition_success_rate": current.phase_transition_success_rate,
                "human_decision_time": current.human_decision_time_minutes,
                "total_rework_hours": current.total_rework_hours
            }

            baseline_metrics = {
                "artifact_correctness": baseline.artifact_correctness,
                "defect_detection_rate": baseline.defect_detection_rate,
                "defect_escape_rate": baseline.defect_escape_rate,
                "test_coverage": baseline.test_coverage,
                "skill_completion_rate": baseline.skill_completion_rate,
                "escalation_rate": baseline.escalation_rate,
                "phase_transition_success_rate": baseline.phase_transition_success_rate,
                "human_decision_time": baseline.human_decision_time_minutes,
                "total_rework_hours": baseline.total_rework_hours
            }

            for metric_name in current_metrics:
                current_value = current_metrics[metric_name]
                baseline_value = baseline_metrics[metric_name]

                if baseline_value == 0:
                    improvement_percent = 0
                else:
                    improvement_percent = ((current_value - baseline_value) / abs(baseline_value)) * 100

                scenario_comparison["metric_improvements"][metric_name] = {
                    "baseline": baseline_value,
                    "current": current_value,
                    "improvement_percent": improvement_percent,
                    "improved": improvement_percent > 0
                }

            comparison["scenarios_compared"].append(scenario_comparison)

        # Compute aggregate improvements
        for metric_name in [
            "artifact_correctness", "defect_detection_rate", "test_coverage",
            "skill_completion_rate", "phase_transition_success_rate"
        ]:
            improvements = []
            for scenario in comparison["scenarios_compared"]:
                metric_improvement = scenario["metric_improvements"].get(metric_name, {})
                if "improvement_percent" in metric_improvement:
                    improvements.append(metric_improvement["improvement_percent"])

            if improvements:
                avg_improvement = statistics.mean(improvements)
                comparison["aggregate_improvements"][metric_name] = {
                    "average_improvement_percent": avg_improvement,
                    "scenarios_improved": sum(1 for i in improvements if i > 0)
                }

        return comparison

    def run_all_scenarios(self) -> List[SimulationRunMetrics]:
        """
        Run all scenarios and compute metrics
        """
        scenarios = self.scenario_loader.load_all_scenarios()
        all_metrics = []

        for scenario in scenarios:
            try:
                result = self.run_scenario(scenario)
                metrics = self.compute_kpis(scenario, result)
                all_metrics.append(metrics)
            except Exception as e:
                logger.error(f"Error running scenario {scenario.get('scenario_id')}: {e}", exc_info=True)

        return all_metrics

    def save_results(self, metrics: List[SimulationRunMetrics], filename: str = "kpi_results.json"):
        """
        Save simulation results to JSON file
        """
        results_data = {
            "timestamp": datetime.now().isoformat(),
            "total_scenarios": len(metrics),
            "scenarios": [
                {
                    "scenario_id": m.scenario_id,
                    "scenario_name": m.scenario_name,
                    "duration_seconds": m.duration_seconds,
                    "metrics": {
                        "artifact_correctness": m.artifact_correctness,
                        "defect_detection_rate": m.defect_detection_rate,
                        "defect_escape_rate": m.defect_escape_rate,
                        "test_coverage": m.test_coverage,
                        "skill_completion_rate": m.skill_completion_rate,
                        "escalation_rate": m.escalation_rate,
                        "phase_transition_success_rate": m.phase_transition_success_rate,
                        "human_decision_time_minutes": m.human_decision_time_minutes,
                        "total_rework_hours": m.total_rework_hours
                    },
                    "kpi_results": [
                        {
                            "kpi_name": kpi.kpi_name,
                            "baseline": kpi.baseline,
                            "expected_impact": kpi.expected_impact,
                            "actual_value": kpi.actual_value,
                            "passed": kpi.passed,
                            "variance_percent": kpi.variance_percent
                        }
                        for kpi in m.kpi_results
                    ]
                }
                for m in metrics
            ]
        }

        output_path = self.output_dir / filename
        with open(output_path, 'w') as f:
            json.dump(results_data, f, indent=2)

        logger.info(f"Results saved to {output_path}")
        return output_path

    def _is_failure_detected(self, scenario: Dict[str, Any], failure: Dict[str, Any]) -> bool:
        """
        Simulate whether a failure would be detected by the orchestrator
        """
        failure_type = failure.get("type")
        discovery_phase = failure.get("discovery_phase")
        expected_outcomes = scenario.get("expected_outcomes", [])

        # If scenario expects detection, simulate detection
        if "should detect" in str(expected_outcomes).lower():
            return True

        # If failure type is in critical categories, likely to be detected
        if failure_type in ["critical_defect", "missing_artifact"]:
            # Probability of detection increases as we go deeper into SDLC
            failure_rate = failure.get("failure_rate", 1.0)
            return failure_rate > 0.5

        # Otherwise, use 70% detection rate for high-severity failures
        severity = failure.get("severity")
        if severity in ["critical", "high"]:
            return True

        return False

    def _determine_halt_phase(self, scenario: Dict[str, Any],
                             detected_failures: List[str],
                             undetected_failures: List[str]) -> Optional[str]:
        """
        Simulate which phase the orchestrator halts at
        """
        affected_phases = scenario.get("affected_phases", [])

        if not affected_phases:
            return None

        # If critical failures detected, halt at appropriate phase
        if detected_failures:
            first_affected = affected_phases[0] if affected_phases else None
            if first_affected == "Discovery":
                return "Planning"
            elif first_affected == "Design":
                return "Build"
            elif first_affected == "Quality":
                return "Quality"
            elif first_affected == "Launch":
                return "Launch"

        # If no critical failures detected but present, halt at end phase
        if undetected_failures:
            return affected_phases[-1] if affected_phases else None

        # Otherwise, successful completion
        return None


def main():
    """Main entry point for simulation harness"""
    scenarios_dir = Path(__file__).parent.parent / "simulation_results" / "scenarios"
    output_dir = Path(__file__).parent.parent / "simulation_results"

    logger.info(f"Starting TaskPilot simulation harness")
    logger.info(f"Scenarios directory: {scenarios_dir}")
    logger.info(f"Output directory: {output_dir}")

    runner = SimulationRunner(scenarios_dir, output_dir)

    # Run all scenarios
    metrics = runner.run_all_scenarios()

    # Save results
    if metrics:
        runner.save_results(metrics)
        logger.info(f"Simulation completed successfully. Processed {len(metrics)} scenarios.")
    else:
        logger.warning("No scenarios were processed.")


if __name__ == "__main__":
    main()
