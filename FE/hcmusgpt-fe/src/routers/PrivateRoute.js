import { Navigate, Outlet } from 'react-router-dom';
import { isLogin } from '../utils';

function PrivateRoute({ element: Element, ...rest }) {
    const isAuth = isLogin();
    return isAuth ? <Outlet /> : <Navigate to="/" />;
}

export default PrivateRoute;
