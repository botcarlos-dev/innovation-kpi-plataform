import { useEffect, useState } from "react";

import StatCard from "../components/dashboard/StatCard";
import StatusBadge from "../components/dashboard/StatusBadge";
import KPIHealthChart from "../components/dashboard/KPIHealthChart";
import KPITrendChart from "../components/dashboard/KPITrendChart";
import { getProjects } from "../api/projects";
import { getKPIs } from "../api/kpis";
import { getMeasurements } from "../api/measurements";
import { getAlerts } from "../api/alerts";


function Dashboard() {
  const [projects, setProjects] = useState([]);
  const [kpis, setKPIs] = useState([]);
  const [measurements, setMeasurements] = useState([]);
  const [alerts, setAlerts] = useState([]);

  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);


  useEffect(() => {
    async function loadDashboard() {
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
        console.error("Dashboard error:", err);

        setError(
          err.response?.data?.detail ||
          err.message ||
          "Unable to load dashboard data."
        );
      } finally {
        setLoading(false);
      }
    }

    loadDashboard();
  }, []);
  console.log("First Measurement:", measurements[0]);
	console.log("First KPI:", kpis[0]);

  if (loading) {
    return (
      <div className="page-loading">
        Loading dashboard...
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


  const healthyMeasurements =
    measurements.filter(
      (measurement) =>
        measurement.status === "HEALTHY"
    );

  const warningMeasurements =
    measurements.filter(
      (measurement) =>
        measurement.status === "WARNING"
    );

  const criticalMeasurements =
    measurements.filter(
      (measurement) =>
        measurement.status === "CRITICAL"
    );


  return (
    <div className="dashboard">

      <div className="dashboard-title">
        <div>
          <h2>Performance Overview</h2>

          <p>
            Overview of innovation projects
            and KPI performance.
          </p>
        </div>
      </div>


      <div className="stats-grid">
        <StatCard
          title="Projects"
          value={projects.length}
          description="Active innovation projects"
        />

        <StatCard
          title="KPIs"
          value={kpis.length}
          description="Configured indicators"
        />

        <StatCard
          title="Measurements"
          value={measurements.length}
          description="Historical KPI measurements"
        />

        <StatCard
          title="Alerts"
          value={alerts.length}
          description="Warning and critical conditions"
        />
      </div>


      {/* KPI HEALTH */}
      <div className="dashboard-section">
        <div className="section-header">
          <div>
            <h3>KPI Health</h3>

            <p>
              Current measurement status
              distribution.
            </p>
          </div>
        </div>


        <div className="health-grid">

          <div className="health-card healthy-card">
            <span>
              Healthy
            </span>

            <strong>
              {healthyMeasurements.length}
            </strong>
          </div>


          <div className="health-card warning-card">
            <span>
              Warning
            </span>

            <strong>
              {warningMeasurements.length}
            </strong>
          </div>


          <div className="health-card critical-card">
            <span>
              Critical
            </span>

            <strong>
              {criticalMeasurements.length}
            </strong>
          </div>

        </div>
      </div>


      {/* KPI HEALTH DISTRIBUTION */}
      <div className="dashboard-section">
        <div className="section-header">
          <div>
            <h3>KPI Health Distribution</h3>

            <p>
              Distribution of KPI measurements
              by performance status.
            </p>
          </div>
        </div>


        <KPIHealthChart
          measurements={measurements}
        />
      </div>


      {/* KPI HISTORICAL TRENDS */}
      <div className="dashboard-section">
        <div className="section-header">
          <div>
            <h3>KPI Historical Trends</h3>

            <p>
              Monitor historical KPI performance
              and identify trends over time.
            </p>
          </div>
        </div>

        <KPITrendChart
          measurements={measurements}
          kpis={kpis}
        />
      </div>


      {/* RECENT ALERTS */}
      <div className="dashboard-section">
        <div className="section-header">
          <div>
            <h3>Recent Alerts</h3>

            <p>
              Latest KPI warnings and critical
              conditions.
            </p>
          </div>
        </div>


        <div className="alerts-list">

          {alerts.length === 0 && (
            <div className="empty-state">
              No alerts detected.
            </div>
          )}


          {alerts
            .slice(0, 5)
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


export default Dashboard;
