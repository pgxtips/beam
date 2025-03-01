import { Outlet } from "react-router";

function DashLayout() {
  return (
      <div className="container">
          <Outlet />
      </div>
  );
}

export default DashLayout;
