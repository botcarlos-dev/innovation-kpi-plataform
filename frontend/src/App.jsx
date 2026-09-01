import { BrowserRouter, Routes, Route } from "react-router-dom";

import Layout from "./components/layout/Layout.jsx"


import Dashboard from "./pages/Dashboard";
import Projects from "./pages/Projects";
import KPIs from "./pages/KPIs";
import Measurements from "./pages/Measurements";
import Alerts from "./pages/Alerts";
import ProjectPerformance from "./pages/ProjectPerformance";


function App() {
  return (
    <BrowserRouter>
      <Layout>
        <Routes>

          <Route
            path="/"
            element={<Dashboard />}
          />

          <Route
            path="/projects"
            element={<Projects />}
          />

          <Route
            path="/project-performance"
            element={<ProjectPerformance />}
          />

          <Route
            path="/kpis"
            element={<KPIs />}
          />

          <Route
            path="/measurements"
            element={<Measurements />}
          />

          <Route
            path="/alerts"
            element={<Alerts />}
          />

        </Routes>
      </Layout>
    </BrowserRouter>
  );
}


export default App;
