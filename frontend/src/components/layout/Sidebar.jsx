import { NavLink } from "react-router-dom";

function Sidebar() {
  const navigation = [
    {
      label: "Dashboard",
      path: "/",
    },
    {
      label: "Projects",
      path: "/projects",
    },
    {
      label: "KPIs",
      path: "/kpis",
    },
    {
      label: "Measurements",
      path: "/measurements",
    },
    {
      label: "Alerts",
      path: "/alerts",
    },
  ];

  return (
    <aside className="sidebar">
      <div className="sidebar-brand">
        <div className="brand-icon">
          IK
        </div>

        <div>
          <h2>Innovation KPI</h2>
          <span>Management Platform</span>
        </div>
      </div>

      <nav className="sidebar-nav">
        {navigation.map((item) => (
          <NavLink
            key={item.path}
            to={item.path}
            className={({ isActive }) =>
              `nav-item ${isActive ? "active" : ""}`
            }
          >
            {item.label}
          </NavLink>
        ))}
      </nav>

      <div className="sidebar-footer">
        <span>Innovation Management</span>
        <small>v1.0.0</small>
      </div>
    </aside>
  );
}

export default Sidebar;
