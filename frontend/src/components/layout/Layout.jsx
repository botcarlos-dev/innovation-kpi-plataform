import Sidebar from "./Sidebar";
import Header from "./Header";

function Layout({ children }) {
  return (
    <div className="app-layout">
      <Sidebar />

      <main className="main-content">
        <Header />

        <section className="page-content">
          {children}
        </section>
      </main>
    </div>
  );
}

export default Layout;
