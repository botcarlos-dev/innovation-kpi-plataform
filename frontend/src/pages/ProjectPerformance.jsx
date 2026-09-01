import { useEffect, useMemo, useState } from "react";

import StatCard from "../components/dashboard/StatCard.jsx";
import StatusBadge from "../components/dashboard/StatusBadge";

import { getProjects } from "../api/projects";
import { getKPIs } from "../api/kpis";
import { getMeasurements } from "../api/measurements";
import { getAlerts } from "../api/alerts";


function ProjectPerformance() {
  const [projects, setProjects] = useState([]);
  const [kpis, setKPIs] = useState([]);
  const [measurements, setMeasurements] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const [selectedProject, setSelectedProject] =
    useState("");

  const [loading, setLoading] =
    useState(true);

  const [error, setError] =
    useState(null);


  useEffect(() => {
    async function loadData() {
      try {
        setLoading(true);

        const [
          projectsData,
          kpisData,
          measurementsData,
          alertsData,
        ] = await Promise.all([
          getProjects(),
          getKPIs(),
          getMeasurements(),
          getAlerts(),
        ]);

        setProjects(projectsData);
        setKPIs(kpisData);
        setMeasurements(measurementsData);
        setAlerts(alertsData);

        setError(null);
      } catch (err) {
        console.error(
          "Project performance error:",
          err
        );

        setError(
          err.response?.data?.detail ||
          err.message ||
          "Unable to load project data."
        );
      } finally {
        setLoading(false);
      }
    }

    loadData();
  }, []);


  const currentProject = useMemo(() => {
    if (!projects.length) {
      return null;
    }

    if (!selectedProject) {
      return projects[0];
    }

    return projects.find(
      (project) =>
        project.id === Number(selectedProject)
    );
  }, [
    projects,
    selectedProject,
  ]);


  const projectMeasurements = useMemo(() => {
    if (!currentProject) {
      return [];
    }

    return measurements.filter(
      (measurement) =>
        measurement.project_id ===
        currentProject.id
    );
  }, [
    measurements,
    currentProject,
  ]);


  const latestMeasurements = useMemo(() => {
    const latestByKPI = {};

    projectMeasurements.forEach(
      (measurement) => {
        const existing =
          latestByKPI[measurement.kpi_id];

        if (
          !existing ||
          new Date(
            measurement.measurement_date
          ) >
            new Date(
              existing.measurement_date
            )
        ) {
          latestByKPI[
            measurement.kpi_id
          ] = measurement;
        }
      }
    );

    return Object.values(latestByKPI);
  }, [projectMeasurements]);


  const projectAlerts = useMemo(() => {
    if (!currentProject) {
      return [];
    }

    return alerts.filter(
      (alert) =>
        alert.project_id ===
        currentProject.id
    );
  }, [
    alerts,
    currentProject,
  ]);


  const getKPI = (kpiId) => {
    return kpis.find(
      (kpi) => kpi.id === kpiId
    );
  };


  if (loading) {
    return (
      <div className="page-loading">
        Loading project performance...
      </div>
    );
  }


  if (error) {
    return (
      <div className="page-error">
        {error}
      </div>
    );
  }


  if (!currentProject) {
    return (
      <div className="empty-state">
        No projects available.
      </div>
    );
  }


  return (
    <div className="project-performance">

      <div className="dashboard-title">
        <div>
          <h2>Project Performance</h2>

          <p>
            Monitor KPI performance,
            trends and operational risks
            for each innovation project.
          </p>
        </div>
      </div>


      {/* PROJECT SELECTOR */}

      <div className="dashboard-section">

        <div className="section-header">
          <div>
            <h3>Select Project</h3>

            <p>
              Choose an innovation project
              to analyse its performance.
            </p>
          </div>
        </div>


        <select
          className="project-selector"
          value={
            selectedProject ||
            currentProject.id
          }
          onChange={(event) =>
            setSelectedProject(
              event.target.value
            )
          }
        >
          {projects.map((project) => (
            <option
              key={project.id}
              value={project.id}
            >
              {project.name}
            </option>
          ))}
        </select>

      </div>


      {/* PROJECT OVERVIEW */}

      <div className="dashboard-section">

        <div className="section-header">
          <div>
            <h3>
              {currentProject.name}
            </h3>

            <p>
              {currentProject.description ||
                "Innovation project performance overview."}
            </p>
          </div>
        </div>


        <div className="stats-grid">

          <StatCard
            title="Measurements"
            value={
              projectMeasurements.length
            }
            description="Historical measurements"
          />

          <StatCard
            title="KPIs Tracked"
            value={
              latestMeasurements.length
            }
            description="Indicators with measurements"
          />

          <StatCard
            title="Alerts"
            value={
              projectAlerts.length
            }
            description="Active warning and critical conditions"
          />

        </div>

      </div>


      {/* LATEST KPI PERFORMANCE */}

      {/* LATEST KPI PERFORMANCE */}

      <div className="dashboard-section">

        <div className="section-header">
          <div>
            <h3>Latest KPI Performance</h3>

            <p>
              Most recent measurement and
              performance thresholds for each KPI.
            </p>
          </div>
        </div>


        <div className="kpi-performance-table">

          {latestMeasurements.length === 0 && (
            <div className="empty-state">
              No KPI measurements available
              for this project.
            </div>
          )}


          {latestMeasurements.map((measurement) => {

            const kpi = getKPI(
              measurement.kpi_id
            );


            return (
              <div
                key={measurement.id}
                className="kpi-performance-row"
              >

                {/* KPI INFORMATION */}

                <div className="kpi-performance-info">

                  <strong>
                    {kpi?.name ||
                `     KPI #${measurement.kpi_id}`}
                  </strong>

                  <span>
                    {kpi?.description ||
                      "No KPI description available."}
                  </span>

                  <small>
                    Latest measurement:{" "}
                    {measurement.measurement_date}
                  </small>

                </div>


                {/* CURRENT VALUE */}

                <div className="kpi-performance-value">

                  <strong>
                    {measurement.value}
                  </strong>

                  <span>
                    {kpi?.unit || ""}
                  </span>

                </div>


                {/* TARGET */}

                <div className="kpi-threshold">

                  <span>
                    Target
                  </span>

                  <strong>
                    {kpi?.target_value ?? "—"}
                    {" "}
                    {kpi?.unit || ""}
                  </strong>

                </div>


                {/* THRESHOLDS */}

                <div className="kpi-threshold">

                  <span>
                    Warning
                  </span>

                  <strong>
                    {kpi?.warning_threshold ?? "—"}
                    {" "}
                    {kpi?.unit || ""}
                  </strong>

                </div>


                <div className="kpi-threshold">

                  <span>
                    Critical
                  </span>

                  <strong>
                    {kpi?.critical_threshold ?? "—"}
                    {" "}
                    {kpi?.unit || ""}
                  </strong>

                </div>


                {/* STATUS */}

                <StatusBadge
                  status={measurement.status}
                />

              </div>
            );
          })}

        </div>

      </div>

      {/* PROJECT ALERTS */}

      <div className="dashboard-section">

        <div className="section-header">
          <div>
            <h3>Project Alerts</h3>

            <p>
              Warning and critical KPI
              conditions for this project.
            </p>
          </div>
        </div>


        <div className="alerts-list">

          {projectAlerts.length === 0 && (
            <div className="empty-state">
              No alerts detected for
              this project.
            </div>
          )}


          {projectAlerts
            .slice(0, 10)
            .map((alert) => (
              <div
                key={alert.id}
                className="alert-row"
              >

                <div className="alert-info">

                  <strong>
                    {alert.title}
                  </strong>

                  <span>
                    {alert.message}
                  </span>

                </div>


                <StatusBadge
                  status={alert.severity}
                />

              </div>
            ))}

        </div>

      </div>

    </div>
  );
}


export default ProjectPerformance;
